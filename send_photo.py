import requests
from config import BASE_URL, TOKEN


def send_local_photo(chat_id: str, photo: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendPhoto"

    payload = {
        'chat_id': chat_id
    }
    

    response = requests.get(url=url, params=payload, files={"photo": photo})

    return response.status_code


with open('test.jpg', 'rb') as file:
    photo = file.read()


def send_photo(chat_id: str, photo: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendPhoto"

    payload = {
        'chat_id': chat_id,
        'photo': photo
    }
    

    response = requests.get(url=url, params=payload)

    return response.status_code


send_photo('1258594598', 'AgACAgIAAxkBAAIBJmTd70sSVzhL-6tuYakLS_7gH_z2AAJ-zDEbh1XwSqWqN8eyhtEtAQADAgADeQADMAQ')

