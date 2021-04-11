import requests
from urllib.parse import urlparse
from environs import Env
import argparse


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
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{netloc}/{path}/clicks/summary'\
        .format(
            netloc=parsed_link.netloc,
            path=parsed_link.path)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_amount = response.json()['total_clicks']
    return clicks_amount


def is_short_link(token, link):
    parsed_link = urlparse(link)
    headers = {'Authorization': f'Bearer {token}'}
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{netloc}/{path}'\
        .format(
            netloc=parsed_link.netloc,
            path=parsed_link.path)
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    env = Env()
    env.read_env()
    token = env('BITLY_ACCESS_TOKEN')

    parser = argparse.ArgumentParser(description='Скрипт для обрезки ссылки и\
                                    подсчета переходов по ней с помощью\
                                    [bit.ly](https://bit.ly/).')
    parser.add_argument('link', help='Предоставте ссылку для ее обработки,\
                        например http://google.com')
    args = parser.parse_args()
    link = args.link
    if is_short_link(token, link):
        try:
            clicks_amount = count_clicks(token, link)
            print(f'По вашей ссылке прошли: {clicks_amount} раз(а)')
        except requests.exceptions.HTTPError as error:
            exit('Неверный bitlink. Ошибка: {0}'.format(error))
    else:
        try:
            bitlink = shorten_link(token, link)
            print(f'Битлинк: {bitlink}')
        except requests.exceptions.HTTPError as error:
            exit('Неверная ссылка. Ошибка: {0}'.format(error))


if __name__ == '__main__':
    main()
