from pytube import YouTube
from errors import handle_download_error
import os
from tkinter import filedialog
import tkinter as tk

a = ""

while (a !="QUIT"):

    a = input("Enter the YouTube video URL: ")
    try:

        yt = YouTube(a)

        video_stream = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}")
        video_stream.download()
        print("Download complete!")

    except Exception as e:
        error_message = handle_download_error(e)
        print(error_message)