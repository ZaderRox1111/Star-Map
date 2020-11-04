import turtle
import sys
import math

def main():
    stars_data = sys.argv[1]
    t = turtle.Turtle()

    turtle.bgcolor('black')
    turtle.screensize(750)
    turtle.speed(0)
    turtle.tracer(50,0)
    t.ht()

    with open(stars_data) as stars:
        lines = stars.readlines()

    for line in lines:
        line = line[: (len(line) - 2)]
        line = line.split()
        x = float(line[0]) * 375.0
        y = float(line[1]) * 375.0
        z = float(line[2])
        magnitude = float(line[4])
        side_length = ((10/(magnitude + 2)))

        side_length *= z + 0.5

        side_length = min(10, max(0.005, side_length))

        draw_star(x, y, t, side_length)

    turtle.exitonclick()

def draw_square(t, side_length):
    t.color('white')
    t.begin_fill()
    t.fd(side_length)
    t.right(90)
    t.fd(side_length)
    t.right(90)
    t.fd(side_length)
    t.right(90)
    t.fd(side_length)
    t.right(90)
    t.end_fill()

def draw_star(x, y, t, side_length):
    t.penup()
    t.goto(x, y)
    t.pendown()

    draw_square(t, side_length)

main()
