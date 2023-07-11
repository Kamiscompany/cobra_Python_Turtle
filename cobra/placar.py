from turtle import Turtle

ALINHAMENTO = "center"
FONTE = ("Courier", 20, "normal")
FONTEGO = ("Courier", 30, "bold")


class Placar(Turtle):
    def __init__(self, altura):
        super().__init__()
        self.pontos = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.pos_y = altura / 2 - 40
        self.load_save()
        self.escreve_pontos()

    def escreve_pontos(self):
        self.clear()
        self.color("white")
        self.goto(0, self.pos_y)
        self.write(f'Pontos: {self.pontos}  Recorde: {self.high_score}', False, ALINHAMENTO, FONTE)

    def aumenta_pontos(self, valor):
        self.pontos += valor
        self.escreve_pontos()

    def save_record(self):
        arquivo_save = open("save_cobrinha.txt", "w")
        arquivo_save.write(str(self.high_score))
        arquivo_save.close()

    def load_save(self):
        arquivo_save = open("save_cobrinha.txt", "r")
        self.high_score = int(arquivo_save.read())
        arquivo_save.close()

    def reset_game(self):
        if self.pontos > self.high_score:
            self.high_score = self.pontos
            self.save_record()
        self.pontos = 0
        self.escreve_pontos()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write('GAME OVER', False, ALINHAMENTO, FONTEGO)
