# ytdownloader.py
# Created by JGallo 2022/10/18
# Download YouTube videos
import time

from pytube import YouTube
import argparse
from moviepy.editor import *


def mp4_to_mp3(title):
    videoclip = VideoFileClip(os.getcwd() + '\\{0}.mp4'.format(title.replace('/', '')))
    audioclip = videoclip.audio
    audioclip.write_audiofile(os.getcwd() + '\\out\\mp3\\{0}.mp3'.format(title.replace('/', '')))
    audioclip.close()
    videoclip.close()


parser = argparse.ArgumentParser(description='Download YouTube videos')
parser.add_argument('-i', '--input', help='Video URL, wrapped in quotes \"\"')
parser.add_argument('-r', '--res', help='Download Resolution: 144,240,260,480,720,1080(default)')
args = parser.parse_args()

if args.input is None:
    parser.print_help(file=None)
else:
    if args.res is None:
        res = '720p'
    else:
        res = str(args.res) + 'p'
    if str(args.input)[-4:] == '.txt':
        file = open(str(args.input), "r")
        links = file.readlines()
        file.close()
        video = None
        for link in links:
            try:
                video = YouTube(link).streams.filter(res=res).first()
                video.download()
                print('successfully downloaded {0}'.format(link))
            except Exception as e:
                print('No suitable download stream found for {0}'.format(link))
                print(e)
            try:
                time.sleep(2)
                mp4_to_mp3(video.title)
            except Exception as e:
                print('could not get mp3 from source {0}'.format(link))
                print(e)

    else:
        try:
            video = YouTube(str(args.input)).streams.filter(res=res).first()
            video.download()
            print('successfully downloaded {0}'.format(str(args.input)))
        except Exception as e:
            print('No suitable download stream found for {0}'.format(str(args.input)))
            print(e)
