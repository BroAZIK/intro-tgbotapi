import requests
from config import BASE_URL, TOKEN


def send_local_document(chat_id: str, document: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendDocument"

    payload = {
        'chat_id': chat_id
    }

    response = requests.get(url=url, params=payload, files={"document": document})



# with open('test.jpg', 'rb') as file:
#     document = file

#     send_local_document('1258594598', document)



def send_document(chat_id: str, document: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendDocument"

    payload = {
        'chat_id': chat_id,
        'document': {
            'file_id': document,
            'file_name': 'test.jpg',
            'mime_type': 'image/jpeg',
            
        }
    }

    response = requests.post(url=url, json=payload)

    return response.status_code

# send_local_document('1258594598', 'BQACAgIAAxkBAAIBRGTgfcfz66Ng3w0s6tiv26j6OLXfAAJAMgAC0lAIS7EL7vuCboo3MAQ')
# send_local_document('1258594598', 'AAMCAgADGQEAAgFEZOB9x_Pro2DfDSzq2K_bqPo4td8AAkAyAALSUAhLsQvu-4JuijcBAAdtAAMwBA')
send_local_document('1258594598', 'AAMCAgADGQEAAgFEZOB9x_Pro2DfDSzq2K_bqPo4td8AAkAyAALSUAhLsQvu-4JuijcBAAdtAAMwBA')
