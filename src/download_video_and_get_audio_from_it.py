from pytube import YouTube, Playlist


def download_youtube_audio(url):
    yt = YouTube(url)
    # audio_streams = yt.streams.filter(only_audio=True, audio_codec="opus").all()
    audio_streams = yt.streams.filter(only_audio=True).all()
    res = audio_streams[0].download()
    print(res)
    for st in yt.streams.filter(only_audio=True).all():
        print(st)


def download_yt_podcast(url):
    pl = Playlist(url)
    print(pl.video_urls())


def main():
    download_youtube_audio("https://www.youtube.com/watch?v=ycPr5-27vSI")
    # download_youtube_audio("https://www.youtube.com/watch?v=rJPVrEg82n0")
    # download_yt_podcast("https://www.youtube.com/watch?v=iG9CE55wbtY&list=PL70DEC2B0568B5469")



if __name__ == '__main__':
    main()
