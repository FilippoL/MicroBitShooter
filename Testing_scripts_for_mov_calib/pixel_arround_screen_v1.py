from microbit import *

MAX_BOUND = 4

speed_x = 0
speed_y = 0

position_x = 3
position_y = 3

while True:
        #reinitialise the position every frame
        reading_x = accelerometer.get_x()
        reading_y = accelerometer.get_y()
        
        
        #####################
        #      UPDATE       #
        #####################
        #CAP SPEED
        if reading_x > 20:#reading from accelerometer says right
            speed_x = 1   #so make the pixel go right
        elif reading_x < -20:#reading from accelerometer says left
            speed_x = -1  #so make the pixel go left
        else: #if is steady
            speed_x = 0 #no speed
            
        #DO THE SAME WITH THE Y
        if reading_y > 20:
            speed_y = 1
        elif reading_y < -20:
            speed_y = -1
        else:
            speed_y = 0
        
        #ADD THE SPEED TO THE POSITION
        position_x = position_x + speed_x
        position_y = position_y + speed_y

        #CAP POSITION
        if position_x > MAX_BOUND: #if the pixel goes off-screen
            position_x = MAX_BOUND
        elif position_x < 0:
            position_x = 0

        if position_y > MAX_BOUND:
            position_y = MAX_BOUND
        elif position_y < 0:
            position_y = 0

        #####################
        #      DRAW         #
        #####################
        display.set_pixel(position_x, position_y, 9)
        sleep(50)

        #####################
        #      CLEAR        #
        #####################
        display.clear()
        