import slack 
import os
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# code is from the slackbot v5 repo

load_dotenv()

channel_id = "C04JY822TK8"  # proj-slackbot channel ID
slack_token = os.getenv("SLACK_API_TOKEN") # WorkerBee bot token

def send_slack_message(message: str):
    '''
    Send a message to our Slack channel.
    '''
    client = WebClient(token=slack_token)


    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text=message
        )
        print("Message sent successfully:", response["ts"])
    except SlackApiError as e:
        print("Error sending message to Slack:", e.response["error"])
       

def main (message_text: str):
    '''
    Main function where we can to build our logic.
    '''
    send_slack_message(message= message_text)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description= 'Send messages to Slack')
    parser.add_argument('--message', '-m', type=str, default='')
    args = parser.parse_args()

    msg = args.message

    if len(msg) >0: 
        main(message_text = msg)
    else: 
        print('Give me a message!')