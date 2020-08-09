#def DisplayBoard(board):
# ASDASD
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#

#def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#

#def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#

#def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#

#def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#


tablero = []

filaCero = [1, 2, 3]
filaUno = [4, 5, 6]
filaDos = [7, 8, 9]

tablero = filaCero, filaUno, filaDos

#for fila in board:
#    print (fila)

#print ("+",7*"-",sep="",end="+ \n")




borde = "+-------"
linea = "|       "

def impBorde():
    print (3*borde, sep="", end="+")

def impLinea():
    print ("\n",3*linea, sep = "", end = "| \n")


def DisplayBoard(board):
    impBorde()
    for i in range (3):
        impLinea()
        print ("|", end = "")
        for j in range (3):
            print ("   ", board[i][j],"   ", sep = "", end = "|")

        #print ("\n")
        impLinea()
        impBorde()


DisplayBoard(tablero)

def correspondencia(nro):
    diccionario = {
        1 : [0, 0],
        2 : [0, 1],
        3 : [0, 2],
        4 : [1, 0],
        5 : [1, 1],
        6 : [1, 2],
        7 : [2, 0],
        8 : [2, 1],
        9 : [2, 2]
    }
    #print(type(diccionario.get(nro)))
    return diccionario.get(nro)


def EnterMove(board):
    #DisplayBoard(board)
    while True:
        movimiento = int(input("\n Ingrese nro: "))
        if movimiento > 0 and movimiento < 10:
            break

    ficha = correspondencia(movimiento)
    a, b = int(ficha[0]), int(ficha[1])
    print (board[int(ficha[0])] [int(ficha[1])])
    #print(a, b)


EnterMove(tablero)
