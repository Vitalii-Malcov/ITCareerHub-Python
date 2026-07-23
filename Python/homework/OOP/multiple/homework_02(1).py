""" 02 Устройства

Создайте два класса:
MediaPlayer — поддерживает только аудио. Принимает список треков.
Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
Проверьте работу классов, вызвав методы воспроизведения.

!!! Не забудьте проверить наличие атрибутов в КАЖДОМ объекте

Здесь собраны 5 вариантов того, как можно организовать __init__
у MediaPlayer / Laptop поверх миксинов из homework_01.py.
"""

from homework_01 import AudioFileMixin, VideoFileMixin
from dataclasses import dataclass
from typing import List

class MediaPlayer_v1(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


class Laptop_v1(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = audio_tracks
        self.video_files = video_files


# =====================================================================================
class MediaPlayer_v2(AudioFileMixin):
    def __init__(self, audio_tracks, *args, **kwargs):
        self.audio_tracks = audio_tracks
        super().__init__(*args, **kwargs)  # уходит дальше по MRO (к object)


class Laptop_v2(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files, *args, **kwargs):
        self.audio_tracks = audio_tracks
        self.video_files = video_files
        super().__init__(*args, **kwargs)


# =====================================================================================
@dataclass
class MediaPlayer_v3(AudioFileMixin):
    audio_tracks: List[str]


@dataclass
class Laptop_v3(AudioFileMixin, VideoFileMixin):
    audio_tracks: List[str]
    video_files: List[str]


# =====================================================================================
class MediaPlayer_v4(AudioFileMixin):
    def __init__(self, audio_tracks=None):
        self.audio_tracks = audio_tracks or []


class Laptop_v4(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks=None, video_files=None):
        self.audio_tracks = audio_tracks or []
        self.video_files = video_files or []


# =====================================================================================
class Device:
    """Базовый класс: принимает произвольные именованные атрибуты и назначает их объекту."""
    def __init__(self, **attrs):
        for name, value in attrs.items():
            setattr(self, name, value)


class MediaPlayer_v5(Device, AudioFileMixin):
    def __init__(self, audio_tracks):
        super().__init__(audio_tracks=audio_tracks)


class Laptop_v5(Device, AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        super().__init__(audio_tracks=audio_tracks, video_files=video_files)



if __name__ == "__main__":

    audio_data = ["Песня 1", "Песня 2"]
    video_data = ["Видео X", "Видео Y"]

    variants = [
        ("Вариант 1 (явный __init__)", MediaPlayer_v1, Laptop_v1),
        ("Вариант 2 (super().__init__)", MediaPlayer_v2, Laptop_v2),
        ("Вариант 3 (dataclass)", MediaPlayer_v3, Laptop_v3),
        ("Вариант 4 (значения по умолчанию)", MediaPlayer_v4, Laptop_v4),
        ("Вариант 5 (базовый класс Device)", MediaPlayer_v5, Laptop_v5),
    ]

    for title, MediaPlayerCls, LaptopCls in variants:
        print(f"=== {title} ===")

        player = MediaPlayerCls(audio_data)
        laptop = LaptopCls(audio_data, video_data)

        player.play_audio()

        # !!! проверка наличия атрибута video_files у MediaPlayer
        try:
            player.play_video()
        except AttributeError as e:
            print(f'{e.__class__.__name__}: {e}')

        print()
        laptop.play_audio()
        laptop.play_video()
        print()
