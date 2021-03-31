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
    bitlink = response.json()['id']
    return bitlink


def count_cliks(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    amount_cliks = response.json()['total_clicks']
    return amount_cliks


def main():
    token = env('BITLY_ACCESS_TOKEN')
    real_link = input('Введите ссылку для сокращения: ')

    try:
        bitlink = shorten_link(token, real_link)
        print(bitlink)
    except requests.exceptions.HTTPError as error:
        exit("Неверная ссылка. Ошибка: {0}".format(error))

    try:
        amount_cliks = count_cliks(token, bitlink)
        print(amount_cliks)
    except requests.exceptions.HTTPError as error:
        exit("Неверный bitlink. Ошибка: {0}".format(error))

if __name__ == '__main__':
    main()
