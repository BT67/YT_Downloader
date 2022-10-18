#ytdownloader.py
#Created by JGallo 2022/10/18
#Download youtube videos
from pytube import YouTube
import argparse, os

parser = argparse.ArgumentParser(description='Download YouTube videos')
parser.add_argument('-i', '--input', help='Video URL')
parser.add_argument('-r', '--res', help='Download Resolution: 144,240,260,480,720,1080(default)')
args = parser.parse_args()

if(args.input == None):
    parser.print_help(file=None)
else:
    url = YouTube(str(args.input))
    if(args.res == None):
        video = url.streams.filter(res='1080p').first()
    elif(args.res != None):
        video = url.streams.filter(res=str(args.res)+'p').first()

    if(video == None):
        print('No suitable download stream found')
        sys.exit()
    elif(video != None):
        video.download()
