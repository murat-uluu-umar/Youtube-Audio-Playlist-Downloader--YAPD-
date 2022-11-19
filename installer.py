import os

libs = ['moviepy','pytube','mutagen','tk','requests','colorama']
command = 'python -m pip install '
if __name__ == '__main__':
    for x in libs:
        os.system(command + x)