import logging
import os
import slack
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackBot:
    def __init__(self): 
        load_dotenv()
        self.client = WebClient(token=os.getenv("SLACK_API_TOKEN"))
        self.logger = logging.getLogger(__name__)

        # ID of channel you want to post message to
        self.channel_id = SlackBot.find_id(self, name="bot-testing-2-electric-boogaloo")

    def find_id(self, name):
        """Find Slack channel ID by name."""
        try:
            response = self.client.conversations_list()
            for channel in response["channels"]:
                if channel["name"] == name:
                    print(f"Found conversation ID: {channel['id']}")
                    return channel["id"]
            print("Channel not found!")
            return None
        except SlackApiError as e:
            print(f"Error retrieving channels: {e}")
            return None

    def send_message(self, text="Hello World!"):
        """Send a message to a Slack channel."""
        if not self.channel_id:
            print("Error: Channel ID not found. Cannot send message.")
            return 
        try:
            result = self.client.chat_postMessage(
                channel=self.channel_id,
                text=text
            )
            print("Message sent successfully:", result)

        except SlackApiError as e:
            print(f"Error sending message: {e}")

    def retrieve_last_message(self):
        result = self.client.conversations_history(channel=self.channel_id)
        last_message = result["messages"][0]["text"]
        return last_message