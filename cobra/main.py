from turtle import Screen
from ccobra import Cobra
from comida import Comida
from placar import Placar
from juiz import Juiz
import time

LARGURA = 500
ALTURA = 500

# criar e ajustar tela
tela = Screen()
tela.setup(width=LARGURA, height=ALTURA)
tela.bgcolor("black")
tela.tracer(0)
# criar cobra
snake = Cobra()
gameover = False
# criar comida
food = Comida(ALTURA, LARGURA)
# criar placar
placar = Placar(ALTURA)
# criar Bordas do jogo
juiz = Juiz(ALTURA, LARGURA)


# inputs
def check_inputs():
    tela.listen()
    tela.onkeypress(snake.move_up, "w")
    tela.onkeypress(snake.move_down, "s")
    tela.onkeypress(snake.move_left, "a")
    tela.onkeypress(snake.move_right, "d")


# gameover
def check_morte():
    global gameover
    snake_x = snake.cabeca.xcor()
    snake_y = snake.cabeca.ycor()
    limite_tela_x = LARGURA / 2
    limite_tela_y = ALTURA / 2
    for pedaco in snake.corpo[1:]:
        if snake.cabeca.distance(pedaco) < 10:
            reset_jogo()
    if snake_x >= limite_tela_x or snake_x <= -limite_tela_x or snake_y >= limite_tela_y or snake_y <= -limite_tela_y:
        reset_jogo()


def reset_jogo():
    snake.reset()
    placar.game_over()
    time.sleep(4)
    placar.reset_game()


# LOOP principal do Jogo
while not gameover:
    tela.update()
    time.sleep(0.15)
    snake.move()
    check_inputs()
    check_morte()
    # comer comida
    if snake.cabeca.distance(food) < 15:
        food.sortear_posicao(ALTURA, LARGURA)
        snake.aumentar()
        placar.aumenta_pontos(100)

tela.exitonclick()
