# ytdownloader.py
# Created by JGallo 2022/10/18
# Download YouTube videos
import sys
from pytube import YouTube
import argparse

parser = argparse.ArgumentParser(description='Download YouTube videos')
parser.add_argument('-i', '--input', help='Video URL, wrapped in quotes \"\"')
parser.add_argument('-r', '--res', help='Download Resolution: 144,240,260,480,720,1080(default)')
args = parser.parse_args()

if args.input is None:
    parser.print_help(file=None)
else:
    url = YouTube(str(args.input))
    video = None
    if args.res is None:
        video = url.streams.filter(res='720p').first()
    elif args.res is not None:
        video = url.streams.filter(res=str(args.res) + 'p').first()

    if video is None:
        print('No suitable download stream found')
        sys.exit()
    elif video is not None:
        video.download()
