#use pip install pytube on your console to get the pytube package
#importing pytube

import pytube
from pytube import YouTube
#defining the dialogue box where you input the url.
url=input('Enter video URL')

#defining the path where the download is stored
path= 'F:'

#the one line code that executes the download
pytube.YouTube(url).streams.get_highest_resolution().download(path)
