#pip install youtube_dl

import os
import youtube_dl

url = "https://www.youtube.com/watch?v=sF_I5HETAfQ"

folder_path = "videoYT"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

options = {
    "format": "best[ext=mp4]",
    "outtmpl": "%(title)s.%(ext)s",
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])
