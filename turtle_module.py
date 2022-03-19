import turtle
import math

bob = turtle.Turtle()
print(bob)
turtle.mainloop()  # tells the window to wait for the user to do sometinhg.

"""Fazendo um quadrado"""
bob.fd(100)  # move foward
bob.lt(90)  # left turn
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

"""Fazendo um quadrado"""
bob.bk(120)  # move backward
bob.rt(90)  # rigth turn
bob.bk(120)  # move backward
bob.rt(90)
bob.bk(120)  # move backward
bob.rt(90)
bob.bk(120)

"""Usando o for"""

for i in range(4):
    print('Hello!')

"""Fazendo o quadrado e utilizando o for"""

for i in range(4):
    bob.fd(140)
    bob.lt(90)

"""Exercicio 1 do capítulo 4"""


def square(t):
    for i in range(4):
        t.fd(140)
        t.lt(90)


square(bob)

"""Exercicio 2 do capítulo 4"""


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


square(bob, 100)
square(bob, 120)
square(bob, 140)
square(bob, 160)
square(bob, 180)
square(bob, 200)

"""Exercicio 3 do capítulo 4"""


def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


polygon(bob, 100, 6)
polygon(bob, 80, 8)
polygon(bob, 140, 7)

"""Exercicio 4 do capítulo 4"""


def circle(t, r):
    circunference = 2 * math.pi * r
    n = 50
    length = circunference / n
    polygon(t, length, n)


circle(bob, 100)
circle(bob, 75)
circle(bob, 50)
circle(bob, 25)