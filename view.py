from colorama import Fore
from colorama import Style

def warning():
    print(f'Paste {Fore.BLUE}url{Style.RESET_ALL} of {Fore.RED}video{Style.RESET_ALL} or {Fore.RED}playlist{Style.RESET_ALL} to download audio.\nYou able to {Fore.CYAN}{Style.DIM}change download directory{Style.RESET_ALL}, just input {Fore.BLUE}cdir{Style.RESET_ALL} instead url.\nAlso you can use {Fore.BLUE}exit{Style.RESET_ALL} command.\nInput {Fore.BLUE}show_dir{Style.RESET_ALL} to get download directory.\n')

def user_interface():
    usr_input = input(f'url or command: ')
    print(Fore.LIGHTGREEN_EX,end='')
    return usr_input

def submittion(size):
    #print(f'Do you want to download {size / 1000000} Mb? Y/n')
    pass
