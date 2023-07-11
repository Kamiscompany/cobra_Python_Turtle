from turtle import Turtle
import random


class Comida(Turtle):

    def __init__(self, alt, lar):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.shapesize(0.75, 0.75)
        self.sortear_posicao(alt, lar)

    def sortear_posicao(self, altura, largura):
        random_x = random.randint(-largura / 2 + 20, largura / 2 - 20)
        random_x = round(random_x / 20) * 20
        random_y = random.randint(-altura / 2 + 20, altura / 2 - 20)
        random_y = round(random_y / 20) * 20
        self.goto(random_x, random_y)