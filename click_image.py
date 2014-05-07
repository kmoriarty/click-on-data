#!/usr/bin/env python
from __future__ import print_function
import Tkinter
from PIL import Image, ImageTk
from sys import argv

data = list()
size = 600, 600

def main():
    window = Tkinter.Tk(className="bla")
    #argv[1] if len(argv) >=2 else 
    image = Image.open(argv[1] if len(argv) >=2 else "bla2.png")
    image.thumbnail(size, Image.ANTIALIAS)
    canvas = Tkinter.Canvas(window, width=image.size[0], height=image.size[1],
                            cursor="crosshair")
    canvas.pack()
    image_tk = ImageTk.PhotoImage(image)
    canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)
    canvas.bind("<Button-1>", callback)
    Tkinter.mainloop()
    with open('somefile.txt', 'a') as f:
        for d in data:
            print(str(d[0])+","+str(d[1]), file=f)

def callback(event):
    canvas = event.widget
    x = event.x
    y = event.y
    os = 4
    print("clicked at: ", x, y)
    data.append([x, y])
    canvas.create_oval(x, y, x+os, y+os, width=4, fill="white", outline="white")


if __name__ == '__main__':
    main()
