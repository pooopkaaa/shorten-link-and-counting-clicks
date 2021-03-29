from environs import Env
import requests
import pprint

env = Env()
env.read_env()

BITLY_ACCESS_TOKEN = env('BITLY_ACCESS_TOKEN')
REAL_LINK = 'http://google.com'

headers = {'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}'}
payload = {'long_url': f'{REAL_LINK}', }
url = 'https://api-ssl.bitly.com/v4/bitlinks'

response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()

bitlink = response.json()['link']
print(bitlink)