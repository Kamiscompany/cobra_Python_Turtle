from turtle import Turtle

POS_INICIAL = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Cobra():

    def __init__(self):
        self.corpo = []
        self.criar_cobra()
        self.cabeca = self.corpo[0]

    def crescer(self, pos):
        parte_corpo = Turtle("square")
        parte_corpo.hideturtle()
        parte_corpo.penup()
        parte_corpo.color("red")
        parte_corpo.setpos(pos)
        parte_corpo.showturtle()
        self.corpo.append(parte_corpo)
        self.rabo = self.corpo[-1]

    def aumentar(self):
        self.crescer(self.rabo.pos())

    def criar_cobra(self):
        for posicao in POS_INICIAL:
            self.crescer(posicao)

    def move(self):
        for segmento in range(len(self.corpo) - 1, 0, -1):
            novo_x = self.corpo[segmento - 1].xcor()
            novo_y = self.corpo[segmento - 1].ycor()
            self.corpo[segmento].goto(novo_x, novo_y)
        self.cabeca.forward(20)

    def move_up(self):
        if self.cabeca.heading() != DOWN:
            for parte in self.corpo:
                parte.setheading(UP)

    def move_down(self):
        if self.cabeca.heading() != UP:
            for parte in self.corpo:
                parte.setheading(DOWN)

    def move_left(self):
        if self.cabeca.heading() != RIGHT:
            for parte in self.corpo:
                parte.setheading(LEFT)

    def move_right(self):
        if self.cabeca.heading() != LEFT:
            for parte in self.corpo:
                parte.setheading(RIGHT)

    def reset(self):
        for parte in self.corpo:
            parte.goto(2000, 2000)
        self.corpo.clear()
        self.criar_cobra()
        self.cabeca = self.corpo[0]


