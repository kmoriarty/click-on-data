#!/usr/bin/env python
from __future__ import print_function
import Tkinter
from PIL import Image, ImageTk
from sys import argv

data = list()
size = 600, 600
workflow_length = 3
workflow_counter = 3
ref_point = 0,0
ref_x_1 = 0
ref_x_2 = 0
ref_size = 0
ref_real_size = 2.5 # real world length of line between reference points

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
    global workflow_length
    global workflow_counter
    global ref_point
    global ref_x_1
    global ref_x_2
    global ref_size
    global ref_real_size
    canvas = event.widget
    x = event.x
    y = event.y
    os = 4
    print("clicked at: ", x, y)
    if workflow_counter == workflow_length:
        ref_point = (x,y)
        workflow_counter -= 1
    elif workflow_counter == workflow_length - 1:
        ref_x_1 = x
        workflow_counter -= 1
    elif workflow_counter == workflow_length - 2:
        ref_x_2 = x
        ref_size = abs(ref_x_2 - ref_x_1)
        ref_size /= ref_real_size
        workflow_counter -= 1
    else:
        x_ = (x - ref_point[0]) / ref_size
        y_ = (y - ref_point[1]) / ref_size
        print("real world coordinates: ", x_, y_)
        data.append([x_, y_])
        canvas.create_oval(x, y, x+os, y+os, width=4, fill="white", outline="white")


if __name__ == '__main__':
    main()
