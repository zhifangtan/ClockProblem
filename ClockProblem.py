import turtle

'''
Define a function to draw the clock face
and calculate the angle between clock hands
'''
def circle(hour, minute):
    '''
    Draw the template of the clock circle and the line around the clock
    :param hour:
    :param minute:
    :return:
    '''
    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(0)
    myPen.up()
    myPen.goto(0, -180)
    myPen.down()
    myPen.circle(180)
    for i in range(1, 13):
        myPen.up()
        myPen.goto(0, 0)
        myPen.setheading(90)  # Point to the top - 12 o'clock
        myPen.right(i * 360 / 12)
        myPen.forward(155)
        myPen.down()
        myPen.forward(25)
    for i in range(1, 61):
        myPen.up()
        myPen.goto(0, 0)
        myPen.setheading(90)  # Point to the top - 12 o'clock
        myPen.right(i * 360 / 60)
        myPen.forward(170)
        myPen.down()
        myPen.forward(10)

    '''
    Draw the hour hand
    '''
    myPen.up()
    myPen.goto(0, 0)
    myPen.setheading(90)
    myPen.right(hour * 360 / 12 + (minute * 0.5))
    myPen.down()
    myPen.forward(100)

    '''
    Draw the minute hand
    '''
    myPen.up()
    myPen.goto(0, 0)
    myPen.setheading(90)  # Point to the top - 0 minute
    myPen.right(minute * 360 / 60)
    myPen.down()
    myPen.forward(150)

    '''
    Write the time and the calculated angle below the clock face
    angle = (0.5 * (60 * hour - 11 * minute)) % 360
    if angle is larger than 180, it is subtracted from 360
    in order to get the smallest angle
    '''
    myPen.up()
    myPen.goto(0,-240)
    myPen.down()
    time = str("%02d"%hour) + ":" + str(minute)
    myPen.write(time,False,align="center",font=("Arial",20,"normal"))
    myPen.up()
    myPen.goto(0,-270)
    myPen.down()
    angle = (0.5 * (60 * hour - 11 * minute)) % 360
    if angle > 180:
        angle = 360 - angle
    angleDisplay = "Angle Between the Hands: " + str(angle) + "deg"
    myPen.write(angleDisplay, False, align="center", font=("Arial", 20, "normal"))
    turtle.getscreen()

'''
Text file with the data is read
the data is split into pairs of hour and minute as a sub list
and all these lists are put in a home list called filelist
'''
file = open("text.txt","r")
data = file.read()
data = data.strip("\n")
filelist = [line.split(":") for line in data.splitlines()]

'''
The lists of data are first being printed out using the for loop
If the time is invalid( hour is not within 0 to 24 or min is not within 0 to 60)
the word "ERROR" is printed
If the time is valid, it will be shown on the clock face with the calculated degree
the user will then be asked if he/she wants to proceed to the next number
If yes, the next time in the list will be shown on the clock face if it is valid
else the clock face will stop updating and user can click on it to exit
Lastly, the collected time (newlist) will be printed out
'''
print(filelist)
row = len(filelist)
newlist = []
for i in range(row):
    if  int(filelist[i][0]) not in range(0,24) or int(filelist[i][1]) not in range(0,60):
        print("ERROR %02d:%02d"%(int(filelist[i][0]),int(filelist[i][1])))
    else:
        newlist.append([int(filelist[i][0]),int(filelist[i][1])])
        circle(int(filelist[i][0]),int(filelist[i][1]))
        choice = input("Next number? yes / no \n").lower()
        if choice == "yes":
            turtle.clearscreen()
        else:
            break
turtle.exitonclick()
print("Valid Time: ")
print(newlist)


