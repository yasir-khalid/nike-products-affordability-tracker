# using Jordan's collections as an Example

import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from `.env` file in root dir

NIKE_URL = os.getenv(
    "NIKE_URL",
    "https://www.nike.com/gb/t/air-jordan-1-hi-flyease-shoes-DJ1dk0/CQ3835-061",
)

MY_BUDGET = int(os.getenv("MY_BUDGET", 100))

# AUTH TOKENS
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK", default=None)
