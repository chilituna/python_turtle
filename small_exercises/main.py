from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.title('Object-oriented turtle demo')
my_screen.bgcolor("black")

kilppis = Turtle()
print(kilppis)

colors = ["crimson", "chartreuse", "dark violet", "spring green", "snow", "orange", "dodger blue"]
angles = [90, 180, 270, 360]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

## DRAW DASHED LINE
# kilppis.shape("turtle")
# kilppis.color("green4")
# for _ in range(10):
#     kilppis.forward(10)
#     kilppis.up()
#     kilppis.forward(10)
#     kilppis.down()

## DRAW DIFFERENT SHAPES
# kilppis.up()
# kilppis.setpos(-50,-200)
# kilppis.down()
# sides = 3
# my_screen.colormode(255)
# r = 240
# g = 240
# b = 0
# for _ in range (10):
#     for i in range (sides):
#         kilppis.pencolor(r, g, b)
#         kilppis.forward(100)
#         kilppis.left(360 / sides)
#     sides += 1
#     g -= 20
#     b += 20

# #DRAW RANDOM WALK
# kilppis.speed(0)
# kilppis.pensize(15)
# for _ in range(500):
#     kilppis.pencolor(random.choice(colors))
#     kilppis.left(random.choice(angles))
#     kilppis.forward(30)


##DRAW SPIROGRAPH
kilppis.speed("fastest")
my_screen.colormode(255)
angle = 10
for _ in range (int(360 / angle)):
    kilppis.pencolor(random_color())
    kilppis.circle(100)
    kilppis.setheading(kilppis.heading() + angle)


my_screen.exitonclick()


