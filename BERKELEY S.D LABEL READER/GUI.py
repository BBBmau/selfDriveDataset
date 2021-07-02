## BERKELEY S.D LABEL READER ##

from tkinter import *
from PIL import ImageTk, Image
import labels_string

window = Tk()
window.title('Label Creater')
window.geometry('1580x730')
global index
index = 0
def CurSelet(ext):
    index= labelList.index(labelList.curselection())
    points = labels_string.box2d_Points(index)
    canvas.create_rectangle(points, outline="yellow", width=3)
    

"creates the framing of scrollbar"
frame1 = Frame(window, width = 100, highlightbackground='yellow', highlightthicknes=3)
frame1.grid(row=0,column=0,padx=10,pady=20,ipadx=20,ipady=20)

"creates the framing of image being chosen"
imageFrame = Frame(window, highlightbackground='blue', highlightthicknes = 3)
imageFrame.grid(row=0, column=1)

"Canvas for image being analyzed"
canvas = Canvas(imageFrame, width = 1280, height = 720)
canvas.grid(row=0, column=0)
imageAn = Image.open("roadImage.jpg")
imageAn = imageAn.resize((1280,720), Image.ANTIALIAS)
imageLabel = ImageTk.PhotoImage(imageAn)
canvas.create_image(0,0, anchor=NW, image= imageLabel)

#points = int(list(labels_string.data['labels']['box2d'].values())[int(0)])
#points = list(labels_string.data['labels'][6]['box2d'].values())


"creates label for title"
title = Label(frame1, text="Labels in Image", fg='blue', font='Helvetica 18 bold')
title.grid(row=0,column=0,padx=10,pady=10)

"create the scroll bar"
labelScroll = Scrollbar(frame1)
labelScroll.grid(row = 1, column = 1,sticky='ns')

"creating the list that contains the label scroll bar"
labelList = Listbox(frame1, yscrollcommand = labelScroll.set, selectmode="single")
labelList.bind('<<ListboxSelect>>',CurSelet)

for labels in labels_string.data['labels']:
    labelList.insert(END,labels['category'])
#labelScroll.config(command = labelList.yview)
labelList.grid(row = 1, column =0, ipadx=20, pady=0)

window.mainloop()
