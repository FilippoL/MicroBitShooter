from microbit import *
import random

MAX_BOUND = 4

speed_x = 0
speed_y = 0

position_x = 3
position_y = 3

enemy_position_x = 0
enemy_position_y = 0

enemy_speed = 2.00

is_died = True
is_shooting = False

counter = 0.00

playing = True

score = 0

bullet_position_x = position_x
bullet_position_y = position_y

while True:
    while playing:
            counter = counter + 0.1
            # reinitialise the position every frame
            reading_x = accelerometer.get_x()
            reading_y = accelerometer.get_y()

            # ################# #
            #      UPDATE       #
            # ################# #
            # CAP SPEED
            if reading_x > 20:  # reading from accelerometer says right
                speed_x = 1     # so make the pixel go right
            elif reading_x < -20:  # reading from accelerometer says left
                speed_x = -1       # so make the pixel go left
            else:  # if is steady
                speed_x = 0  # no speed

            # DO THE SAME WITH THE Y
            if reading_y > 20:
                speed_y = 1
            elif reading_y < -20:
                speed_y = -1
            else:
                speed_y = 0
                
            # UPDATE POSITION PLAYER
            position_x = position_x + speed_x
            position_y = position_y + speed_y

            # UPDATE POSITION ENEMY
            if counter > enemy_speed:
                enemy_position_y = enemy_position_y + 1
                counter = 0
                
            # COLLISION
            # PLAYER VS WALLS COLLISION
            if position_x > MAX_BOUND:  # when the pixel goes off-screen
                position_x = MAX_BOUND
            elif position_x < 0:
                position_x = 0

            if position_y > MAX_BOUND:
                position_y = MAX_BOUND
            elif position_y < 0:
                position_y = 0

            # ENEMY VS WALLS COLLISION
            if enemy_position_y > 4:
                is_died = True

            # ENEMY VS BULLETT COLLISION
            if bullet_position_x == enemy_position_x and bullet_position_y == enemy_position_y and is_shooting:
                enemy_speed = enemy_speed - 0.125
                is_shooting = False
                score = score + 1
                is_died = True

            if bullet_position_y < 1:
                is_shooting = False

            if is_died:
                enemy_position_x = random.randrange(5)
                enemy_position_y = 0
                is_died = False
                
            # PLAYER VS ENEMY 
            if position_x == enemy_position_x and position_y == enemy_position_y:
                is_died = True
                playing = False

                
            # UPDATE POSITION BULLETT 
            if is_shooting:
                bullet_position_y = bullet_position_y - 1
            else:
                bullet_position_x = position_x
                bullet_position_y = position_y
                
            # BUTTON PRESS
            if button_a.is_pressed() or button_b.is_pressed():
                is_shooting = True

            # ################# #
            #      DRAW         #
            # ################# #
            
            display.set_pixel(bullet_position_x, bullet_position_y, 5)
            display.set_pixel(enemy_position_x, enemy_position_y, 9)
            display.set_pixel(position_x, position_y, 9)
            sleep(75)
            if not playing:
                display.scroll("GAME OVER, SCORE : " + str(score) + " PRESS ANY BUTTON TO RETRY")
            #####################
            #      CLEAR        #
            #####################
            display.clear()
            
    if button_a.is_pressed() or button_b.is_pressed():
        display.clear()
        score = 0
        playing = True
   
    