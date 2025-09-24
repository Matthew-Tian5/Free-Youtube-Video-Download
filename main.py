from pytube import YouTube


a = input("Enter the YouTube video URL: ")
try:

    yt = YouTube(a)


    video_stream = yt.streams.get_highest_resolution()

    print(f"Downloading: {yt.title}")
    video_stream.download()
    print("Download complete!")

except Exception as e:
    print(f"An error occurred: {e}")