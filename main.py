import os

import requests

from booking import MackayParser, ChghParser


def read_env(var):
    res = os.getenv(var)
    if res is None:
        raise Exception(f'Cannot get {var} from env')
    else:
        print(f'{var}: {res}')
        return res


def get_line_token():
    return read_env('VACCINE_LINE_TOKEN')


def send_message(msg):
    headers = {'Authorization': 'Bearer ' + get_line_token()}
    payload = {'message': msg}
    r = requests.post('https://notify-api.line.me/api/notify', headers=headers, params=payload)
    return r.status_code


if __name__ == '__main__':

    mackay_parser = MackayParser()
    is_mackay_full = mackay_parser.is_full()
    if is_mackay_full:
        print('mackay is full ... have to wait ...')
    else:
        text = f'mackay maybe open! go to {mackay_parser.url} for details'
        print(text)
        send_message(text)

    chgh_parser = ChghParser()
    is_chgh_full = chgh_parser.is_full()
    if is_chgh_full:
        print('chgh is full ... have to wait ...')
    else:
        text = f'chgh maybe open! go to {chgh_parser.url} for details'
        print(text)
        send_message(text)
