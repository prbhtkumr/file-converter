import os

files = os.listdir()

dest = input("Destination of converted file: ")

file_format = input((dest+"> Format to you want the file converted: ")

for file in range(len(files)):
	os.system(f"ffmpeg -i {file} -vcodec copy -acodec copy {dest}/{file.split('.')[0]}.{file_format}") 

