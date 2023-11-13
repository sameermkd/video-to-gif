from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("a.webm")
videoClip.write_gif("a.gif")


# pip install moviepy