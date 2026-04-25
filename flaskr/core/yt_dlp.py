import yt_dlp

def download_youtube(url, ydl_opts: dict[str, str]):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
