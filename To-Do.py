from graphics import *
from PIL import Image, ImageDraw, ImageFont
import ctypes


global x
global y
x = 0
y = 70
lst = [0, 70, False, 1]
def drawer(win):
    background = Polygon(Point(0.0,0.0), Point(0.0, 600.0), Point(600.0, 600.0), Point(600.0, 0.0))
    background.setFill("steelblue3")
    background.draw(win)
    bodybackground = Polygon(Point(20.0,70.0), Point(20.0, 600.0), Point(580.0, 600.0), Point(580.0, 70.0))
    bodybackground.setFill("slateGray1")
    bodybackground.setWidth(0)
    bodybackground.draw(win)

    #the add button
    add = Rectangle(Point(200.0, 10.0), Point(400.0,50.0))
    add.draw(win)
    addCircle = Rectangle(Point(203.0, 13.0), Point(240.0, 46.0))
    addCircle.setFill("white")
    addCircle.setOutline("white")
    addCircle.draw(win)
    addCross1 = Line(Point(208.0, 30.0), Point(237.0, 30.0))
    addCross1.setFill("slategray4")
    addCross1.draw(win)
    addCross2 = Line(Point(222.0, 16.0), Point(222.0, 44.0))
    addCross2.setFill("slategray4")
    addCross2.draw(win)
    addTxt = Text(Point(320.0, 30.0), "ADD NEW")
    addTxt.setSize(15)
    addTxt.draw(win)


    close = Rectangle(Point(530.0, 10.0), Point(580.0, 50.0))
    close.draw(win)
    close.setFill("sienna3")

    closeCross1 = Line(Point(535.0, 14.0), Point(575.0, 46.0))
    closeCross1.draw(win)
    closeCross1.setWidth(0.5)
    closeCross2 = Line(Point(535.0, 46.0), Point(575.0, 14.0))
    closeCross2.draw(win)
    closeCross2.setWidth(0.5)

    deleteBtn = Rectangle(Point(415.0, 11.0), Point(522.0, 50.0))
    deleteBtn.setFill("red")
    deleteBtn.draw(win)
    deleteMsg = Text(Point(470.0, 32.0), "DELETE")
    deleteMsg.setFill("white")
    deleteMsg.draw(win)

def Save(newRemList, win, reminder):
    input = reminder.getText()
    for i in range(len(newRemList)):
        newRemList[i].undraw()
    infile = open("reminders.txt", "a")
    infile.write(input)
    infile.write("\n")
    infile.close()
    lst[2] = False

def cancelSave(newRemList, win):
    for i in range(len(newRemList)):
        newRemList[i].undraw()
    lst[2] = False

def newReminder(win, click):
    separator = Line(Point(45.0, 70.0+lst[1]), Point(559, 70.0+lst[1]))
    separator.setWidth(0)
    separator.setFill("silver")
    separator.draw(win)

    #make the text box
    board = Rectangle(Point(45.0, 136.0), Point(559.0, 335.0))
    board.setFill("snow1")
    board.setOutline("snow3")
    board.draw(win)

    lst[2] = True
    message = Text(Point(302.0, 160.0), "New Remider")
    message.setSize(15)
    message.setFill("slategrey")
    message.draw(win)

    reminder = Entry(Point(301.0, 205.0), 50)
    reminder.setTextColor("white")
    reminder.draw(win)


    save = Rectangle(Point(336.0, 250.0), Point(416.0, 277.0))
    save.setOutline("wheat3")
    save.setFill("wheat1")
    save.draw(win)
    cancel = Rectangle(Point(423.0, 250.0), Point(506.0, 277.0))
    cancel.setFill("sienna3")
    cancel.setOutline("sienna4")
    cancel.draw(win)

    saveMessage = Text(Point(377.0, 264.0), "Save")
    saveMessage.setFill("grey")
    saveMessage.draw(win)
    cancelMessage = Text(Point(464.0, 264.0), "Cancel")
    cancelMessage.setFill("white")
    cancelMessage.draw(win)

    newRemList = [board, message, reminder, save, cancel, saveMessage, cancelMessage]
    saveclick = win.getMouse()
    if 416.0>saveclick.getX()>336.0 and 250.0<saveclick.getY()<277.0 and lst[2]:
        Save(newRemList, win, reminder)
    if 423.0<saveclick.getX()<506.0 and 250.0<saveclick.getY()<277.0 and lst[2]:
        cancelSave(newRemList, win)

    lst[1] += 70

def delete(win):
    board = Rectangle(Point(6.0, 10.0), Point(194.0, 51.0))
    board.setFill("white")
    board.draw(win)
    enter = Entry(Point(92.0, 38.0), 10)
    enter.setText("0.0")
    enter.draw(win)
    message = Text(Point(92.0, 18.0), "Enter the Number to delete")
    message.setSize(6)
    message.draw(win)
    sub = Rectangle(Point(140.0, 26.0), Point(170.0, 47.0))
    sub.setFill("red")
    sub.draw(win)

    k = win.getMouse()
    if 140.0< k.getX() <170 and 26< k.getY() <47 and not(lst[2]):

        delNum = eval(enter.getText())

        with open("reminders.txt", "r") as f:
            lines = f.readlines()
        lcv = 0
        with open("reminders.txt", "w") as f:
            for line in lines:
                lcv+=1
                if lcv != delNum:
                    #line.strip("\n")
                    f.write(line)
    stripe = Line(Point(90, 33+(delNum*70)),Point(517, 33+(delNum*70))).draw(win)


def mouseFunctions(win, click):
    if(click.getX() > 200.0 and click.getX()<400 and click.getY()>10 and click.getY()<50):
        newReminder(win, click)
    if(click.getX() > 530.0 and click.getX()<580 and click.getY()>10 and click.getY()<50):
        picFile = open("reminders.txt", "r")

        img = Image.new('RGB', (200, 200), color=(30, 30, 30))

        d = ImageDraw.Draw(img)
        lcv2 = 0
        d.text((500, 270 + lcv2), "Today's to do list", fill=(255, 255, 255))
        for line in picFile.readlines():
            d.text((30, 20 + lcv2), line, fill=(170,170,170))
            lcv2 += 10
        img.save('bg.bmp')
        img.save('bg.png')

        backGround = Image.open("code21.jpg")
        addOn = Image.open("bg.bmp")

        area = (100, 100, 300, 300)
        backGround.paste(addOn, area)

        backGround.save('back.bmp')
        backGround.save('back.png')

        win.close()
    if(415.0<click.getX()<522.0 and 11.0<click.getY()<50.0 and not(lst[2])):
        delete(win)
    if 140.0< click.getX() <170 and 26< click.getY() <47 and not(lst[2]):
        delete(win)

def main():
    win = GraphWin("Your To-Do List", 600, 600)
    drawer(win)
    infile = open("reminders.txt", "r")

    while True:
        for line in infile.readlines():
            rem = Text(Point(313.0, 118.0+lst[0]), line)
            rem.setSize(20)
            rem.draw(win)
            numbering = Text(Point(70.0, 118.0 + lst[0]), lst[3])
            numbering.setSize(20)
            numbering.draw(win)
            lst[0]+=70
            separator = Line(Point(45.0, 70.0 + lst[1]), Point(559, 70.0 + lst[1]))
            separator.setWidth(0)
            separator.setFill("silver")
            separator.draw(win)
            lst[1]+=70
            lst[3] += 1
        click = win.getMouse()
        if click:
            mouseFunctions(win, click)
main()