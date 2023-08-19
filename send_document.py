import requests
from config import BASE_URL, TOKEN


def send_local_document(chat_id: str, document: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendDocument"

    payload = {
        'chat_id': chat_id
    }

    response = requests.get(url=url, params=payload, files={"document": document})



with open('test.jpg', 'rb') as file:
    document = file

    send_local_document('1258594598', document)

