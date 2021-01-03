import os

files = os.listdir()

dest_source = input("Destination of source file: ")

os.system(f"cd {dest_source}")

dest_conv = input("Destination of converted file: ")

file_format = input((dest_conv+"> Format to you want the file converted: ")

for file in range(len(files)):
	os.system(f"ffmpeg -i {file} -vcodec copy -acodec copy {dest}/{file.split('.')[0]}.{file_format}") 

