import os
import shutil
from pytube import Playlist, YouTube

def run(pl):
    links = pl.video_urls

    for index, l in enumerate(links):
        yt = YouTube(l)

        try:
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path='C:\\Users\\Dell\\Desktop\\mmm\\')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            try:
                shutil.move(out_file, new_file)
                print(f'[{index+1}/{len(links)}] {yt.title} has been successfully downloaded and converted.')
            except Exception as e:
                print(f"An error occurred while overwriting {new_file}: {e}")

        except:
            print(f'[{index}/{len(links)}] Can not download {yt.title}.')


if __name__ == "__main__":
    url = 'https://www.youtube.com/playlist?list=PLagYdGDvVgEIpp16f01N40UKCBzhGln1-'
    pl = Playlist(url)
    run(pl)
