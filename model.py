from moviepy.editor import *
from pytube import YouTube
from pytube import Playlist
from mutagen.mp3 import MP3
from tkinter import filedialog
from mutagen.id3 import ID3, APIC, error
from io import BytesIO

import os
import string
import pickle
import tkinter
import requests

download_path = ''

def on_complete(stream, file_path):
    print(f'path: {file_path}')
    print(f'size: {stream.filesize * 0.000001} Mb')

def download_audio_from_url(url):
    video = YouTube(url=url, on_complete_callback=on_complete)
    path = video.streams.get_audio_only().download(download_path)
    print(path)
    add_cover_image_to_audio(path, video.video_id)

def download_audio_from_video(video):
    path = video.streams.get_audio_only().download(download_path)
    add_cover_image_to_audio(path, video.video_id)

def get_video_thumbnail(id):
    url = f'http://img.youtube.com/vi/{id}/0.jpg'
    response = requests.get(url)
    img = BytesIO(response.content).read()
    return img

def change_format(path : string):
    new_path = path.replace('mp4','mp3')
    video = AudioFileClip(path)
    video.write_audiofile(new_path)
    video.close()
    os.remove(path)
    return new_path

def add_cover_image_to_audio(video_path, id):
    path = change_format(video_path)
    audio = MP3(path, ID3=ID3)
    try:
        audio.add_tags()
    except error:
        print(error)
    audio.tags.add(APIC(mime='image/jpeg',type=3,desc=u'Cover',data=get_video_thumbnail(id)))
    audio.save()

def change_cover_image_to_audio(path, id):
    audio = MP3(path, ID3=ID3)
    try:
        audio.add_tags()
    except error:
        print(error)
    audio.tags.add(APIC(mime='image/jpeg',type=3,desc=u'Cover',data=get_video_thumbnail(id)))
    audio.save()

def download_playlist(url):
    playlist = Playlist(url)
    print(playlist.videos)
    for video in playlist.videos:
        download_audio_from_video(video)

def choose_download_dir():
    root = tkinter.Tk()
    root.withdraw()
    global download_path 
    download_path = filedialog.askdirectory()
    save_download_dir()

def get_path():
    root = tkinter.Tk()
    root.withdraw() 
    path = filedialog.askopenfilename()
    return path

def save_download_dir():
    with open("path.bin", "wb") as f:
        pickle.dump(download_path, f)

def load_download_dir():
    if os.path.isfile('path.bin'):
        global download_path
        with open("path.bin", "rb") as f:
            download_path = pickle.load(f)
    else:
        print("You didn't choose download directory")
        choose_download_dir()

def get_video_download_size(url):
    return YouTube(url=url).streams.get_audio_only().filesize

def get_playlist_download_size(url):
    playlist = Playlist(url=url)
    playlist_size = 0
    for video in playlist.videos:
        playlist_size += video.streams.get_audio_only().filesize
    return playlist_size
