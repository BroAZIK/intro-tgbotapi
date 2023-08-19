import requests
from config import BASE_URL, TOKEN


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


K1 = [
    [
        {
            "text": "Location",
            "request_location": True
        }, 
        {
            "text": "Contact",
            "request_contact": True
        }
    ],
    [
        "ok"
    ]
]

keyboard = {
    'keyboard': K1,
    'resize_keyboard': True,
}

send_keyboard('1258594598', 'Hello', keyboard)
