import os
import subprocess

from pytube import Playlist, YouTube

def run(pl):
    # get linked list of links in the playlist
    links = pl.video_urls

    # download each item in the list
    for l in links:
       # url input from user
        yt = YouTube(l)

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # download the file
        out_file = video.download(output_path='C:\\Users\\Dell\\Desktop\\mmm\\')

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print(yt.title + " has been successfully downloaded.")

if __name__ == "__main__":
    url = 'https://www.youtube.com/playlist?list=PLVdrvbY9AVQrd4M9f9_5FVkfV_yHY8ALz'
    pl = Playlist(url)
    run(pl)