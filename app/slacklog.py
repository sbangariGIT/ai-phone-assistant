import os
from dotenv import load_dotenv
from slack import WebClient

class Logger:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        self.slack_client = WebClient(os.getenv('SLACK_BOT_TOKEN'))

    def notify_slack(self, message):
        self.debug_print(f"Sending Slack Message: {message}")
        message = f"[AI_PHONE_ASSISTANT] " + message
        self.slack_client.chat_postMessage(
        channel='monitor-cloud',
        text=message)

dbg = Logger()