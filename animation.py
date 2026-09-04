import turtle
import random

t= turtle.Turtle()
s= turtle.Screen()
s.bgcolor("white")
t.speed(0)

for i in range(200):
    t.pencolor("black")
    t.forward(i)
    t.right(144)
    t.circle(i/3)
    t.right(20)

