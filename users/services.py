import os

import requests
from dotenv import load_dotenv

load_dotenv()


class MyBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = os.getenv('TELEGRAM_TOKEN')

    def send_message(self, text):
        CHAT_ID = os.getenv('CHAT_ID')

        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': CHAT_ID,
                'text': text
            }
        )
