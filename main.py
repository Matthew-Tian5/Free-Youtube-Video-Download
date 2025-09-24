from pytube import YouTube
from errors import handle_download_error
import os
from tkinter import filedialog
import tkinter as tk
import ssl
import time

def select_download_path():
    root = tk.Tk()
    root.withdraw() 
    folder_selected = filedialog.askdirectory()
    return folder_selected if folder_selected else os.getcwd()

def authenticate_youtube():
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:

            test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            yt = YouTube(
                test_url,
                use_oauth=True,
                allow_oauth_cache=True
            )
            return True
        except Exception as e:
            print(f"Authentication attempt {retry_count + 1} failed. Please try again.")
            retry_count += 1
            time.sleep(2)  
    return False


ssl._create_default_https_context = ssl._create_unverified_context

download_path = select_download_path()
print(f"Downloads will be saved to: {download_path}")


print("Starting YouTube authentication process...")
if not authenticate_youtube():
    print("Failed to authenticate. Please try running the program again.")
    exit(1)

print("Authentication successful! You can now download videos.")

a = ""
while (a != "QUIT"):
    a = input("Enter the YouTube video URL (or 'QUIT' to exit): ")
    try:
        if a != "QUIT":
            yt = YouTube(
                a,
                use_oauth=True,
                allow_oauth_cache=True
            )
            video_stream = yt.streams.get_highest_resolution()
            print(f"Downloading: {yt.title}")
            video_stream.download(output_path=download_path)
            print(f"Download complete! Saved to: {download_path}")

    except Exception as e:
        error_message = handle_download_error(e)
        print(error_message)