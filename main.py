from environs import Env
import requests
import pprint

env = Env()
env.read_env()

BITLY_ACCESS_TOKEN = env('BITLY_ACCESS_TOKEN')

headers = {'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}'}
url = 'https://api-ssl.bitly.com/v4/user'

response = requests.get(url, headers=headers)
response.raise_for_status()
pprint.pprint(response.json())
