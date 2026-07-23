""" 01 Воспроизведение мультимедиа

Создайте два класса:
Класс 1

AudioFileMixin — требует наличие атрибута audio_tracks (список треков).


Метод play_audio() выводит:
Воспроизведение аудио для <НазваниеКласса>:
	<название трека>
	<название трека>

Класс 2

VideoFileMixin — требует наличие атрибута video_files (список видео).


Метод play_video() выводит:
Воспроизведение видео для <НазваниеКласса>:
	<название видео>
	<название видео>

Если нужное поле отсутствует — выбрасывайте AttributeError.
"""


class AudioFileMixin:
    def play_audio(self):
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(f"\t{track}")


class VideoFileMixin:
    def play_video(self):
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for video in self.video_files:
            print(f"\t{video}")


###########################################################################################
class AudioFileMixinExplicit:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError(
                f"{self.__class__.__name__} должен иметь атрибут 'audio_tracks'"
            )
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(f"\t{track}")


class VideoFileMixinExplicit:
    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError(
                f"{self.__class__.__name__} должен иметь атрибут 'video_files'"
            )
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for video in self.video_files:
            print(f"\t{video}")


#############################################################################################
class AudioFileMixinTryExcept:
    def play_audio(self):
        try:
            tracks = self.audio_tracks
        except AttributeError:
            raise AttributeError(
                f"{self.__class__.__name__} должен иметь атрибут 'audio_tracks'"
            )
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in tracks:
            print(f"\t{track}")


class VideoFileMixinTryExcept:
    def play_video(self):
        try:
            videos = self.video_files
        except AttributeError:
            raise AttributeError(
                f"{self.__class__.__name__} должен иметь атрибут 'video_files'"
            )
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for video in videos:
            print(f"\t{video}")


####################################################################################
_MISSING = object()  # уникальный объект-метка, которого точно нигде нет

class AudioFileMixinSentinel:
    def play_audio(self):
        tracks = getattr(self, "audio_tracks", _MISSING)
        if tracks is _MISSING:
            raise AttributeError(
                f"{self.__class__.__name__} должен иметь атрибут 'audio_tracks'"
            )
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in tracks:
            print(f"\t{track}")


class VideoFileMixinSentinel:
    def play_video(self):
        videos = getattr(self, "video_files", _MISSING)
        if videos is _MISSING:
            raise AttributeError(
                f"{self.__class__.__name__} должен иметь атрибут 'video_files'"
            )
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for video in videos:
            print(f"\t{video}")


######################################################################################
class AudioFileMixinInitSubclass:

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "audio_tracks"):
            raise AttributeError(
                f"{cls.__name__} должен иметь атрибут 'audio_tracks'"
            )

    def play_audio(self):
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(f"\t{track}")


class VideoFileMixinInitSubclass:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "video_files"):
            raise AttributeError(
                f"{cls.__name__} должен иметь атрибут 'video_files'"
            )

    def play_video(self):
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for video in self.video_files:
            print(f"\t{video}")

if __name__ == "__main__":

    audio_data = ["track1.mp3", "track2.mp3"]
    video_data = ["video1.mp4", "video2.mp4"]

    variants = [
        ("Вариант 1 (естественный AttributeError)", AudioFileMixin, VideoFileMixin),
        ("Вариант 2 (hasattr)", AudioFileMixinExplicit, VideoFileMixinExplicit),
        ("Вариант 3 (try/except)", AudioFileMixinTryExcept, VideoFileMixinTryExcept),
        ("Вариант 4 (getattr + sentinel)", AudioFileMixinSentinel, VideoFileMixinSentinel),
    ]

    for title, audio_mixin, video_mixin in variants:
        print(f"=== {title} ===")

        class MediaPlayer(audio_mixin, video_mixin):
            def __init__(self, audio_tracks, video_files):
                self.audio_tracks = audio_tracks
                self.video_files = video_files

        player = MediaPlayer(audio_tracks=audio_data, video_files=video_data)
        player.play_audio()
        player.play_video()

        class BrokenPlayer(audio_mixin):
            pass

        try:
            BrokenPlayer().play_audio()
        except AttributeError as e:
            print(f"Ожидаемая ошибка: {e}")

        print()

    print("=== Вариант 5 (__init_subclass__) ===")


    class MediaPlayer5(AudioFileMixinInitSubclass, VideoFileMixinInitSubclass):
        audio_tracks = audio_data
        video_files = video_data

    MediaPlayer5().play_audio()
    MediaPlayer5().play_video()

    try:
        class BrokenPlayer5(AudioFileMixinInitSubclass):
            pass
    except AttributeError as e:
        print(f"Ожидаемая ошибка (при объявлении класса): {e}")

    try:
        class BrokenVideoPlayer5(VideoFileMixinInitSubclass):
            pass
    except AttributeError as e:
        print(f"Ожидаемая ошибка (нет video_files): {e}")
