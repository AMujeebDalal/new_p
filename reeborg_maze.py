def turn_right():
    turn_left()
    turn_left()
    turn_left()
while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()  
            
            
            

            
            
            
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while at_goal() != True:
    while right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
            if front_is_clear():
                move()
