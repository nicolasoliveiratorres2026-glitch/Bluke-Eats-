#Importando as bibliotecas
import turtle
import random
import math
import winsound

winsound.PlaySound("bluke_eats.wav", winsound.SND_LOOP | winsound.SND_ASYNC)
#Criando a variável de pontuação
pontos = 0

#Fazendo a lista "corpo", que é o corpo da Bluke
corpo = []

bluke = turtle.Turtle()
bluke.speed(1)
comida = turtle.Turtle()
comida.speed(0)

s = turtle.Screen()
s.tracer(0)
#Fazendo com que o turtle preste atenção nas teclas que a gente vai pressionar
s.listen()

#Fazendo com que a Bluke e a comida dela não risque a tela
bluke.penup()
comida.penup()
comida.goto(random.randint(-200, 200), random.randint(-200, 200))
#Colocando o título da janela
s.title("Bluke Eats!")

#Configurando o tamanho da janela do jogo
s.setup(width=600, height=600)

#Registrando os sprites
s.register_shape("bluke_direita.png")
s.register_shape("bluke_esquerda.png")
s.register_shape("bluke_cima.png")
s.register_shape("bluke_baixo.png")
s.register_shape("bluke_comendo_baixo.png")
s.register_shape("bluke_comendo_cima.png")
s.register_shape("bluke_comendo_direita.png")
s.register_shape("bluke_comendo_esquerda.png")
s.register_shape("corpo.png")
s.register_shape("comida.png")

bluke.shape("bluke_direita.png")
comida.shape("comida.png")


#Criando as funções de movimento e de criar o corpo
def criar_corpo():
    pedaco = turtle.Turtle()
    pedaco.speed(0)
    pedaco.penup()
    pedaco.shape("corpo.png")
    if len(corpo) > 0:
        ultimo = corpo[-1]
        pedaco.goto(ultimo.xcor(), ultimo.ycor())
    else:
        angulo = math.radians(bluke.heading())
        x_atras = bluke.xcor() - math.cos(angulo) * 40
        y_atras = bluke.ycor() - math.cos(angulo) * 40
        pedaco.goto(x_atras, y_atras)
    corpo.append(pedaco)

def mover():
    global pontos
    x_antigo = bluke.xcor()
    y_antigo = bluke.ycor()
    for i in range(len(corpo)-1, 0, -1):
        x_da_frente = corpo[i-1].xcor()
        y_da_frente = corpo[i-1].ycor()
        corpo[i].goto(x_da_frente, y_da_frente)
    if len(corpo) > 0:
          corpo[0].goto(x_antigo, y_antigo)
    bluke.fd(60)
    if bluke.distance(comida) < 70:
          comida.goto(random.randint(-200, 200), random.randint(-200, 200))
          pontos += 1
          criar_corpo()
    s.update()
    s.ontimer(mover, 100)

def cima():
    global pontos
    bluke.shape("bluke_cima.png")
    bluke.setheading(90)
    if bluke.distance(comida) < 100:
            bluke.shape("bluke_comendo_cima.png")
    if bluke.distance(comida) < 70:
            comida.goto(random.randint(-200, 200), random.randint(-200, 200))
            pontos += 1
    
def baixo():
    global pontos
    bluke.shape("bluke_baixo.png")
    bluke.setheading(270)
    if bluke.distance(comida) < 100:
        bluke.shape("bluke_comendo_baixo.png")
    if bluke.distance(comida) < 70:
            comida.goto(random.randint(-200, 200), random.randint(-200, 200))
            pontos += 1

def direita():
    global pontos
    bluke.shape("bluke_direita.png")
    bluke.setheading(0)
    if bluke.distance(comida) < 100:
            bluke.shape("bluke_comendo_direita.png")
    if bluke.distance(comida) < 70:
            comida.goto(random.randint(-200, 200), random.randint(-200, 200))
            pontos += 1
    
def esquerda():
    global pontos
    bluke.shape("bluke_esquerda.png")
    bluke.setheading(180)
    if bluke.distance(comida) < 100:
            bluke.shape("bluke_comendo_esquerda.png")
    if bluke.distance(comida) < 70:
            comida.goto(random.randint(-200, 200), random.randint(-200, 200))
            pontos += 1

#Definindo quais teclas clicar para ativar as funções de movimento
s.onkeypress(cima, "Up")
s.onkeypress(cima, "w")
s.onkeypress(cima, "W")
s.onkeypress(baixo, "Down")
s.onkeypress(baixo, "s")
s.onkeypress(baixo, "S")
s.onkeypress(direita, "Right")
s.onkeypress(direita, "d")
s.onkeypress(direita, "D")
s.onkeypress(esquerda, "Left")
s.onkeypress(esquerda, "a")
s.onkeypress(esquerda, "A")
s.ontimer(mover, 100)
turtle.done()
