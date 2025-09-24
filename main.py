from pytube import YouTube
from errors import handle_download_error
import os
from tkinter import filedialog
import tkinter as tk
import ssl

def download_path():
    root = tk.Tk()
    root.withdraw() 
    folder_selected = filedialog.askdirectory()
    return folder_selected if folder_path else os.getcwd()

a = ""
ssl._create_default_https_context = ssl._create_unverified_context

while (a !="QUIT"):
    a = input("Enter the YouTube video URL: ")
    try:
        if(a!="QUIT"):
            
            yt = YouTube(
                a,
                use_oauth=True,
                allow_oauth_cache=True
            )

            video_stream = yt.streams.get_highest_resolution()
            print(f"Downloading: {yt.title}")
            video_stream.download()
            print("Download complete!")

    except Exception as e:
        error_message = handle_download_error(e)
        print(error_message)