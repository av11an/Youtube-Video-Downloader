from tkinter import END
import pytube
import tkinter as tk
from pytube import YouTube
import os


# pytube commands
def ytd(link, save_path):
    youtube = pytube.YouTube(link)
    video = youtube.streams.get_highest_resolution()
    try:
        video.download(save_path)
    except:
        print("Error")




def clearText(text1, text2):
    text1.delete(0, END)
    text2.delete(0, END)


def toDesktop():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    text = desktop
    save_entry.insert(0, text)


# Init tk
app = tk.Tk()
app.title("Youtube Video Downloader")
app.geometry("500x200")
app.resizable(False, False)

# Init Strings
link_var = tk.StringVar()
save_var = tk.StringVar()

# Labels and Entries
link_label = tk.Label(app, text="Youtube URL: ")
link_label.pack()

link_entry = tk.Entry(app, textvariable=link_var)
link_entry.pack()

save_label = tk.Label(app, text="Copy and Paste File path ?:/ : ")
save_label.pack()

save_entry = tk.Entry(app, textvariable=save_var)
save_entry.pack()

savetoDesktop = tk.Button(app, text="To Desktop", bd="5", command=toDesktop)
savetoDesktop.place(x=210, y=100)

downloadBtn = tk.Button(app, text="Download", bd="5",
                        command=lambda: [ytd(link_var.get(), save_var.get()), clearText(link_entry, save_entry)])
downloadBtn.place(x=210, y=140)

if __name__ == '__main__':
    app.mainloop()
