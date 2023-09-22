from importlib.resources import path
import pytube
from tkinter import *
import os

def main(path):
    
    def apply():
        url = url_entry.get()
        print(url)
        if not os.path.exists("youtube video"):
            os.makedirs("youtube video")
        if url !='':
            pytube.YouTube(url).streams.get_highest_resolution().download(path)
            url_entry.delete(0,END)
            url_entry.insert(0,"Succesfully downloaded")
        else:
            url_entry.delete(0,END)
            url_entry.insert(0,"Insert one valid url")
         
    window = Tk()
    window.title("Youtube Downloader")
    window.geometry("480x240")
    
    label_sep = Label(window,text="",font=("Cambria",12),bg="#CD0000",justify=RIGHT)
    label_sep.grid(row=1)
    
    label_text = Label(window,text="URL of the video", font=("Cambria",12),fg="White",bg="#CD0000",justify=RIGHT)
    label_text.grid(row=2,column=1)
    
    url_entry = Entry(window, font=("Cambria",12),bg="#CD0000",fg="White",justify=RIGHT,width=25)
    url_entry.grid(row=2,column=2)
    
    button = Button(window,text="Confirm",font=("Cambria",12),fg="White",bg="#CD0000",command=apply)
    button.grid(row=2,column=3)
        
    window.mainloop()

path = input("Your path :")
main(path)
    
