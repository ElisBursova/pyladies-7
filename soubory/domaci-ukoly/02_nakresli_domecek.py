# -*- coding: UTF-8 -*-
# Napiš funkci, která vykreslí domeček dané velikosti.
# (t.j. velikost se zadá argumentem)

from turtle import forward, left, right, exitonclick, hideturtle
from math import sqrt

def nakresli_domecek(velikost):
    left(45)
    forward(sqrt(2) * velikost)
    left(90)
    forward(sqrt(2) * velikost / 2)
    left(90)
    forward(sqrt(2) * velikost / 2)
    left(90)
    forward(sqrt(2) * velikost)
    right(135)
    forward(velikost)
    right(90)
    forward(velikost)
    right(90)
    forward(velikost)
    right(90)
    forward(velikost)
    # Bez tohoto prikazu bude na konci nakreslene cary sipka
    hideturtle()

velikost_domecku = input("Zadej velikost domecku: ")
nakresli_domecek(velikost_domecku)
exitonclick()