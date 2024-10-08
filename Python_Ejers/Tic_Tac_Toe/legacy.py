"""
def check_win_con():
    win_con='0'
    celdas_vacias=mirar_celdas_vacias()
    celdas_maquina=mirar_celdas_maquina()
    win_cons=CONS
    posibles_victorias=[]
    for con in win_cons:
        if len(list(set(celdas_maquina).intersection(con)))==2:
            win_con=str(list(set(con).difference(celdas_maquina)))[2]
            if win_con in celdas_vacias:
                posibles_victorias.append(win_con)    
    return posibles_victorias


def check_loose_con():
    loose_con='0'
    celdas_vacias=mirar_celdas_vacias()
    celdas_jugador=mirar_celdas_jugador()
    loose_cons=CONS
    posibles_derrotas=[] 
    for con in loose_cons:
        if len(list(set(celdas_jugador).intersection(con)))==2:
            loose_con=str(list(set(con).difference(celdas_jugador)))[2]
            if loose_con in celdas_vacias:
                posibles_derrotas.append(loose_con)      
    return posibles_derrotas

def mirar_celdas_jugador():
    celdas_jugador=[]
    for x in range(3):
        for y in range(3):
            if celdas_global[x][y] == JUGADOR:
                celdas_jugador.append(POSICIONES[x][y])
    return celdas_jugador

def mirar_celdas_maquina():
    celdas_maquina=[]
    for x in range(3):
        for y in range(3):
            if celdas_global[x][y] == MAQUINA:
                celdas_maquina.append(POSICIONES[x][y])
    return celdas_maquina
"""
