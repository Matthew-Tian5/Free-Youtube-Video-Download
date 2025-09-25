import yt_dlp
import os
import platform
from tkinter import filedialog
import tkinter as tk

def select_download_path():
    root = tk.Tk()
    root.withdraw()

    initial_dir = os.path.expanduser("~/Downloads")  
    folder_selected = filedialog.askdirectory(initialdir=initial_dir)
    return folder_selected if folder_selected else os.getcwd()

def download_progress_hook(d):
    if d['status'] == 'downloading':
        if 'total_bytes' in d:
            progress = (d['downloaded_bytes'] / d['total_bytes']) * 100
          
            print(f"\033[K\rDownloading... {progress:.1f}%", end='', flush=True)
    elif d['status'] == 'finished':
        print("\nDownload complete!")

def download_video(url, download_path):
  
    output_template = os.path.join(download_path, '%(title)s.%(ext)s').replace('\\', '/')
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_template,
        'progress_hooks': [download_progress_hook],
        'quiet': False,
        'no_warnings': False,
       
        'windowsfilenames': platform.system() == 'Windows'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Starting download...")
            ydl.download([url])
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


download_path = select_download_path()
print(f"Downloads will be saved to: {download_path}")


os.system('cls' if platform.system() == 'Windows' else 'clear')

print("YouTube Video Downloader")
print("-" * 20)


url = ""
while (url != "QUIT"):
    url = input("Enter the YouTube video URL (or 'QUIT' to exit): ")
    if url != "QUIT":
        download_video(url, download_path)