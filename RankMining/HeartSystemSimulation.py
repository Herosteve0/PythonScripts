from tkinter import *
import math

win = Tk()
win.title("RankMining - Health Simulation")
geoX = round(win.winfo_screenwidth() * 0.5)
geoY = round(win.winfo_screenheight() * 0.5)
win.geometry(str(geoX)+'x'+str(geoY))
#win.resizable(False, False)

heartsdisplay = []

def DrawHearts(maxhealth: int, health: float, maxvoidhealth: int, voidhealth: float):
    global heartsdisplay

    heartsdisplay = []

    for i in range(math.ceil((maxhealth+maxvoidhealth)/2)):
        img = PhotoImage(file=f'RankMining/EmptyHeart.png')
        heartsdisplay.append(Label(win, text=str(i), image=img))

    for i in range(len(heartsdisplay)):
        heartsdisplay[i].place(x=150, y=150)#place(x=geoX*0.05+i*13,y=geoY*0.9)
        print(geoX*0.05+i*13, geoY*0.9)

    win.update()

DrawHearts(20, 10, 0, 0)

win.mainloop()