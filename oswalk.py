from tkinter import *
from tkinter.simpledialog import askstring
from datetime import date
from PIL import Image
from PIL import ImageTk
import os, os.path
import tkinter.messagebox
import fnmatch

root = Tk()
root.title("OSWalkpy v1.0")
root.geometry("510x440")
root.resizable(0,0)

labelframe = LabelFrame(root)
labelframe.config(width=30, borderwidth=0, highlightthickness=0, padx=20, pady=5)
labelframe.grid(row=1, column=0)
labelframe2 = LabelFrame(root)
labelframe2.config(width=30, borderwidth=0, highlightthickness=0, padx=20, pady=5)
labelframe2.grid(row=5, column=0)
labelframe3 = LabelFrame(root)
labelframe3.config(width=30, borderwidth=0, highlightthickness=0, padx=20, pady=5)
labelframe3.grid(row=4, column=0)
text = Text(root)
dirtext = Text(labelframe)
text.config(fg="white", width=25, height=1)
dirtext.grid(column=1, row=1)
dirtext.config(width=20, height=1)
lblfilenum = Label(labelframe3, text="Files: ",  font=("Helvetica", 10))
lblfilenum.config()
lblfilenum.grid(column=0, row=3)
lblfilecount = Label(labelframe3, text="",  font=("Helvetica", 10))
lblfilecount.config(fg="green")
lblfilecount.grid(column=1, row=3)
titlelabel = Label(root, text="File names and Directory Tree", font=("Helvetica", 15))
titlelabel.config(fg="green")
titlelabel.grid(column=0, row=0)
dirname = Label(labelframe, text="Commands: ")
dirname.grid(column=0, row=1, sticky=W)

width = 30
height = 30
img = Image.open("icon.png")
img = img.resize((width,height), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

clearImg = Image.open("clear.png")
clearImg = clearImg.resize((width,height), Image.ANTIALIAS)
photoC = ImageTk.PhotoImage(clearImg)

def About():
    top = Toplevel()
    top.title("About")
    top.geometry("350x460")
    root.resizable(0,0)
    
    today = date.today()
    d1 = today.strftime("%m/%d/%Y")

    img = PhotoImage(file="python.png")
    lblimage = Label(top, image=img)
    lblimage.grid(column=1, row=6)

    lbltitle = Label(top, text="OSWalkpy\n", font=("Helvetica", 17, "bold"))
    lbltitle.config(padx=5, pady=10)
    lbltitle.grid(column=1, row=0)

    lblauthor = Label(top, text="Author: ", font=("Helvetica", 11))
    lblauthor.config(pady=10)
    lblauthor.grid(column=0, row=1)   

    lblauthor = Label(top, text="c0d3ninja", font=("Helvetica", 11))
    lblauthor.config(pady=10)
    lblauthor.grid(column=1, row=1)   

    lblversion2 = Label(top, text="Version: ", font=("Helvetica", 11))
    lblversion2.config(pady=10)
    lblversion2.grid(column=0, row=2) 

    lblversion2 = Label(top, text="1.0", font=("Helvetica", 11))
    lblversion2.config(pady=10)
    lblversion2.grid(column=1, row=2) 

    lbldiscord= Label(top, text="Discord: ", font=("Helvetica", 11))
    lbldiscord.config(pady=10)
    lbldiscord.grid(column=0, row=3)   

    lbldiscord2 = Label(top, text="http://discord.gg/NBy2atu", font=("Helvetica", 11))
    lbldiscord2.config(pady=10)
    lbldiscord2.grid(column=1, row=3) 

    lblgithub = Label(top, text="Github: ", font=("Helvetica", 11))
    lblgithub.config(pady=10)
    lblgithub.grid(column=0, row=4)   

    lblgithub2 = Label(top, text="https://github.com/gotr00t0day", font=("Helvetica", 11))
    lblgithub2.config(pady=10)
    lblgithub2.grid(column=1, row=4) 

    lbldate = Label(top, text="Date: ", font=("Helvetica", 11))
    lbldate.config(pady=10)
    lbldate.grid(column=0, row=5)   

    lbldate2 = Label(top, text=d1, font=("Helvetica", 11))
    lbldate2.config()
    lbldate2.grid(column=1, row=5) 

    top.mainloop()

text.insert(END, "\t\t\tCOMMANDS")
text.insert(END, "\n")
text.insert(END, "\n")
text.insert(END, "\t.help: \t\t(Get a list of all commands.)\n\n")
text.insert(END, "\t.all: \t\t(A directory tree for all files.)\n\n")
text.insert(END, "\t.filesearch: \t\t(Search for a file)\n\n")
text.insert(END, "\t.ext: \t\t(Search for files with *.ext)\n\n")
text.insert(END, "\t.delext \t\t(Deletes all .extension files)\n\n")

def commands():
    text.insert(END, "\t\t\tCOMMANDS")
    text.insert(END, "\n")
    text.insert(END, "\n")
    text.insert(END, "\t.help: \t\t(Get a list of all commands.)\n\n")
    text.insert(END, "\t.all: \t\t(A directory tree for all files.)\n\n")
    text.insert(END, "\t.filesearch: \t\t(Search for a file)\n\n")
    text.insert(END, "\t.ext: \t\t(Search for files with *.ext)\n\n")
    text.insert(END, "\t.delext \t\t(Deletes all .extension files)\n\n")

def allfiles():
    text.delete("1.0", END)
    lblfilecount.config(text="")
    directory = askstring("Search", "Directory name")
    file_count = tkinter.StringVar()
    file_count = sum(len(files) for _, _, files in os.walk(directory))
    lblfilecount.config(text=file_count)
    for dirName, subdirList, fileList in os.walk(directory):
        text.insert(END, "\n")
        text.insert(END, 'DIR: {}'.format(dirName))
        text.insert(END, "\n")
        for fname in fileList:
            text.insert(END, '\t┗━━━━━━\t{}'.format(fname))
            text.insert(END, "\n")

def removefiles():
    text.delete("1.0", END)
    lblfilecount.config(text="")
    filextension = askstring("REMOVE FILES", "File Extension")
    indir = askstring("REMOVE FILES", "Directory Name")
    for root, dirs, files in os.walk(indir):
        for file in files:
            if file.endswith(filextension):
                os.remove(os.path.join(root, file)) 


def find():
    text.delete("1.0", END)
    lblfilecount.config(text="")
    filen = askstring("file search", "File name")
    indir = askstring("file search", "Directory name")
    fileList = []
    for dName, sdName, fList in os.walk(indir):
        for fileName in fList:
            if fnmatch.fnmatch(fileName, filen):
                fileList.append(os.path.join(dName, fileName))
                text.insert(END, "[DIR]: {}".format(dName))
                text.insert(END, "\n")
                text.insert(END, '\t┗━━━━━━\t{}'.format(fileName))
                text.insert(END, "\n")

def extension(): 
    text.delete("1.0", END)
    lblfilecount.config(text="")
    directory = askstring(".txt", "Directory Name")
    extension =askstring("*.ext", "Extension")
    file_count = tkinter.StringVar()
    file_count.set(sum(len(files) for _, _, files in os.walk(directory)))
    lblfilecount.config(textvariable=file_count)
    for dirpath, dirnames, files in os.walk(directory, topdown=True):
        text.insert(END, "\n")        
        text.insert(END, "[DIR]: {}".format(dirpath))
        text.insert(END, "\n")    
        for filename in files:
            if filename.endswith(extension):            
                text.insert(END, '\t┗━━━━━━\t{}'.format(filename))
                text.insert(END, "\n")

def clear():
    lblfilecount.config(text="")
    text.delete("1.0", END)

def search():
    text.delete("1.0", END)
    lblfilecount.config(text="")
    if dirtext.get("1.0", 'end-1c') == ".help":
        commands()
    if dirtext.get("1.0", 'end-1c') == ".ext":
        extension()
    elif dirtext.get("1.0", 'end-1c') == ".filesearch":
        find()
    elif dirtext.get("1.0", 'end-1c') == ".delext":
        removefiles()
    elif dirtext.get("1.0", 'end-1c') == ".all":
        allfiles()
    else:
        pass

search = Button(labelframe2, text="Search", fg="white", bg="black", image=photo, height=30, width=50, command=search)
search.grid(row=4, column=0, padx=5)

clear = Button(labelframe2, text="Clear", fg="white", bg="black", image=photoC, height=30, width=50, command=clear)
clear.grid(row=4, column=1, padx=5)


scrollbar = Scrollbar(root)
scrollbar.grid(row=2, column=1, sticky="ns")
text.config(width=60, height=15, bg="black")
text.grid(row=2, pady=10, sticky=W)
scrollbar.config(bg="black", command=text.yview)
text.config(yscrollcommand=scrollbar.set)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About", command=About)
menubar.add_cascade(label="Help", menu=aboutmenu)

root.config(menu=menubar)

root.mainloop()
