from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

url = input("Enter the YouTube video link: ")

while True:
    file_type = input("Enter 1 for mp3, 2 for mp4, or 3 for both: ")
    if file_type in ('1', '2', '3'):
        break
    else:
        print("Invalid option. Please try again.")

yt = YouTube(url)
if file_type in ('1', '3'):
    video = yt.streams.filter(only_audio=True).first()
    video.download()
    mp4_file = video.default_filename
    mp3_file = os.path.splitext(mp4_file)[0] + '.mp3'
    audio = AudioFileClip(mp4_file)
    audio.write_audiofile(mp3_file)
    os.remove(mp4_file)

if file_type in ('2', '3'):
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
    video.download()

print("Download completed successfully.")
