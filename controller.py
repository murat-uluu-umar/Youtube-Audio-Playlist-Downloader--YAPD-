from logging import error
import model
import view
import os

def render():
    model.load_download_dir()
    os.system('cls')
    view.warning()
    controll()

def controll():
    action = view.user_interface()
    try:
        if 'cdir' in action:
            model.choose_download_dir()
            render()
        elif 'show_dir' in action:
            print(model.download_path)
            input()
            render()
        elif 'exit' in action:
            exit()
        elif 'playlist' in action:
            model.download_playlist(action)
        else:
            model.download_audio_from_url(action)
        render()
    except:
        print(f'There is no command like {action}! Or it was incorrectly wrote. Try again.')
        input()
        render()
