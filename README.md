# Обрезка ссылок с помощью [bit.ly](https://bit.ly/)

Скрипт для обрезки ссылки и подсчета переходов по ней с помощью [bit.ly](https://bit.ly/).

## Установка

- Для работы скрипта у вас должен быть установлен [Python3](https://www.python.org/downloads/).
- Скачайте код.
- Рекомендуется использовать [virtualenv/env](https://docs.python.org/3/library/venv.html) для изоляции проекта.
- Установите зависимости для работы скрипта.

```bash
pip install -r requirements.txt
```

- Создайте файл `.env`, который содержит токен доступа к [bit.ly](https://bit.ly/). Для получения токена воспользуйтесь документацией [dev.bitly.com](https://dev.bitly.com/).

```
BITLY_ACCESS_TOKEN=
```

## Пример работы

- Введите ссылку, чтобы ее обрезать.

```bash
python main.py https://google.com
Битлинк: bit.ly/3m128Hi
```

- Введите обрезанную ссылку, чтобы получить количество переходов по ней.

```bash
python main.py bit.ly/3m128Hi
По вашей ссылке прошли: 2 раз(а)
```
