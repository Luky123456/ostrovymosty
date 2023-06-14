import random
import tkinter as tk

win = tk.Tk()

randX = random.randrange(4,7)
randY = random.randrange(3,10)
widthVar = 500
heightVar = 500
pictureWidth = 50
pictureHeight = 50
status = False
gold = 0

canvas= tk.Canvas(width = randX * pictureWidth + 100, height = randY * pictureHeight, background="gray")
canvas.pack()

water = []
islands = []

imageIsland = tk.PhotoImage(file = "obrazky/ostrov0.png")
imageIsland2 = tk.PhotoImage(file = "obrazky/ostrov3.png")
imageMostHor = tk.PhotoImage(file = "obrazky/ostrov1.png")
imageMostVer = tk.PhotoImage(file = "obrazky/ostrov2.png")
imageKruhBlue = tk.PhotoImage(file = "obrazky/ostrov_kruh0.png")
imageKruhOrange = tk.PhotoImage(file = "obrazky/ostrov_kruh1.png")

def setUp():
    global water, islands
    for y in range(randY):
        for x in range(randX):
            resultIsland = random.randrange(0,101)
            if resultIsland <= 20:
                islands.append(canvas.create_image(pictureWidth*x,pictureHeight*y, anchor = 'nw', image = imageIsland))
                
            else:
                water.append(canvas.create_image(pictureWidth*x,pictureHeight*y, anchor = 'nw', image = imageIsland2))
    canvas.create_image(randX*pictureWidth+25, 0, anchor = "nw", tags = "kruh", image = imageKruhBlue)

def changer(e):
    global water, gold
    print(gold)
    print("klikol som")
    zoz = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if (len(zoz)!=0 and zoz[0] in water):
        print("klikol si a bola to voda")
        newX = (e.x//pictureWidth)*pictureWidth
        newY = (e.y//pictureHeight)*pictureHeight
        temp = zoz[0]
        canvas.delete(temp)
        water.remove(temp)
        if status == False:
            canvas.create_image(newX, newY, anchor="nw", image = imageMostHor, tag = "bridge")
            gold += 10
        else:
            gold += 50
            canvas.create_image(newX, newY, anchor="nw", image = imageIsland, tag = "bridge")
    canvas.delete("pocet")
    canvas.create_text(randX*pictureWidth+10,25, text = gold, fill = "black", tag = "pocet")
    
def spinner(e):
    zoz = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    canvas.itemcget(zoz[0],"image")
    print(canvas.itemcget(zoz[0],"image"))
    if canvas.itemcget(zoz[0],"image") == "pyimage3":
        canvas.itemconfig(zoz[0],image=imageMostVer)   
    else:
        canvas.itemconfig(zoz[0],image=imageMostHor)

def fieldStatus(e):
    global status
    zoz = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    canvas.itemcget(zoz[0],"image")
    print(canvas.itemcget(zoz[0],"image"))
    print(status)
    if canvas.itemcget(zoz[0],"image") == "pyimage5":
        status = True
        canvas.itemconfig(zoz[0],image=imageKruhOrange)
    else:
        status = False
        canvas.itemconfig(zoz[0],image=imageKruhBlue)
        
setUp()

canvas.bind("<Button-1>", changer)
canvas.tag_bind("bridge","<Button-1>", spinner)
canvas.tag_bind("kruh","<Button-1>", fieldStatus)

win.mainloop()

