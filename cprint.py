from sys import argv
from random import randint
from time import sleep


ANSI_RESET = '\u001b[00m'


class fg:
    def rgb(red, green, blue):
        return f'\r\u001b[38;2;{red};{green};{blue}m'
    def rgbl(rgb: list):
        return f'\u001b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m'


class bg:
    def rgb(red, green, blue):
        return f'\r\u001b[48;2;{red};{green};{blue}m'
    def rgbl(rgb: list):
        return f'\u001b[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m'


def ansiprint(string, ansi_escape_code: int):
    global ANSI_RESET
    print(f'\u001b[{ansi_escape_code}m' + string + ANSI_RESET)


def rgbprint(string=None, isbg: bool = False, rgb: list = [0, 0, 0], random: bool = False, delay: float = 0.1, end=''):
    global ANSI_RESET
    if random:
        if string is None:
            while True:
                rgb = [randint(0, 255), randint(0, 255), randint(0, 255)]
                if isbg:
                    print(f'\r{bg.rgbl(rgb)}' + f'{rgb[0]}, {rgb[1]}, {rgb[2]}     ' + ANSI_RESET, end=end)
                else:
                    print(f'\r{fg.rgbl(rgb)}' + f'{rgb[0]}, {rgb[1]}, {rgb[2]}     ' + ANSI_RESET, end=end)
                sleep(delay)
        else:
            rgb = [randint(0, 255), randint(0, 255), randint(0, 255)]
            if isbg:
                print(f'\r{bg.rgbl(rgb)}' + f'{string}' + ANSI_RESET, end=end)
            else:
                print(f'\r{fg.rgbl(rgb)}' + f'{string}' + ANSI_RESET, end=end)
    else:
        if isbg:
            print(f'\r{bg.rgbl(rgb)}' + f'{string}' + ANSI_RESET, end=end)
        else:
            # print(f'{string=}')
            print(f'\r{fg.rgbl(rgb)}' + f'{string}' + ANSI_RESET, end=end)


def main():
    if len(argv) == 1:
        rgbprint(random=True)
    elif len(argv) == 2:
        rgbprint(string=argv[1], random=True)
    else:
        end = ''
        strings = argv[2:]
        rgb = argv[1].split(' ')
        argv2lst = list(argv[2])
        if list('end=') == argv2lst[:4]:
            end = ''.join(argv2lst[4:])
            strings = argv[3:]
        for string in strings:
            rgbprint(string=string, rgb=rgb, end=end, random=False)

if __name__ == '__main__':
    main() 


