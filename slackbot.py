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
        channel_name = name
        conversation_id = None
        try:
            # Call the conversations.list method using the WebClient
            for result in self.client.conversations_list():
                if conversation_id is not None:
                    break
                for channel in result["channels"]:
                    if channel["name"] == channel_name:
                        conversation_id = channel["id"]
                        #Print result
                        print(f"Found conversation ID: {conversation_id}")
                        break

        except SlackApiError as e:
            print(f"Error: {e}")

    def send_message(self):
        try:
            # Call the conversations.list method using the WebClient
            result = self.client.chat_postMessage(
                channel=self.channel_id,
                text="Hello world!"
                # You could also use a blocks[] array to send richer content
            )
            # Print result, which includes information about the message (like TS)
            print(result)

        except SlackApiError as e:
            print(f"Error: {e}")