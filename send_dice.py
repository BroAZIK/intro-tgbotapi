import requests
from config import BASE_URL, TOKEN


def send_dice(chat_id, emoji):
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendDice"

    payload = {
        'chat_id': chat_id,
        'emoji': emoji
    }

    response = requests.get(url=url, params=payload)

    return response.status_code


send_dice('1258594598', '🏀')

