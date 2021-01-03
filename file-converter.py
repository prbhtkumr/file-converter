import os

files = os.listdir()

file_format = input("Format to you want the file converted: ")

for file in range(len(files)):
	os.system(f"ffmpeg -i {file} -vcodec copy -acodec copy {file.split('.')[0]}.{file_format}") 
