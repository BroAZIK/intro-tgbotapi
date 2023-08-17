import requests
import time


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
        'text': text
    }

    response = requests.get(url=url, params=payload)

    return response.status_code


def echo():
    update_id = 0

    while True:
        time.sleep(0.5)

        print(f'updates: {update_id}')
        updates = getUpdates()
        if updates[-1]['update_id'] == update_id:
            continue
        else:
            last_update = updates[-1]
            
            chat_id = last_update['message']['chat']['id']
            text = last_update['message']['text']

            sendMessage(chat_id, text)
            print(f"send msg to {chat_id} ({text})")

            update_id = updates[-1]['update_id']


echo()
