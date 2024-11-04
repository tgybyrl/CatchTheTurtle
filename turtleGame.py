import random
import turtle
from random import randint


#screen
game_screen = turtle.Screen()
game_screen.title("Catch The Turtle!")
game_screen.bgcolor("light blue")

#first turtle
turta = turtle.Turtle()
turta.hideturtle()
turta.pencolor("blue")
turta.penup()
turta.color("blue")
turta.shapesize(2)
turta.speed(0)

#second turtle
countdown_turta = turtle.Turtle()
countdown_turta.hideturtle()
countdown_turta.color("black")

#third turtle
mikelencelo = turtle.Turtle()
mikelencelo.shape('turtle')
mikelencelo.shapesize(3)
mikelencelo.color('green')
mikelencelo.penup()
mikelencelo.speed(3)

#countdown timer
countdown_turta.teleport(-130,280.0)
FONT_timer = ('Arial', 27, 'normal')

def countdown(time):
    game_screen.onclick(None)  # disable click until countdown completes
    countdown_turta.clear()

    if time > 0:
        countdown_turta.teleport(-100,280.0)
        countdown_turta.write(f"Time : {time}", font=FONT_timer)
        game_screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        mikelencelo.hideturtle()
        countdown_turta.teleport(-130, 280.0)
        countdown_turta.write("Game Over!",font=FONT_timer)
''' else:        #to loop the game with out restarting app
        countdown_turta.teleport(-130, 280.0)
        countdown_turta.write("Click Screen", font=FONT_timer)
        game_screen.onclick(lambda x, y: countdown(15))          
'''
countdown_turta.write("Click Screen",font=FONT_timer)

game_screen.onclick(lambda x,y : countdown(5))

#score function and mouse interaction
Font_score = "Arial",24,'normal'
turta.teleport(-80,350.0)
s = 0
turta.write(f'Score : {s}', font=(Font_score))
def give_position(x,y):
    print(mikelencelo.pos())
    global s
    s +=1
    mikelencelo.clear()
    if mikelencelo.pos():
        turta.clear()
        turta.write(f'Score : {s}', font=(Font_score))
    if s > 9:
        turta.teleport(-100,350.0)

mikelencelo.onclick(give_position,btn=1,add=None)


running = True
def random_teleport():
    if running:
        mikelencelo.teleport(random.randint(-300,200),random.randint(-300,250))
        game_screen.ontimer(random_teleport, 500)

    else :
        pass

random_teleport()

turtle.mainloop()
