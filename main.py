import requests
from urllib.parse import urlparse
from environs import Env


def shorten_link(token, link):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': link, }
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, link):
    parsed_link = urlparse(link)
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc + parsed_link.path}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_amount = response.json()['total_clicks']
    return clicks_amount


def is_short_link(token, link):
    parsed_link = urlparse(link)
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc + parsed_link.path}'
    r = requests.get(url, headers=headers)
    if r.ok:
        return True
    else:
        return False


def main():
    env = Env()
    env.read_env()
    token = env('BITLY_ACCESS_TOKEN')

    link = input('Введите ссылку: ')
    if is_short_link(token, link):
        try:
            clicks_amount = count_clicks(token, link)
            print(f'По вашей ссылке прошли: {clicks_amount} раз(а)')
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
