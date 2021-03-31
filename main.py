from environs import Env
import requests
import pprint

env = Env()
env.read_env()


def shorten_link(token, real_link):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': f'{real_link}', }
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    pprint.pprint(response.json())
    bitlink = response.json()['link']
    return bitlink


def main():
    token = env('BITLY_ACCESS_TOKEN')
    real_link = input('Введите ссылку для сокращения: ')
    
    try:
        bitlink = shorten_link(token, real_link)
        print(bitlink)
    except requests.exceptions.HTTPError as error:
        exit("Неверная ссылка. Ошибка: {0}".format(error))

if __name__ == '__main__':
    main()
