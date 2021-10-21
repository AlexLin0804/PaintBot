from tkinter import *
from link_move import*
from PaintFunction import*
import math

root=Tk()
root.title('Paint Bot')
root.geometry("1020x820")
root.config(bg="maroon")

# Label Angle
LabelAngle1 = 90
LabelAngle2 = 90
LabelAngle3 = 90

# Paint Frame
paint_frame = Canvas(root, width=800, height=800)
paint_frame.grid(row=0, column=1, padx=2.5, pady=5)

# Control frame
control_frame = Frame(root, width=200, height=800)
control_frame.grid(row=0, column=0, padx=5, pady=5,sticky="nsew")
control_frame.pack_propagate(False)

# Axis 1 Buttons in Control frame
Axis1Label = Label(control_frame, text = "Axis 1",font='Helvetica 18 bold')

Axis1AngleLabel = Label(control_frame, text = LabelAngle1)
Axis1clockwise = Button(control_frame, text="CW - X",width=17, command=lambda: PaintBot.Axis1Clockwise(Axis1AngleLabel))
Axis1Counterclockwise = Button(control_frame, text="CCW - Z", width=17,command=lambda: PaintBot.Axis1Counter_clockwise(Axis1AngleLabel))

Axis1clockwise.pack(side=BOTTOM,pady=5)
Axis1AngleLabel.pack(side=BOTTOM)
Axis1Counterclockwise.pack(side=BOTTOM)
Axis1Label.pack(side=BOTTOM, pady=5)



# Axis 2 Buttons in Control frame
Axis2Label = Label(control_frame, text = "Axis 2",font='Helvetica 18 bold')

Axis2AngleLabel = Label(control_frame, text = LabelAngle2)
Axis2clockwise = Button(control_frame, text="CW - S",width=17, command=lambda: PaintBot.Axis2Clockwise(Axis2AngleLabel))
Axis2Counterclockwise = Button(control_frame, text="CCW - A", width=17,command=lambda: PaintBot.Axis2Counter_clockwise(Axis2AngleLabel))

Axis2clockwise.pack(side=BOTTOM)
Axis2AngleLabel.pack(side=BOTTOM)
Axis2Counterclockwise.pack(side=BOTTOM)
Axis2Label.pack(side=BOTTOM, pady=5)



# Axis 3 Buttons in Control frame
Axis3Label = Label(control_frame, text = "Axis 3",font='Helvetica 18 bold')

Axis3AngleLabel = Label(control_frame, text = LabelAngle3)
Axis3clockwise = Button(control_frame, text="CW - W",width=17, command=lambda: PaintBot.Axis3Clockwise(Axis3AngleLabel))
Axis3Counterclockwise = Button(control_frame, text="CCW - Q", width=17,command=lambda: PaintBot.Axis3Counter_clockwise(Axis3AngleLabel))

Axis3clockwise.pack(side=BOTTOM)
Axis3AngleLabel.pack(side=BOTTOM)
Axis3Counterclockwise.pack(side=BOTTOM)
Axis3Label.pack(side=BOTTOM, pady=5)
Axis3Label.pack(side=BOTTOM, pady=5)

def draw(event=None):
    Paint(PaintBot.link3.getTipXPos(),800 - PaintBot.link3.getTipYPos(),paint_frame)

# Erase drawing
def EraseAll(event=None):
    paint_frame.delete("tag")

# Define Robot
PaintBot = Robot(paint_frame, 800, 800, Axis1AngleLabel, Axis2AngleLabel, Axis3AngleLabel)

#Creating Tittle
Title = Label(control_frame, text = "PAINTBOT - TAMU 2021",font='Helvetica 12 bold')
Title.pack(side=TOP)

# Create a button to update the label widget
PaintButton = Button(control_frame, text="Paint - SpaceBar",width=17, command=draw)
PaintButton.pack(side=TOP, pady=10)


# Create a Reset button for the robot
ResetRobotButton = Button(control_frame, text="Reset Robot - R",width=17, command = lambda: PaintBot.resetRobot(Axis1AngleLabel, Axis2AngleLabel, Axis3AngleLabel))
ResetRobotButton.pack(side=TOP, pady=10)

# Create a erase button for the paint frame
EraseButton = Button(control_frame, text="Erase All - F",width=17, command = EraseAll)
EraseButton.pack(side=TOP, pady=10)

# World Mode Control
World = Label(control_frame, text = "World Control",font='Helvetica 18 bold')
World.pack(side=TOP)

PlusXButton = Button(control_frame, text="+X - L", width=14, command = PaintBot.PlusX)
MinusXButton = Button(control_frame, text="-X - J", width=14, command = PaintBot.MinusX)
PlusYButton = Button(control_frame, text="+Y - I", width=14, command = PaintBot.PlusY)
MinusYButton = Button(control_frame, text="-Y - K", width=14, command = PaintBot.MinusY)

PlusXButton.pack(side=TOP, pady=5)
MinusXButton.pack(side=TOP, pady=5)
PlusYButton.pack(side=TOP, pady=5)
MinusYButton.pack(side=TOP, pady=5)


#Better hotkeys
history = []
targetx = 400
targety = 300

def HotKeyControl():
    for key in history:
        # print(key)
        if key == 81 or key == "q" or key == 113:
            PaintBot.Axis3Counter_clockwise(Axis3AngleLabel, "event")
        if key == 87 or key == "w" or key == 119:
            PaintBot.Axis3Clockwise(Axis3AngleLabel, "event")
        if key == 65 or key == "a" or key == 97:
            PaintBot.Axis2Counter_clockwise(Axis2AngleLabel, "event")
        if key == 83 or key == "s" or key == 115:
            PaintBot.Axis2Clockwise(Axis2AngleLabel, "event")
        if key == 90 or key == "z" or key == 122:
            PaintBot.Axis1Counter_clockwise(Axis1AngleLabel, "event")
        if key == 88 or key == "x" or key == 120:
            PaintBot.Axis1Clockwise(Axis1AngleLabel, "event")
        if key == 82 or key == "r":
            PaintBot.resetRobot(Axis1AngleLabel, Axis2AngleLabel, Axis3AngleLabel, "event")
        if key == 70 or key == "f":
            EraseAll("event")
        if key == 32 or key == "space":
            draw("event")
        # if key == 86:
        #     PaintBot.GoTo(targetx, targety)
        if key == 73:
            PaintBot.targety = PaintBot.targety + 1
            PaintBot.GoTo(PaintBot.targetx, PaintBot.targety)
        if key == 74:
            PaintBot.targetx = PaintBot.targetx - 1
            PaintBot.GoTo(PaintBot.targetx, PaintBot.targety)
        if key == 75:
            PaintBot.targety = PaintBot.targety - 1
            PaintBot.GoTo(PaintBot.targetx, PaintBot.targety)
        if key == 76:
            PaintBot.targetx = PaintBot.targetx + 1
            PaintBot.GoTo(PaintBot.targetx, PaintBot.targety)

    root.after(5, HotKeyControl)


def keyup(e):
    if e.keycode in history :
        history.pop(history.index(e.keycode))

def keydown(e):
    if not e.keycode in history :
        history.append(e.keycode)

root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)

HotKeyControl()



#init robot canvas
#canvas = Canvas(root, width=800, height=800)
root.update()
PaintBot.drawRobot(paint_frame, paint_frame.winfo_width(), paint_frame.winfo_height())



# Run the GUI
root.mainloop()
