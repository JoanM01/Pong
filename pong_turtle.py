import turtle

#Ventana
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Marcador
marcadorA = 0
marcadorB = 0

#Jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(2.5)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

#Jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(2.5)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)


#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)


#Linea
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#Variables de la velocidad de la pelota
pelota.dx = 0.5
pelota.dy = 0.5


#Dibujar el marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0    PONG    Player 2: 0", align="center", font=("Courier", 25, "normal"))


#Funciones de las barras
def jugadorA_up():
	y = jugadorA.ycor()
	y += 20
	jugadorA.sety(y)

def jugadorA_down():
	y = jugadorA.ycor()
	y -= 20
	jugadorA.sety(y)

def jugadorB_up():
	y = jugadorB.ycor()
	y += 20
	jugadorB.sety(y)

def jugadorB_down():
	y = jugadorB.ycor()
	y -= 20
	jugadorB.sety(y)

#Teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")



while True:
	wn.update()

	pelota.setx(pelota.xcor() + pelota.dx)
	pelota.sety(pelota.ycor() + pelota.dy)

	#Revisa colisiones con los bordes de la ventana
	if pelota.ycor() > 290:
		pelota.dy *= -1
	if pelota.ycor() < -290:
		pelota.dy *= -1

	# Si la pelota sale por la izq o derecha, la pelota vuelve al centro
	if pelota.xcor() > 390:
		pelota.goto(0,0)
		pelota.dx *= -1
		marcadorA += 1
		pen.clear()

        #Formato
		pen.write(f"Player  1: {marcadorA}    PONG    Player 2: {marcadorB}", align="center", font=("Courier", 25, "normal"))

	if pelota.xcor() < -390:
		pelota.goto(0,0)
		pelota.dx *= -1
		marcadorB += 1
		pen.clear()
		
		#Formato
		pen.write(f"Player 1: {marcadorA}     PONG    Player 2: {marcadorB}", align="center", font=("Courier", 25, "normal"))


	#Revisa las colisiones
	if ((pelota.xcor() > 340 and pelota.xcor() < 350)
			and (pelota.ycor() < jugadorB.ycor() + 50
			and pelota.ycor() > jugadorB.ycor() - 50)):
		pelota.dx *= -1

	if ((pelota.xcor() < -340 and pelota.xcor() > -350)
			and (pelota.ycor() < jugadorA.ycor() + 50
			and pelota.ycor() > jugadorA.ycor() - 50)):
		pelota.dx *= -1