import yt_dlp
from urllib.parse import urlparse

from pytube import YouTube


class AudioScrap:
    def __init__(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'cachedir': True,
            'quiet': True,
            'nocheckcertificate': True,
            'noplaylist': True,
            'extract_flat': 'in_playlist',
            'skip_download': True,
        }
        self.tool = yt_dlp.YoutubeDL(ydl_opts)
    def convert_shorts_url(self,url):
        """
        Convert a YouTube Shorts URL to a standard YouTube URL format.
        """
        parsed_url = urlparse(url)
        if 'shorts' in parsed_url.path:
            video_id = parsed_url.path.split('/')[-1]
            return f"https://www.youtube.com/watch?v={video_id}"
        return url
    def stream_audio(self,youtube_url):
        # Convert Shorts URL to standard URL if needed
        youtube_url = self.convert_shorts_url(youtube_url)
        with self.tool as ydl:
            info_dict = ydl.extract_info(youtube_url, False)
            audio_url = info_dict['url']
        return audio_url
        # def get_audio_url(self, youtube_url):
            # Convert Shorts URL to standard URL if needed
        # youtube_url = self.convert_shorts_url(youtube_url)
        # yt = YouTube(youtube_url)
        # audio_stream = yt.streams.filter(only_audio=True).first()
        # return audio_stream.url



# Example usage
# youtube_url = 'https://youtu.be/4dsFQFCvVGU?si=AudWDTlwmfEN48Mx'
# AudioScrap.stream_audio(youtube_url)
