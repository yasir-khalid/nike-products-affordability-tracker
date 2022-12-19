import requests
import re
import os
from bs4 import BeautifulSoup

import config
from helpers.logs import init_logger
from helpers.slack_notifications import post_to_slack
from helpers.git_history import get_git_revision_short_hash

from prefect import flow, task, get_run_logger
from prefect.context import get_run_context
from prefect.deployments import Deployment

logging = init_logger(name=__name__)

# Scraping the HTML content from Nike's website
@task(name="Scraping Nike website URL")
def scrap_nike_website(url: str) -> int:
    logger = get_run_logger()

    web_get = requests.get(url).text
    soup = BeautifulSoup(web_get, "html.parser")
    logger.info(f"Scraping of {url[:35]} ... completed")
    return soup


# Parsing the HTML content extracted from site, for certain pre-specified tags
@task(name="Parsing HTML content for product and price")
def parsing_html_content(soup_html_parser):
    logger = get_run_logger()

    price_string = soup_html_parser.find("div", {"class": "product-price"}).text
    price_string_cleaned = price_string.replace(" ", "")
    price = float(re.search("[0-9]+.[0-9]+", price_string_cleaned).group(0))
    merchandise = soup_html_parser.find("h1", {"data-test": "product-title"}).text
    logger.info(f"Found '{merchandise}' with price: £ {price}")
    return price, merchandise


# Comparison extracted price tag vs my personal budget to check affordability
@task(name="Checking affordability of Nike product")
def check_affordability(current_price, my_budget):
    logger = get_run_logger()
    logger.info(f"Nike merchandise price from official store: {current_price}")
    logger.info(f"Your current budget: {my_budget}")
    if current_price <= my_budget:
        logger.info("Shoes are within your affordability range")
        return True
    else:
        logger.info(
            f"Out of your affordability range by £{round(current_price - my_budget, 2)}"
        )
        return False


# --- Combining the entire execution into 1 main function i.e. Flow ----


@flow(name="Fetching prices from Nike website")
def pipeline(nike_url, my_budget=100):

    html_parser = scrap_nike_website(nike_url)
    price, merchandise = parsing_html_content(html_parser)

    if check_affordability(current_price=price, my_budget=config.MY_BUDGET):
        post_to_slack(
            f"{merchandise} priced: £ {price} within your affordability range"
        )
    else:
        post_to_slack(
            f"{merchandise} priced: £ {price} outside of your affordability range"
        )


if __name__ == "__main__":
    pipeline(config.NIKE_URL, config.MY_BUDGET)

    deployment = Deployment.build_from_flow(
        flow=pipeline,
        name="Nike-affordability-checker",
        version=get_git_revision_short_hash(),
        work_queue_name="local-laptop-prefect-runner",
    )
    deployment.apply()
