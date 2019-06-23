import numpy as np
from python_intermedio.validation import input_data,verification , movement


def printed(tamaño_matriz ,posicion_reina , posiciones):
    '''Creacion de la matriz y ubicacion de la reina y los obstaculos'''
    matriz = np.zeros((tamaño_matriz,tamaño_matriz))
    for i in range(len(posiciones)):
        obstaculo = posiciones[i]
        matriz[int(obstaculo[0])][int(obstaculo[1])] = 5
    matriz[position_reina[0]][posicion_reina[1]] = 1
    return matriz

def pintar_movimientos(matriz , posicion_reina , key ):
    '''este metodo pinta los diferentes movimientos de la reina'''
    movimientos = movement()
    if key in movimientos:
        try :
            x , y = posicion_reina
            new_x = movimientos[key][0] + x
            new_y = movimientos[key][1] + y
            if matriz[new_x][new_y] == 0 and new_y >=0 and new_x>= 0:
                matriz[new_x][new_y] = 2
                pintar_movimientos(matriz , [new_x , new_y] , key)
                return matriz
            else:
                return matriz
        except:
            pass

def counter(tamaño_matriz,numero_obstaculos ,posicion_reina , posiciones ):
    matriz = printed(tamaño_matriz  , position_reina, posiciones)
    posicion_reina = position_reina
    movimientos = {'abajo':None, 'arriba':None,'derecha':None,'izquierda':None,'diagonal_superior_izquierda':None,
                   'diagonal_superior_derecha':None, 'diagonal_inferior_izquierda':None,'diagonal_inferior_derecha':None}
    for key in movimientos.keys():
       pintar_movimientos(matriz , posicion_reina ,key )
    return matriz

try:
    entradas = input_data('input')
    tamaño_matriz , numero_obstaculos, position_reina, ostaculos = verification(entradas)
    matriz = counter(tamaño_matriz , numero_obstaculos , position_reina, ostaculos)
    print(matriz)
except:
    print(verification(entradas))
    print('Corrija la entrada de datos')

