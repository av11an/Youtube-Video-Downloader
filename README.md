# Youtube-Video-Downloader
Tkinter GUI YT Downloader

make sure to pip3 install pytube

if there are errors try replaceing a line in the cypher.py code in the pytube packages

line to replace: 

var_regex = re.compile(r"^\w+\W")

replace line with:

var_regex = re.compile(r"^\$*\w+\W")
