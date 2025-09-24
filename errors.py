from pytube.exceptions import *

def handle_download_error(error):
    """Handle different types of YouTube download errors"""
    if isinstance(error, VideoUnavailable):
        return "This video is unavailable."
    elif isinstance(error, RegexMatchError):
        return "Invalid YouTube URL."
    elif isinstance(error, VideoPrivate):
        return "This video is private."
    elif isinstance(error, LiveStreamError):
        return "Cannot download live streams."
    else:
        return f"An unexpected error occurred: {str(error)}"