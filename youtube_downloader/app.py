from pytube import YouTube
from sys import argv

if len(argv) < 2:
    print("Please provide a YouTube link as a command-line argument.")
    exit()

link = argv[1]
yt = YouTube[link]

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('./storage/shared/bbt')