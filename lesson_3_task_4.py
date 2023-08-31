from turtle import *

t = Turtle()
t.speed(8)
t.screen.setup(1200, 800)

def coor(x, y): #функция для переноса черепашки
    t.up()
    t.goto(x, y)
    t.down()

def line(x): #функция рисования линии
    t.fd(x)

def circ(rad, angle): #функция рисования окружности
    t.circle(rad, angle)

#рисуем голову
coor(-300, -250)

def Sqare(length, height, rad, angle): #функция задания квадрата с закругленными углами
    line(length)
    circ(rad, angle)
    line(height)
    circ(rad, angle)
    line(length)
    circ(rad, angle)
    line(height)
    circ(rad, angle)

Sqare(600, 400, 50, 90)

#Рисуем уши
coor(-350,150)
t.left(180)

def ears(length, width): #функция рисования уха
    t.fd(width)
    t.circle(30,90)
    t.fd(length)
    t.circle(30,90)
    t.fd(width)

ears(200, 50)
coor(350,-100)
ears(200, 50)

#Рисуем нос
coor(0, 0)
t.circle(50, 360)

#Рисуем глаза
coor(-50, 50)
t.left(270)
Sqare(100, 100, 30, 90)
coor(210, 50)
Sqare(100, 100, 30, 90)

#Рисуем рот
coor(-120,-150)
t.left(180)
Sqare(40, 200, 20, 90)

t.screen.exitonclick()
t.screen.mainloop()
