from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        stream_res_720 = streams.get_by_resolution('720p')
        stream_res_720.download(output_path=save_path)
        print("Success!")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')
    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    video_url = input('Please, enter a YouTube url: ')
    save_dir = open_file_dialog()

    if save_dir:
        print('Started download...')
        download_video(video_url, save_dir)

    else:
        print('The directory is not exist')
        