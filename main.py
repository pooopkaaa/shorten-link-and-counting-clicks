import requests
import pprint
from urllib.parse import urlparse
from environs import Env


def shorten_link(token, link):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': f'{link}', }
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_cliks(token, link):
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    amount_cliks = response.json()['total_clicks']
    return amount_cliks


def is_short_link(link):
    if urlparse(link).scheme:
        return False
    else:
        return True


def main():
    env = Env()
    env.read_env()
    token = env('BITLY_ACCESS_TOKEN')

    link = input('Введите ссылку: ')

    if is_short_link(link):
        try:
            amount_cliks = count_cliks(token, link)
            print(f'По вашей ссылке прошли: {amount_cliks} раз(а)')
        except requests.exceptions.HTTPError as error:
            exit("Неверный bitlink. Ошибка: {0}".format(error))
    else:
        try:
            bitlink = shorten_link(token, link)
            print(f'Битлинк: {bitlink}')
        except requests.exceptions.HTTPError as error:
            exit("Неверная ссылка. Ошибка: {0}".format(error))


if __name__ == '__main__':
    main()
