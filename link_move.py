from tkinter import *
import math 
import numpy as np


# This might be helpful 
# X = Radius * cos(Theta)
# Y = Radius * sin(Theta)

class Robot:
    def __init__(self, pFrame, width, height, a1l, a2l, a3l):
        self.link1 = Link(400, 0, 400, 150)
        self.link2 = Link(400, 150, 400, 250)
        self.link3 = Link(400, 250, 400, 325)

        # Angle for rotation
        self.Angle1 = 90
        self.Angle2 = 90
        self.Angle3 = 90
        self.TrueAngle2 = 90
        self.TrueAngle3 = 90

        # Target positions
        self.targetx = 400
        self.targety = 325

        #self.control_frame = cFrame
        self.paint_frame = pFrame
        self.width = width
        self.height = height

        # print(self.width, self.height)

        self.Angle1Label = a1l
        self.Angle2Label = a2l
        self.Angle3Label = a3l
    
    def GoTo(self, x, y):
        # self.paint_frame.create_oval(
        #     x - 10,
        #     800 - y - 10,
        #     x + 10,
        #     800 - y + 10,
        #     fill="red",
        #     tags="a1"
        # )
        #inverse kinematic solution to arm angles given target position
        #since last 2 links sum to more than first link, solution is complete over the work space
        hy_dist = math.sqrt((400 - x) ** 2 + y ** 2)
        target_angle1 = math.degrees(math.atan((x - 400) / (0 - y))) + 90
        target_angle1 = round(target_angle1 % 360)

        Link1EndX = self.link1.getTipXPos()
        link1EndY = self.link1.getTipYPos()

        if self.getAngle1() < target_angle1:
            self.Axis1Counter_clockwise(self.Angle1Label)
        if self.getAngle1() > target_angle1:
            self.Axis1Clockwise(self.Angle1Label)

        #angle 2 frame respect to origin
        dist_left_toTarget = math.sqrt((Link1EndX - x) ** 2 + (link1EndY - y) ** 2)
        try:
            target_angle2 = target_angle1 + math.degrees(math.acos((dist_left_toTarget ** 2 + 100 ** 2 - 75 ** 2) / (2 * dist_left_toTarget * 100)))
            target_angle2 = round(target_angle2 % 360)
        except:
            return

        #angle 3 frame respect to origin
        try:
            target_angle3 = target_angle1 * 0 + target_angle2 + math.degrees(math.acos((100 ** 2 + 75 ** 2 - dist_left_toTarget ** 2) / (2 * 100 * 75))) + 180
            target_angle3 = round(target_angle3 % 360)
        except:
            return

        #print(target_angle3)
        #print(self.getAngle3())

        #adjust arm angles
        while(self.getAngle2() < target_angle2 or self.getAngle2() > target_angle2 or self.getAngle3() < target_angle3 or self.getAngle3() > target_angle3):
            if self.getAngle2() < target_angle2:
                self.Axis2Counter_clockwise(self.Angle2Label)
            if self.getAngle2() > target_angle2:
                self.Axis2Clockwise(self.Angle2Label)
            if self.getAngle3() < target_angle3:
                self.Axis3Counter_clockwise(self.Angle3Label)
            if self.getAngle3() > target_angle3:
                self.Axis3Clockwise(self.Angle3Label)

    def getAngle1(self):
        return self.Angle1

    def getAngle2(self):
        return self.Angle2

    def getAngle3(self):
        return self.Angle3


    def getAllLinkPositions(self):
        return [
            400, 0,
            self.link1.getTipXPos(), self.link1.getTipYPos(),
            self.link2.getTipXPos(), self.link2.getTipYPos(),
            self.link3.getTipXPos(), self.link3.getTipYPos(),
        ]

    def Axis1Clockwise(self, angleLabel, event=None):
        #calculate new link1 tip position
        self.Angle1 = self.Angle1 - 1
        angleLabel['text'] = self.Angle1
        #print(self.Angle1)
        newTipX = self.link1.getBaseXPos() + 150*math.cos(math.radians(self.Angle1))
        newTipY = self.link1.getBaseYPos() + 150*math.sin(math.radians(self.Angle1))

        xMovementDifference = newTipX - self.link1.getTipXPos()
        yMovementDifference = newTipY - self.link1.getTipYPos()

        self.link1.setTipCords(newTipX,newTipY)

        #set link1 tip and link2 base to same
        self.link2.setBaseCords(self.link1.getTipXPos(), self.link1.getTipYPos())
        #set link2 tip
        self.link2.setTipCords(self.link2.getTipXPos() + xMovementDifference, self.link2.getTipYPos() + yMovementDifference)
        #set link2 tip and link3 base to same
        self.link3.setBaseCords(self.link2.getTipXPos(), self.link2.getTipYPos())
        #set link3 tip
        self.link3.setTipCords(self.link3.getTipXPos() + xMovementDifference, self.link3.getTipYPos() + yMovementDifference)
        self.Axis2Clockwise(Label(), event)
        
        self.updateRobot(self.paint_frame, self.width, self.height)
        return 0

    def Axis1Counter_clockwise(self, angleLabel, event=None):
        #calculate new link1 tip position
        self.Angle1 = self.Angle1 + 1
        angleLabel['text'] = self.Angle1
        newTipX = self.link1.getBaseXPos() + 150*math.cos(math.radians(self.Angle1))
        newTipY = self.link1.getBaseYPos() + 150*math.sin(math.radians(self.Angle1))

        xMovementDifference = newTipX - self.link1.getTipXPos()
        yMovementDifference = newTipY - self.link1.getTipYPos()

        self.link1.setTipCords(newTipX,newTipY)

        #set link1 tip and link2 base to same
        self.link2.setBaseCords(self.link1.getTipXPos(), self.link1.getTipYPos())
        #set link2 tip
        self.link2.setTipCords(self.link2.getTipXPos() + xMovementDifference, self.link2.getTipYPos() + yMovementDifference)
        #set link2 tip and link3 base to same
        self.link3.setBaseCords(self.link2.getTipXPos(), self.link2.getTipYPos())
        #set link3 tip
        self.link3.setTipCords(self.link3.getTipXPos() + xMovementDifference, self.link3.getTipYPos() + yMovementDifference)
        self.Axis2Counter_clockwise(Label(), event)
        
        self.updateRobot(self.paint_frame, self.width, self.height)
        return 0

    def Axis2Clockwise(self, angleLabel, event=None):
        self.Angle2 = self.Angle2 - 1
        if angleLabel['text'] != "":
            self.TrueAngle2 = self.TrueAngle2 - 1
            angleLabel['text'] = self.TrueAngle2
        newTipX = self.link2.getBaseXPos() + 100*math.cos(math.radians(self.Angle2))
        newTipY = self.link2.getBaseYPos() + 100*math.sin(math.radians(self.Angle2))

        xMovementDifference = newTipX - self.link2.getTipXPos()
        yMovementDifference = newTipY - self.link2.getTipYPos()
        
        self.link2.setTipCords(newTipX,newTipY)
        #set link2 tip and link3 base to same
        self.link3.setBaseCords(self.link2.getTipXPos(), self.link2.getTipYPos())
        #set link3 tip
        self.link3.setTipCords(self.link3.getTipXPos() + xMovementDifference, self.link3.getTipYPos() + yMovementDifference)
        self.Axis3Clockwise(Label(), event)
        
        self.updateRobot(self.paint_frame, self.width, self.height)
        return 0

    def Axis2Counter_clockwise(self, angleLabel, event=None):
        self.Angle2 = self.Angle2 + 1
        if angleLabel['text'] != "":
            self.TrueAngle2 = self.TrueAngle2 + 1
            angleLabel['text'] = self.TrueAngle2
        newTipX = self.link2.getBaseXPos() + 100*math.cos(math.radians(self.Angle2))
        newTipY = self.link2.getBaseYPos() + 100*math.sin(math.radians(self.Angle2))

        xMovementDifference = newTipX - self.link2.getTipXPos()
        yMovementDifference = newTipY - self.link2.getTipYPos()
        
        self.link2.setTipCords(newTipX, newTipY)
        #set link2 tip and link3 base to same
        self.link3.setBaseCords(self.link2.getTipXPos(), self.link2.getTipYPos())
        #set link3 tip
        self.link3.setTipCords(self.link3.getTipXPos() + xMovementDifference, self.link3.getTipYPos() + yMovementDifference)
        self.Axis3Counter_clockwise(Label(), event)

        self.updateRobot(self.paint_frame, self.width, self.height)
        return 0

    def Axis3Clockwise(self, angleLabel, event=None):
        self.Angle3 = self.Angle3 - 1
        if angleLabel['text'] != "":
            self.TrueAngle3 = self.TrueAngle3 - 1
            angleLabel['text'] = self.TrueAngle3
        newTipX = self.link3.getBaseXPos() + 75*math.cos(math.radians(self.Angle3))
        newTipY = self.link3.getBaseYPos() + 75*math.sin(math.radians(self.Angle3))
        
        self.link3.setTipCords(newTipX,newTipY)

        #print(self.link3.getTipXPos())
        #print(self.link3.getTipYPos())

        self.updateRobot(self.paint_frame, self.width, self.height)

    def Axis3Counter_clockwise(self, angleLabel, event=None):
        self.Angle3 = self.Angle3 + 1
        if angleLabel['text'] != "":
            self.TrueAngle3 = self.TrueAngle3 + 1
            angleLabel['text'] = self.TrueAngle3
        newTipX = self.link3.getBaseXPos() + 75*math.cos(math.radians(self.Angle3))
        newTipY = self.link3.getBaseYPos() + 75*math.sin(math.radians(self.Angle3))

        self.link3.setTipCords(newTipX,newTipY)

        #print(self.link3.getTipXPos())
        #print(self.link3.getTipYPos())

        self.updateRobot(self.paint_frame, self.width, self.height)

    # Reset to its oringinal position 
    def resetRobot(self, angle1, angle2, angle3, event=None):
        self.Angle1 = 90
        self.Angle2 = 90
        self.Angle3 = 90

        self.TrueAngle1 = 90
        self.TrueAngle2 = 90
        self.TrueAngle3 = 90

        angle1['text'] = 90
        angle2['text'] = 90
        angle3['text'] = 90

        self.targetx = 400
        self.targety = 325


        self.link1.setTipCords(400,150)
        self.link2.setTipCords(400,250)
        self.link3.setTipCords(400,325)

        self.link1.setBaseCords(400,0)
        self.link2.setBaseCords(400,150)
        self.link3.setBaseCords(400,250)
        self.updateRobot(self.paint_frame, self.width, self.height)

    def drawRobot(self, canvas, width, height):
        #MAGIC NUMBER, DON'T KNOW WHERE 4 COMES FROM
        height = height - 4
        #link1
        canvas.create_line(
            self.link1.getBaseXPos(),
            height - self.link1.getBaseYPos(),
            self.link1.getTipXPos(),
            height - self.link1.getTipYPos(),
            width = 20,
            tags="l1"
        )
        #link2
        canvas.create_line(
            self.link2.getBaseXPos(),
            height - self.link2.getBaseYPos(),
            self.link2.getTipXPos(),
            height - self.link2.getTipYPos(),
            width = 10,
            tags="l2"
        )
        #link3
        canvas.create_line(
            self.link3.getBaseXPos(),
            height - self.link3.getBaseYPos(),
            self.link3.getTipXPos(),
            height - self.link3.getTipYPos(),
            width = 5,
            tags="l3"
        )
        #axis1
        canvas.create_oval(
            self.link1.getBaseXPos() - 10,
            height - self.link1.getBaseYPos() - 10,
            self.link1.getBaseXPos() + 10,
            height - self.link1.getBaseYPos() + 10,
            fill="red",
            tags="a1"
        )
        #axis2
        canvas.create_oval(
            self.link2.getBaseXPos() - 7,
            height - self.link2.getBaseYPos() - 7,
            self.link2.getBaseXPos() + 7,
            height - self.link2.getBaseYPos() + 7,
            fill="blue",
            tags="a2"
        )
        #axis3
        canvas.create_oval(
            self.link3.getBaseXPos() - 4,
            height - self.link3.getBaseYPos() - 4,
            self.link3.getBaseXPos() + 4,
            height - self.link3.getBaseYPos() + 4,
            fill="green",
            tags="a3"
        )

    def updateRobot(self, canvas, width, height):
    	height = height - 4
    	canvas.coords('l1', self.link1.getBaseXPos(), height - self.link1.getBaseYPos(), self.link1.getTipXPos(), height - self.link1.getTipYPos())
    	canvas.coords('l2', self.link2.getBaseXPos(), height - self.link2.getBaseYPos(), self.link2.getTipXPos(), height - self.link2.getTipYPos())
    	canvas.coords('l3', self.link3.getBaseXPos(), height - self.link3.getBaseYPos(), self.link3.getTipXPos(), height - self.link3.getTipYPos())
    	canvas.coords('a2', self.link2.getBaseXPos() - 7, height - self.link2.getBaseYPos() - 7, self.link2.getBaseXPos() + 7, height - self.link2.getBaseYPos() + 7)
    	canvas.coords('a3', self.link3.getBaseXPos() - 4, height - self.link3.getBaseYPos() - 4, self.link3.getBaseXPos() + 4, height - self.link3.getBaseYPos() + 4)
    	return

    def updateControl(self, canvas, width, height):
        pass

    # World Control Mode functions 
    def PlusX(self):
        self.targetx+=1
        self.GoTo(self.targetx, self.targety)

    def MinusX(self):
        self.targetx-=1
        self.GoTo(self.targetx, self.targety)
        
    def PlusY(self):
        self.targety+=1
        self.GoTo(self.targetx, self.targety)
        
    def MinusY(self):
        self.targety-=1
        self.GoTo(self.targetx, self.targety)
        


class Link:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def getBaseXPos(self):
        return self.x1

    def getBaseYPos(self):
        return self.y1

    def getTipXPos(self):
        return self.x2

    def getTipYPos(self):
        return self.y2

    def setBaseCords(self, x, y):
        self.x1 = x
        self.y1 = y

    def setTipCords(self, x, y):
        self.x2 = x
        self.y2 = y