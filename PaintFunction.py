def Paint(x, y,frame): #center coordinates, radius
    r = 5 # radius always set to 5
    # x-r = x0  x1 = x + r
    # y-r = y0  y1 = y + r
    return frame.create_oval(x-r, y-r, x+r, y+r,fill="red", tags='tag')