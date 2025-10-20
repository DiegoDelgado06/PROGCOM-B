import turtle
screen = turtle.Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
def dibujar_rectangulo(x, y, ancho, alto, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color('black', color)
    t.begin_fill()
    for _ in range(2):
        t.forward(ancho)
        t.left(90)
        t.forward(alto)
        t.left(90)
    t.end_fill()
def escribir_texto(x, y, texto, tamano=14, color='black', estilo='bold'):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.write(texto, font=('Arial', tamano, estilo))
def pared_ladrillos_intercalados(x, y, filas, columnas, ladrillo_ancho, ladrillo_alto, color_ladrillo, color_lineas):
    t.pensize(1)
    for fila in range(filas):
        offset = ladrillo_ancho / 2 if fila % 2 else 0
        for col in range(columnas + 1):
            ladrillo_x = x + col * ladrillo_ancho - offset
            ladrillo_y = y + fila * ladrillo_alto
            if ladrillo_x >= x + columnas * ladrillo_ancho:
                continue
            dibujar_rectangulo(ladrillo_x, ladrillo_y, ladrillo_ancho, ladrillo_alto, color_ladrillo)
            t.penup()
            t.goto(ladrillo_x, ladrillo_y)
            t.pendown()
            t.color(color_lineas)
            t.setheading(0)
            t.forward(ladrillo_ancho)
            t.backward(ladrillo_ancho)
            t.left(90)
            t.forward(ladrillo_alto)
            t.backward(ladrillo_alto)
            t.right(90)
        t.penup()
        t.goto(x, y + (fila + 1) * ladrillo_alto)
        t.pendown()
        t.forward(columnas * ladrillo_ancho)
def dibujar_persona(x, y):
    t.pensize(2)
    t.color('black')
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(x, y - 5)
    t.pendown()
    t.goto(x, y - 20)
    t.goto(x - 7, y - 12)
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.goto(x + 7, y - 12)
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.goto(x - 5, y - 30)
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.goto(x + 5, y - 30)
def dibujar_rama(x, y, direccion=1):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('forestgreen')
    t.pensize(3)
    t.setheading(90 * direccion)
    t.forward(20)
    for angulo in [30, -30]:
        t.right(angulo)
        t.forward(10)
        t.backward(10)
        t.left(angulo)
    t.pensize(2)
    t.color('black')
def cara_frontal(x, y):
    ladrillo_ancho = 30
    ladrillo_alto = 20
    columnas = 7
    filas = 6
    pared_ladrillos_intercalados(x, y, filas, columnas, ladrillo_ancho, ladrillo_alto, 'lightsalmon', 'gray')
    puerta_ancho = 50
    puerta_alto = 80
    puerta_x = x + (columnas * ladrillo_ancho - puerta_ancho) / 2
    puerta_y = y
    dibujar_rectangulo(puerta_x, puerta_y, puerta_ancho, puerta_alto, 'gray')
    escribir_texto(puerta_x + 5, puerta_y + puerta_alto + 5, 'Floristeria DADH', 14)
    ventana_x = x + 10
    ventana_y = y + ladrillo_alto * filas - 50
    dibujar_rectangulo(ventana_x, ventana_y, 40, 40, 'lightblue')
    dibujar_persona(ventana_x + 20, ventana_y + 30)
    dibujar_rama(x + 50, y + filas * ladrillo_alto - 5, direccion=-1)
    dibujar_rama(x + 150, y + filas * ladrillo_alto - 5, direccion=-1)
    dibujar_rama(x + 50, y - 5, direccion=1)
    dibujar_rama(x + 150, y - 5, direccion=1)
def cara_trasera(x, y):
    pared_ladrillos_intercalados(x, y, 6, 7, 30, 20, 'lightsalmon', 'gray')
    escribir_texto(x + 75, y + 60, 'D A D H', 28, 'black', 'normal')
def cara_izquierda(x, y):
    pared_ladrillos_intercalados(x, y, 6, 4, 30, 20, 'lightsalmon', 'gray')
def cara_derecha(x, y):
    pared_ladrillos_intercalados(x, y, 6, 4, 30, 20, 'lightsalmon', 'gray')
def dibujar_casa_completa():
    cara_frontal(-330, 0)
    cara_trasera(100, 0)
    cara_izquierda(-330, -180)
    cara_derecha(100, -180)
    t.hideturtle()
    screen.mainloop()
dibujar_casa_completa()
