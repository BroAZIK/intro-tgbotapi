import requests
import time
from pprint import pprint


BASE_URL = 'https://api.telegram.org/bot'
TOKEN    = "6602447524:AAFuq2qNvn61P7j5ocEdDxoRn0jw8TVAO4Y"


def getMe() -> dict:
    '''getting info about the bot'''
    url = f"{BASE_URL}{TOKEN}/getMe"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return False


def getUpdates() -> dict:
    '''getting info about the bot'''
    url = f"{BASE_URL}{TOKEN}/getUpdates"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result'] 
    
    return False


def sendMessage(chat_id: str, text: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': f"*{text}*",
        'parse_mode': "MarkdownV2"
    }

    response = requests.get(url=url, params=payload)

    return response.status_code


def sendPhoto(chat_id: str, file_id: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendPhoto"

    payload = {
        'chat_id': chat_id,
        'photo': file_id,
        'parse_mode': "HTML",
        'caption': "<b>This is a photo you have sent.</b>"
    }

    response = requests.get(url=url, params=payload)

    return response.status_code


def send_keyboard(chat_id, text, keyboard):
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': keyboard
    }

    response = requests.get(url=url, json=payload)

    return response.status_code

def echo():
    update_id = 0

    while True:
        time.sleep(0.5)

        # print(f'updates: {update_id}')
        updates = getUpdates()
        if updates[-1]['update_id'] == update_id:
            continue
        else:
            last_update = updates[-1]
            
            message = last_update['message']
            # pprint(message)
            print("-"*50)

            chat_id = message['chat']['id']

            if 'text' in message.keys():
                text = message['text']
                if text == '/start':
                    text = "Hello, I am a bot."
                    keyboard = {
                        'keyboard': [
                            ['Home', 'About'],
                            ['Contact', 'Location']
                        ],
                    }
                    send_keyboard(chat_id, text, keyboard)
                else:
                    sendMessage(chat_id, text)
            
            elif 'photo' in message.keys():
                file_id = message['photo'][-1]['file_id']
                sendPhoto(chat_id, file_id)

            update_id = updates[-1]['update_id']

echo()
