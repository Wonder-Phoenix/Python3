#pip install imageio
#pip install imageio imageio-ffmpeg
import imageio

from moviepy.config import change_settings
change_settings({"FFMPEG_BINARY": "/usr/bin/ffmpeg"})

reader = imageio.get_reader("ma_video.mp4")

meta = reader.get_meta_data()
duration = meta["duration"]
fps = meta["fps"]

imageio.mimsave("mon_gif.gif", reader, fps=fps)
