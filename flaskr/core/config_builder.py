from pathlib import Path


class ConfigBuilder:
    def __init__(self):
        # defaults for yt-dlp CLI
        self.options = {
            'extract_flat': 'discard_in_playlist',
            'fragment_retries': 10,
            'ignoreerrors': 'only_download',
            'noplaylist': True,
            'postprocessors': [{'key': 'FFmpegExtractAudio',
                     'nopostoverwrites': False,
                     'preferredcodec': 'best',
                     'preferredquality': '5'},
                    {'key': 'FFmpegConcat',
                     'only_multi_video': True,
                     'when': 'playlist'}],
            'retries': 10,
            'warn_when_outdated': True
        }

    # TODO: Not finished, complete as needed
    def set_format(self, audio_only: bool, format: str = None):
        if audio_only:
            self.options["format"] = "m4a/bestaudio/best"
        else:
            self.options["format"] = format
    def set_path(self, path: str):
        self.options['paths'] = {
            'home': path
        }
    def get_options(self):
        return self.options
