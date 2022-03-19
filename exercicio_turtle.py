import turtle
import math


def square(t, length, cor="orange"):
    t.color(cor)
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n, cor="blue"):
    angle = 360 / n
    t.color(cor)
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r, cor="red"):
    circunference = 2 * math.pi * r
    n = 50
    length = circunference / n
    polygon(t, length, n, cor)

# dir(turtle)


if __name__ == '__main__':

    bob = turtle.Turtle()
    alice = turtle.Turtle()

    bob.penup()
    bob.goto((-200, 40))
    bob.pendown()

    alice.penup()
    alice.goto((200, 40))
    alice.pendown()

    circle(bob, 100)
    circle(alice, 100)

    bob.penup()
    bob.goto((-210, -220))
    bob.pendown()

    alice.penup()
    alice.goto((210, -220))
    alice.pendown()

    polygon(bob, 100, 3)
    polygon(alice, 100, 3)

    bob.penup()
    bob.goto((-220, -40))
    bob.pendown()
    bob.pensize(5)

    alice.penup()
    alice.goto((200, -40))
    alice.pendown()
    alice.pensize(5)

    square(bob, 80)
    square(alice, 80)


    bob.penup()
    bob.goto((-210, -220))
    bob.pendown()

    alice.penup()
    alice.goto((210, -220))
    alice.pendown()

    polygon(bob, 100, 6)
    polygon(alice, 100, 6)


    # turtle.clear()


