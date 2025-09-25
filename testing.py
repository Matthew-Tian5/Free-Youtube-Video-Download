from pytube import YouTube
import ssl
import time

def authenticate_and_download(url):
    try:
        # Configure SSL context
        ssl._create_default_https_context = ssl._create_unverified_context
        
        # Initialize YouTube object with authentication
        yt = YouTube(
            url,
            use_oauth=True,
            allow_oauth_cache=True,
            on_progress_callback=lambda stream, chunk, bytes_remaining: print(f"Downloading... {(1-bytes_remaining/stream.filesize)*100:.1f}%")
        )
        
        # Get highest resolution stream
        print("Fetching available streams...")
        video_stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f"Starting download: {yt.title}")
        video_stream.download()
        print("Download complete!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        if "HTTP Error 400" in str(e):
            print("\nTroubleshooting tips:")
            print("1. Make sure you've completed the OAuth authentication")
            print("2. Try updating pytube: pip install --upgrade pytube")
            print("3. Verify the video URL is correct and accessible")

# Test video URL
video_url = 'https://www.youtube.com/watch?v=BHTxzn4YL6o'

# Attempt download with retry logic
max_retries = 3
for attempt in range(max_retries):
    try:
        print(f"\nAttempt {attempt + 1} of {max_retries}")
        authenticate_and_download(video_url)
        break
    except Exception as e:
        if attempt < max_retries - 1:
            print(f"Retrying in 2 seconds...")
            time.sleep(2)
        else:
            print("Max retries reached. Please try again later.")