from pathlib import Path

class Utils:
    def get_directories() -> list:
        return [d.name for d in Path('/mnt/media/music').iterdir() if d.is_dir()]