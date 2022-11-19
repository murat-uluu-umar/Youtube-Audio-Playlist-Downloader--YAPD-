from model import *
from colorama import Fore
from colorama import Style

welcome = f'{Fore.GREEN}Welcome to the Audio Cover Includer!'

track_path = ''
url = ''


if __name__ == '__main__':
    print(welcome)
    print('-'*len(welcome) + '\n'*2)
    print(Style.RESET_ALL, Fore.LIGHTBLUE_EX)  
    url = input('Paste url here: ')
    video = YouTube(url=url)
    track_path = get_path()
    change_cover_image_to_audio(track_path, video.video_id)
    print('Done')
