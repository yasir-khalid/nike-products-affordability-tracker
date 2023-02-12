# using Jordan's collections as an Example

import os
from os import environ
import json

from dotenv import load_dotenv

load_dotenv()  # take environment variables from `.env` file in root dir

# BUSINESS LOGIC CUSTOMISATION
NIKE_URL = os.getenv(
    "NIKE_URL",
    "https://www.nike.com/gb/t/dunk-low-retro-shoes-szNRv1/FB3354-001",
)

MY_BUDGET = int(os.getenv("MY_BUDGET", 100))

# SLACK CONFIGURATIONS & AUTH TOKENS
SLACK_NOTIFICATIONS = bool(
        json.loads(environ.get('SLACK_NOTIFICATIONS', 'false').lower())
    )
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK", default=None)

# PREFECT 2.0 CUSTOMISATIONS
PREFECT_DEPLOYMENT = bool(
        json.loads(environ.get('PREFECT_DEPLOYMENT', 'false').lower())
    )
