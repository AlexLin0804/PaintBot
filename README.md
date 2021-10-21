# PAINTBOT - INVERSE KINEMATICS:  

## Overview:

![alt text](https://github.tamu.edu/yk7335/CSCE-452/blob/master/Project%202/PaintBot.PNG?raw=true)

We built a simulation of a RRR robot shown in the figure below. The robot has 3 links and is connected to base link at the bottom. Our robotic siumation 
allows users to move each of the 3 links counter clockwise and clockwise bby 1 pixel (1 degree). It also allows the user to paint a filled circle at the tip of 
link 3. Our link 1 had a length of 150 pixels, link 2 had a length of 100 pixel, and link 3 had a length of 75 pixels. 

We used the forward kinematics to calculate the the movement of each link when counter clockwise or clockwise was pressed. When a axis was rotated we calcualted the 
new x and y values by the following functions.  

| X1 = X0 + rCos(theta)  | Y1 = Y0 + rCos(theta) |
| --- | --- |

where r is the length of the link.  

Links 1 and 2 had some extra rotations we had to keep track of. We had to take the other links' position into account or links would disconnect at a certain point. To deal 
with this we roated link 1 or 2 the same amount we moved the other links in the x and y axis. Finally we accountd for the other links' orientation by rotating them by 1 degree. 

## Function Implementation  

### 10/1/21
updateRobot(self, canvas, width, height) -> this function updates the 3 links position by getting their current x and y cordinates. 

drawRobot(self, canvas, width, height) -> this function initially draws the 3 links and the axes. We used Tkinter's create_oval method for the axis and the create_line method for the links.  

Axis1Clockwise(self, angleLabel, event=None), Axis2Clockwise(self, angleLabel, event=None), Axis3Clockwise(self, angleLabel, event=None) -> This function changes the x and y position of link link 1,2,3. We do this by using the equations above. Since this is moving the link clockwise we subtract 1 degree to the link's angle each time. After getting the new cordinates we update the robot's drawing using the updateRobot function.    

Axis1Counter_clockwise(self, angleLabel, event=None), Axis2Counter_clockwise(self, angleLabel, event=None), Axis3Counter_clockwise(self, angleLabel, event=None) -> This function changes the x and y position of link link 1,2,3. We do this by using the equations above. Since this is moving the link counter-clockwise we add 1 degree to the link's angle each time the function is called. After getting the new cordinates we update the robot's drawing using the updateRobot function.

resetRobot(self, event=None) -> This function resets the location of the all links to the starting position.

getAllLinkPositions(self)-> returns a list of the position of the tip of all the links.  

Paint(x, y,frame)-> This function paints the circle on the canvas. It uses the x and y values of the links to paint where the link is. We used Tkinter's create_oval method to paint the circle.  

GoTo(self, x, y) -> This function uses a inverse kinematic solution to the arm angles using the target position. Since last 2 links sumed up to more than first link, we used this functon to create a solution that is complete over the work space.  

### 10/10/21  

(+/-) (x,y) buttons -> We added buttons to let the robot arm move in x and y pixel values. Each plus and minus would move the robot's links by 1 pixel. These buttons are calling our GoTo(self,x,y) funciton which handles our inverse kinematic solution. Since that was coded by the last project's due date we used that finish out inverse kinematics solution.


## Compile Instrcutions
Run the command: `python3 main.py`

