import requests
from config import BASE_URL, TOKEN

from nested_list import K1

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

keyboard = {
    'keyboard': K1,
}

send_keyboard('1258594598', 'Hello', keyboard)
