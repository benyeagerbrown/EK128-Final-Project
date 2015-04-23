from tkinter import *
import random



master = Tk()
master.title("Dice roller")

def draw_canvas(N):
    ###Draws a canvas to fit the number of dice###
    w = Canvas(master, width=75*N+25, height=300)
    w.pack()
    return w

def draw_die(n, start_x=25, start_y=120):
    ###Draws a die showing n dots###
    w.create_rectangle(start_x, start_y, start_x+50, start_y+50, fill="white")
    if n ==1: #One dot in the center
        w.create_oval(start_x+25,start_y+25,start_x+25,start_y+25,fill="black", width=10.0)
    if n == 2: #Two dots, one in each corner
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
    if n == 3: #Two dots, one in each corner, and one in center
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
        w.create_oval(start_x+25,start_y+25,start_x+25,start_y+25,fill="black", width=10.0)
    if n == 4: #One dot in each corner
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
        w.create_oval(start_x+12.5, start_y+37.5, start_x+12.5, start_y+37.5, fill="black", width=10.0)
        w.create_oval(start_x+37.5, start_y+12.5, start_x+37.5, start_y+12.5, fill="black", width=10.0)
    if n == 5: #One dot in each corner, and one dot in the center
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
        w.create_oval(start_x+12.5, start_y+37.5, start_x+12.5, start_y+37.5, fill="black", width=10.0)
        w.create_oval(start_x+37.5, start_y+12.5, start_x+37.5, start_y+12.5, fill="black", width=10.0)
        w.create_oval(start_x+25,start_y+25,start_x+25,start_y+25,fill="black", width=10.0)
    if n == 6: #Three dots in vertical lines on each side
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
        w.create_oval(start_x+12.5, start_y+37.5, start_x+12.5, start_y+37.5, fill="black", width=10.0)
        w.create_oval(start_x+37.5, start_y+12.5, start_x+37.5, start_y+12.5, fill="black", width=10.0)
        w.create_oval(start_x+12.5, start_y+25, start_x+12.5, start_y+25, fill="black", width=10.0)
        w.create_oval(start_x+37.5, start_y+25, start_x+37.5, start_y+25, fill="black", width=10.0)

def draw_dice(N):
    ###Draws N dice###
    for dice in  range(N):
       draw_die(random.randint(1,6),start_x=25+dice*75)
w=draw_canvas(30)
draw_dice(30)
mainloop()
