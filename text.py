from tkinter import *
from tkinter import filedialog
from tkinter import font
from PIL import ImageTk,Image
from tkinter import colorchooser

root=Tk()

frame=LabelFrame(root,text="")
frame.grid(row=0,column=0)

global s
s=IntVar()
s.set(8)
l=[8,12,16,20,24,28,32,36,40,44]
drop=OptionMenu(frame,s,*l)
drop.grid(row=0,column=7,padx=5)

global f
f=StringVar()
f.set("Helvetica")
l1=["Algerian","Helvetica","Forte","Jokerman"]
drop1=OptionMenu(frame,f,*l1)
drop1.grid(row=0,column=6,padx=5)

text=Text(root,width=200,height=200,font=(f.get(),s.get()))
text.grid(row=1,column=0)


def openf():
    text_file=filedialog.askopenfilename(initialdir="C:",title="select a file to open",filetypes=(("text files","*.txt"),))
    if text_file!='':
        text_file=open(text_file,'r+')
        temp=text_file.read()
        text.insert(END,temp)
        text_file.close()
    else:
        pass

def save():
    text_file=filedialog.askopenfilename(initialdir="C:",title="select a file to save",filetypes=(("text files","*.txt"),))
    if text_file!='':
        text_file=open(text_file,'w+')
        text_file.write(text.get(1.0,END))
    else:
        pass


def bold():
    b=font.Font(text,text.cget("font"))
    b.configure(weight="bold")
    text.tag_configure("bold",font=b)
    current=text.tag_names("sel.first")
    if "bold" in current:
        text.tag_remove("bold","sel.first","sel.last")
    else:
        text.tag_add("bold","sel.first","sel.last")

def italics():
    i=font.Font(text,text.cget("font"))
    i.configure(slant="italic")
    text.tag_configure("italic",font=i)
    current=text.tag_names("sel.first")
    if "italic" in current:
        text.tag_remove("italic","sel.first","sel.last")
    else:
        text.tag_add("italic","sel.first","sel.last")
        
def addimage():
    global img
    img_location=filedialog.askopenfilename(initialdir="tkinter",title="select an image",filetypes=(("jpg files","*.jpg"),))
    if img_location=='':
        pass
    else:
        img=ImageTk.PhotoImage(file=img_location)
        text.image_create(END,image=img)

def addcolor():
    my_color=colorchooser.askcolor()[1]
    text.tag_configure("colored", foreground=my_color)
    current=text.tag_names("sel.first")
    text.tag_add("colored","sel.first","sel.last")

def style():
    selected=f.get()
    siz=s.get()
    sf=font.Font(text,text.cget("font"))
    text.tag_configure("style",font=(selected,siz))
    current=text.tag_names("sel.first")
    text.tag_add("style","sel.first","sel.last")
    


openfile=Button(frame,text="open",command=openf)
openfile.grid(row=0,column=0,padx=5)
save=Button(frame,text="save",command=save)
save.grid(row=0,column=1,padx=5)
bold=Button(frame,text="bold",command=bold)
bold.grid(row=0,column=2,padx=5)
italics=Button(frame,text="italics",command=italics)
italics.grid(row=0,column=3,padx=5)
image=Button(frame,text="image",command=addimage)
image.grid(row=0,column=4,padx=5)
color=Button(frame,text="text color",command=addcolor)
color.grid(row=0,column=5,padx=5)
fstyle=Button(frame,text="Make changes",command=style)
fstyle.grid(row=0,column=8,padx=5)


root.mainloop()





