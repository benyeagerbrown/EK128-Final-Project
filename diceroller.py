from tkinter import *
import random
from tkinter import ttk

#make window for number of dice

def quit():
    root.destroy()
    

root = Tk()
root.title("Dice Roller")

mainframe = ttk.Frame(root, padding="50 10 50 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

dice = StringVar()
dice_entry = ttk.Entry(mainframe, width=7, textvariable=dice).grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Number of Dice:").grid(column=1, row=1, sticky=E)
ttk.Button(mainframe, text="Roll", command=quit).grid(column=3, row=1, sticky=W)

root.bind('<Return>', quit)

root.mainloop()

N=int(dice.get())

master = Tk()  #Initiates window
master.title("Dice Roller")  #Titles window


def draw_canvas(N):
    ###Draws a canvas to fit the number of dice###
    if N <=20:
        w = Canvas(master, width=75*N+25, height=300)
    elif N >20 and N%20 != 0: #When there are more than 20, the width is set and the height changes
        w = Canvas(master, width=1525, height=300*((N//20)+1))
    elif N >20 and N%20 == 0: #When there are exact multiples of 20, the height does not adjust
        w = Canvas(master, width=1525, height=300*((N//20)))
    w.pack()
    return w

def dimensions(N):
    ###Finds dimensions for the window to fit N dice (For use later)###
    if N <=20:
        width=75*N + 25
        height=300
    elif N >20 and N%20 !=0:
        width = 1525
        height = 300*(N//20+1)
    elif N >20 and N%20 ==0:
        width=1525
        height= 300*(N//20)
    return width, height

def draw_die(n, start_x=25, start_y=120):
    ###Draws a die showing n dots###
    w.create_rectangle(start_x, start_y, start_x+50, start_y+50, fill="white")
    if n ==1: #One dot in the center
        w.create_oval(start_x+25,start_y+25,start_x+25,start_y+25,fill="black", width=10.0)
    elif n == 2: #Two dots, one in each corner
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
    elif n == 3: #Two dots, one in each corner, and one in center
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
        w.create_oval(start_x+25,start_y+25,start_x+25,start_y+25,fill="black", width=10.0)
    elif n == 4: #One dot in each corner
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
        w.create_oval(start_x+12.5, start_y+37.5, start_x+12.5, start_y+37.5, fill="black", width=10.0)
        w.create_oval(start_x+37.5, start_y+12.5, start_x+37.5, start_y+12.5, fill="black", width=10.0)
    elif n == 5: #One dot in each corner, and one dot in the center
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
        w.create_oval(start_x+12.5, start_y+37.5, start_x+12.5, start_y+37.5, fill="black", width=10.0)
        w.create_oval(start_x+37.5, start_y+12.5, start_x+37.5, start_y+12.5, fill="black", width=10.0)
        w.create_oval(start_x+25,start_y+25,start_x+25,start_y+25,fill="black", width=10.0)
    elif n == 6: #Three dots in vertical lines on each side
        w.create_oval(start_x+12.5, start_y+12.5,start_x+12.5,start_y+12.5,fill="black",width=10.0)
        w.create_oval(start_x+37.5, start_y+37.5,start_x+37.5,start_y+37.5,fill="black",width=10.0)
        w.create_oval(start_x+12.5, start_y+37.5, start_x+12.5, start_y+37.5, fill="black", width=10.0)
        w.create_oval(start_x+37.5, start_y+12.5, start_x+37.5, start_y+12.5, fill="black", width=10.0)
        w.create_oval(start_x+12.5, start_y+25, start_x+12.5, start_y+25, fill="black", width=10.0)
        w.create_oval(start_x+37.5, start_y+25, start_x+37.5, start_y+25, fill="black", width=10.0)

def draw_dice(N):
    ###Draws N dice###
    for dice in  range(N):  #For each die, pick a random integer from 1 to 6, then move the x-coordinate by 75
        if dice%20 > 0 or dice==0: #Starts new row of dice and ensures that dice are in line vertically
            start_x=25+((dice%20)*75)
        elif dice%20==0 and dice !=0: 
            start_x=25
        if dice <20: #Moves dice down when a new row needs to be started
            start_y=120
        elif dice >= 20 :
            start_y= 120 + 195*(dice//20)
        draw_die(random.randint(1,6), start_x=start_x, start_y=start_y)

w= draw_canvas(N) #Create the canvas of necessary size
width, height = dimensions(N) #Retrieve the dimensions
draw_dice(N) #Draw the dice

reroll_button=ttk.Button(w, text = "Reroll", command=lambda: draw_dice(N)) #Create a button that rolls again
button_window = w.create_window(width//2, 3*height//4 + 2*height/15, anchor=S, window=reroll_button) #Create a "window" on the canvas






mainloop()

