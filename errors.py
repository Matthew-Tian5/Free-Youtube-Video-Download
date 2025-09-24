class blankinputError(Exception):
    """Cannot be blank input. Please enter a valid YouTube URL."""
    pass

class invalidURLerror(Exception):
    """Invalid YouTube URL. Please enter a valid YouTube URL to download the video."""
    pass