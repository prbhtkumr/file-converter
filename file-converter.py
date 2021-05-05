import os

ffmpeg = "ffmpeg\\bin\\"

dest_source = input("Destination of source file: ")

os.system(f"cd {dest_source}")

files = os.listdir(dest_source)

dest_conv = input("Destination of converted file: ")

try:
	os.system(f"mkdir {dest_conv}")
except:
	pass

file_format = input((dest_conv+"> Format to you want the file converted: "))

if "mp3" in file_format:
	for file in files:
		os.system(f'ffmpeg -i \"{dest_source}/{file}\" \"{dest_conv}/{file.split(".")[0]}.{file_format}\"')
else:
	for file in files:
		os.system(f'ffmpeg -i \"{dest_source}/{file}\" -vcodec copy -acodec copy \"{dest_conv}/{file.split(".")[0]}.{file_format}\"')

