from turtle import Turtle

class Juiz(Turtle):

  def __init__(self, alt, lar):
    super().__init__()
    self.color("white")
    self.speed("fastest")
    self.pensize(4)
    self.hideturtle()
    self.penup()
    self.vMove = alt
    self.hMove = lar
    self.goto(alt / 2, lar / 2)
    self.bordas()

  def bordas(self):
    self.pendown()
    for i in range(2):
      self.right(90)
      self.forward(self.vMove)
      self.right(90)
      self.forward(self.hMove)
