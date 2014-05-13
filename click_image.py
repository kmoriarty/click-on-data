#!/usr/bin/env python
from __future__ import print_function
import Tkinter
from PIL import Image, ImageTk
from sys import argv
import math

ref_real_size = 2.5 #real world length of line between reference points (2nd and 3rd point)

data = list()
size = 1500, 1500
workflow_length = 3
workflow_counter = 3
data_counter = 0
ref_point = 0,0
ref_x_1 = 0
ref_x_2 = 0
ref_size = 0

def main():
    global ref_real_size
    window = Tkinter.Tk(className="Data Point Recorder")
    if len(argv) < 3:
        print_usage()
        exit()
    image = Image.open(argv[1])
    ref_real_size = float(argv[2])
    image.thumbnail(size, Image.ANTIALIAS)
    canvas = Tkinter.Canvas(window, width=image.size[0], height=image.size[1],
                            cursor="crosshair")
    canvas.pack()
    image_tk = ImageTk.PhotoImage(image)
    canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)
    canvas.bind("<Button-1>", callback)
    Tkinter.mainloop()
    with open( argv[2] if len(argv) >=3 else 'output.csv', 'w') as f:
        for d in data:
            print(str(d[0])+","+str(d[1]), file=f)

def callback(event):
    global workflow_length
    global workflow_counter
    global ref_point
    global ref_x_1
    global ref_x_2
    global ref_y_1
    global ref_y_2
    global ref_size
    global ref_real_size
    global data_counter
    canvas = event.widget
    x = event.x
    y = event.y
    os = 4
    print("clicked at: ", x, y)
    if workflow_counter == workflow_length:
        ref_point = (x,y)
        workflow_counter -= 1
        canvas.create_oval(x-(os/2), y-(os/2), x-(os/2), y-(os/2), width=4, fill="red", outline="red")
    elif workflow_counter == workflow_length - 1:
        ref_x_1 = x
        ref_y_1 = y
        workflow_counter -= 1
    elif workflow_counter == workflow_length - 2:
        ref_x_2 = x
        ref_y_2 = y
        ref_size = float(math.sqrt(pow(ref_x_2 - ref_x_1,2) + pow(ref_y_2 - ref_y_1,2)))
        print(ref_size)
        ref_size /= ref_real_size
        print(ref_size)
        workflow_counter -= 1
    else:
        x_ = (x - ref_point[0]) / ref_size
        y_ = (y - ref_point[1]) / ref_size
        print("[",data_counter,"] real world coordinates: ", x_, y_)
        data_counter += 1
        data.append([x_, y_])
        canvas.create_oval(x-(os/2), y-(os/2), x-(os/2), y-(os/2), width=4, fill="white", outline="white")

def print_usage():
    print("Usage: ", argv[0], "input_image.png scale_line_size [output.csv]")
    print("Example: ./click_image.py points.png 5.0")
    print("Data is written to output file on window close.")
    print("First point clicked is origin and will be marked red.")
    print("Second two points clicked define scale. Note: this only works in x direction!")
    print("All the rest of the points will be marked white and pushed into a matrix that is exported in csv format")
    print("Please add the scale line size, e.g. 2.5[cm] to predetermine the length of the scale line")


if __name__ == '__main__':
    main()
