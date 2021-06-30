from booking import MackayParser, ChghParser


if __name__ == '__main__':

    mackay_parser = MackayParser()
    is_mackay_full = mackay_parser.is_full()
    if is_mackay_full:
        print('mackay is full ... have to wait ...')
    else:
        text = f'mackay maybe open! go to {mackay_parser.url} for details'
        print(text)

    chgh_parser = ChghParser()
    is_chgh_full = chgh_parser.is_full()
    if is_chgh_full:
        print('chgh is full ... have to wait ...')
    else:
        text = f'chgh maybe open! go to {chgh_parser.url} for details'
        print(text)
