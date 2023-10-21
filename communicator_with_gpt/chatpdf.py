import requests

files = [
    ('file', ('file', open('10_otchet.pdf', 'rb'), 'application/octet-stream'))
]
headers = {
    'x-api-key': 'sec_b2QaUVq1eb7SNfKrkg45VDVpWkciFhTN'
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)

headers = {
    'x-api-key': 'sec_b2QaUVq1eb7SNfKrkg45VDVpWkciFhTN',
    "Content-Type": "application/json",
}

data = {
    'sourceId': response.json()['sourceId'],
    'messages': [
        {
            'role': "user",
            'content': "О чём этот документ?",
        }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)
