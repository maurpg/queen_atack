
def movement():
    movimientos = {'abajo': [1, 0], 'arriba': [-1, 0], 'derecha': [0, 1],
                   'izquierda': [0, -1], 'diagonal_superior_izquierda': [-1, -1],
                   'diagonal_inferior_izquierda': [1, -1],
                   'diagonal_superior_derecha': [-1, 1],
                   'diagonal_inferior_derecha': [1, 1]}
    return movimientos

def input_data(file):
    '''Apertura y lectura del archivo'''
    input_data = []
    f = open(file, "r")
    for x in f:
        input_data.append(x.replace('\n' ,'').split(' '))
    input_data.pop(len(input_data) -1)
    return input_data


def verification(list_data):
    if list_data is None or len(list_data)<= 0:
        return 'Ingrese un archivo que contenga datos'
    else:
        try:
            size_matriz = int(list_data[0][0])
            number_obst = int(list_data[0][1])
            x  = int(list_data[1][0])
            y = int(list_data[1][1])
            erros = False
            position_queen = [x , y]
            if (x or y) > size_matriz:
                return 'Posicion de la reina fuera de la matriz'
            ostacu = list_data[1:]
            print(ostacu)
            len_obsta = len(ostacu)
            print(len_obsta)
            if len_obsta  != number_obst:
                print(len(ostacu) , number_obst)
                return 'El numero de obstaculos no coinciden'
            else:
                for obs in ostacu:
                    if (int(obs[0]) < size_matriz) and (int(obs[1]) < size_matriz):
                        erros = False
                    else:
                       erros = True
            if erros == True:
                return 'Los obstaculos no pueden estar fuera de la matriz'

            return size_matriz , number_obst , position_queen , ostacu
        except :
            return 'Ingrese datos validos'


