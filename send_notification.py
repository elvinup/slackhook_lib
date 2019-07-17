import os
import slack
from configparser import ConfigParser

def send_text(text, channel):
    parser = ConfigParser()
    parser.read('config/config.ini')
    slacktoken = parser.get('auth', 'slacktoken')

    client = slack.WebClient(token=slacktoken)

    response = client.chat_postMessage(
        channel=channel,
        text=text)
    assert response["ok"]
    assert response["message"]["text"] == text

def main():
    send_text('pi #1 checking in', '#pi_checkin')
    
if __name__ == "__main__":
    main()

