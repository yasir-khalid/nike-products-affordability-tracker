# using Jordan's collections as an Example
# https://www.nike.com/gb/t/air-jordan-1-mid-shoes-XkK3zR/DQ8426-517
import os

NIKE_URL = os.getenv(
    "NIKE_URL",
    "https://www.nike.com/gb/t/air-jordan-1-hi-flyease-shoes-DJ1dk0/CQ3835-061",
)
MY_BUDGET = os.getenv("MY_BUDGET", 100)


# AUTH TOKENS
SLACK_WEBHOOK_PIKACHU_WORKFLOWS = os.getenv(
    "SLACK_WEBHOOK_PIKACHU_WORKFLOWS", default=None
)
