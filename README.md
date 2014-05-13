click-on-data
=============

Quick &amp; Dirty Script written in python to record x,y values of data points by clicking them on an image


Usage:

run click_image.py, it will print the usage. 

Say you have recorded a bunch of data points, and you've done so on grid paper, or have a scaled line on the image.
The scaled line should be along the X direction. This image is saved as your_image_file.png and your scale line had a length of 1. 

Run:

    ./click_image.py your_image_file.png 1.0 data.csv

Then:
- First: click on a point you want to be the origin. It will be marked with a red point.
- Click on the start of your scale line.
- Click on the end of your scale line. The scale line will be marked blue.
- Click on your data points. You can verify how many you've clicked on in the terminal output.
- When you're done, close the window. On closing the window the data will be written to your data.csv file. 
