import config
import os

from prefect_slack import SlackWebhook
from prefect_slack.messages import send_incoming_webhook_message

webhook_url = config.SLACK_WEBHOOK_PIKACHU_WORKFLOWS

def post_to_slack(message: str):
    send_incoming_webhook_message(
        slack_webhook=SlackWebhook(
            url=webhook_url
        ),
        text= message
    )