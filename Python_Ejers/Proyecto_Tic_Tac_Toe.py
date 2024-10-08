import random
import termcolor

celdas_global=[['1','2','3'],['4','5','6'],['7','8','9']]
POSICIONES=[['1','2','3'],['4','5','6'],['7','8','9']]

JUGADOR="X"
MAQUINA="O"

VICTORIA_JUGADOR=termcolor.colored(JUGADOR, 'red')
VICTORIA_MAQUINA=termcolor.colored(MAQUINA, 'blue')

def turno():
    moneda=["cara","cruz"]
    lanzar=random.choice(moneda)
    #lanzar="cara"
    if lanzar=="cara":
        
        return True
    else:
        
        return False

def dibujar_tablero():
    tablero="""
        ╔═══╗╔═══╗╔═══╗
        ║ {} ║║ {} ║║ {} ║
        ╚═══╝╚═══╝╚═══╝
        ╔═══╗╔═══╗╔═══╗
        ║ {} ║║ {} ║║ {} ║
        ╚═══╝╚═══╝╚═══╝
        ╔═══╗╔═══╗╔═══╗
        ║ {} ║║ {} ║║ {} ║
        ╚═══╝╚═══╝╚═══╝
    """
    return tablero.format(celdas_global[0][0],celdas_global[0][1],celdas_global[0][2],
                          celdas_global[1][0],celdas_global[1][1],celdas_global[1][2],
                          celdas_global[2][0],celdas_global[2][1],celdas_global[2][2])

def fin_partida():
    print(dibujar_tablero())
    exit()



def turno_jugador():
    if empate():
        fin_partida()

    if gana_maquina():
            print("Victoria de la Maquina.")
            fin_partida()
    else:
        print(dibujar_tablero())
        try:
            celdas_vacias=mirar_celdas_vacias()
            casilla=int(input("Introduce la casilla en la que quieres poner tu marca(X):"))
            if str(casilla) not in celdas_vacias:
                print("ERROR. Esa casilla ya está ocupada.")
                turno_jugador()
            else:
                match casilla:
                    case 1:
                        celdas_global[0][0]=JUGADOR
                    case 2:
                        celdas_global[0][1]=JUGADOR
                    case 3:
                        celdas_global[0][2]=JUGADOR
                    case 4:
                        celdas_global[1][0]=JUGADOR
                    case 5:
                        celdas_global[1][1]=JUGADOR
                    case 6:
                        celdas_global[1][2]=JUGADOR
                    case 7:
                        celdas_global[2][0]=JUGADOR
                    case 8:
                        celdas_global[2][1]=JUGADOR
                    case 9:
                        celdas_global[2][2]=JUGADOR
                    case _:
                        print("Error. Valor no valido introducido.")
                        turno_jugador()    
        except:
            print("Error. Valor no valido introducido.")
            turno_jugador()
        turno_maquina()  


def mirar_celdas_vacias():
    celdas_vacias=[]
    valores_vacios=['1','2','3','4','5','6','7','8','9']
    for x in range(3):
        for y in range(3):
            if celdas_global[x][y] in valores_vacios:
                celdas_vacias.append(celdas_global[x][y])
    return celdas_vacias

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

def gana_jugador():

    celdas_vacias=mirar_celdas_vacias()
    celdas_jugador=mirar_celdas_jugador()
    win_cons=[  ['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['1','4','7'],
                ['2','5','8'],
                ['3','6','9'],
                ['1','5','9'],
                ['3','5','7']]
    for con in win_cons:
        if len(list(set(celdas_jugador).intersection(con)))==3:
            for x in range(3):
                for y in range(3):
                    if POSICIONES[x][y] in con:
                        celdas_global[x][y]=VICTORIA_JUGADOR
            return True

    return False

def gana_maquina():
    celdas_vacias=mirar_celdas_vacias()
    celdas_maquina=mirar_celdas_maquina()
    win_cons=[  ['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['1','4','7'],
                ['2','5','8'],
                ['3','6','9'],
                ['1','5','9'],
                ['3','5','7']]
    for con in win_cons:
        if len(list(set(celdas_maquina).intersection(con)))==3:
            for x in range(3):
                for y in range(3):
                    if POSICIONES[x][y] in con:
                        celdas_global[x][y]=VICTORIA_MAQUINA
            print(dibujar_tablero())
            return True

    return False


def check_win_con():
    win_con='0'
    celdas_vacias=mirar_celdas_vacias()
    celdas_maquina=mirar_celdas_maquina()
    win_cons=[  ['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['1','4','7'],
                ['2','5','8'],
                ['3','6','9'],
                ['1','5','9'],
                ['3','5','7']]
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
    celdas_maquina=mirar_celdas_maquina()
    loose_cons=[['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['1','4','7'],
                ['2','5','8'],
                ['3','6','9'],
                ['1','5','9'],
                ['3','5','7']]
    posibles_derrotas=[] 
    for con in loose_cons:
        if len(list(set(celdas_jugador).intersection(con)))==2:
            loose_con=str(list(set(con).difference(celdas_jugador)))[2]
            if loose_con in celdas_vacias:
                posibles_derrotas.append(loose_con)      

    return posibles_derrotas

def jugada_optima():
    optimo='0'
    if len(check_win_con())>0:
        print("Existe condición de victoria")
        optimo=random.choice(check_win_con())

    elif len(check_loose_con())>0:
        print("Existe condición de derrota")
        optimo=random.choice(check_loose_con())

    else:
        esquinas=['1','3','7','9']
        aristas=['2','4','6','8']
        celdas_libres =mirar_celdas_vacias()
        celdas_maquina=mirar_celdas_maquina()
        celdas_jugador=mirar_celdas_jugador()
        match len(celdas_libres):
            case 9: #Si el tablero esta vacio la jugada optima es cualquiera de las esquinas
                optimo=random.choice(esquinas)
            case 8: #Vamos segundos y que es nuestro primer turno
                if '5' in celdas_libres: #si el centro está libre lo tomamos
                    optimo='5'
                else: # sino cualquier esquina es optima
                    optimo=random.choice(esquinas)
            case 7: #Vamos primeros y es nuestro segundo turno (tiene una sola casilla)
                if celdas_jugador[0] in esquinas: # el jugador ha jugado en una esquina
                    optimo=random.choice(list(set(celdas_libres).intersection(esquinas))) # Cualquier esquina es perfectamente valida
                elif celdas_jugador[0] in aristas:
                    optimo='5' # Amenazamos con la diagonal y con el centro
                else: # El jugador ha jugado en el centro:
                    optimo=str(10-int(celdas_maquina[0])) # Hacemos una Diagonal OXO
            case 6: # Vamos segundos y es nuestro segundo turno
                optimo=random.choice(list(set(celdas_libres).intersection(aristas))) # En este caso el empate esta practicamente garantizado, un lado es un poco mejor en este caso.
            case 5: #Vamos primeros y es nuestro tercer turno
                print("hehe")
                exit()

                
                
    return optimo  


def turno_maquina():
    if empate():
        fin_partida()

    if gana_jugador():
        print("Victoria del Jugador.")
        fin_partida()
    else:
        print(dibujar_tablero())
        celdas_vacias=mirar_celdas_vacias()
        jugada=jugada_optima()
        match jugada:
                    case '1':
                        celdas_global[0][0]=MAQUINA
                    case '2':
                        celdas_global[0][1]=MAQUINA
                    case '3':
                        celdas_global[0][2]=MAQUINA
                    case '4':
                        celdas_global[1][0]=MAQUINA
                    case '5':
                        celdas_global[1][1]=MAQUINA
                    case '6':
                        celdas_global[1][2]=MAQUINA
                    case '7':
                        celdas_global[2][0]=MAQUINA
                    case '8':
                        celdas_global[2][1]=MAQUINA
                    case '9':
                        celdas_global[2][2]=MAQUINA
                    case _:
                        print("Algo ha salido catastroficamente mal. ESTE MENSAJE DE TEXTO NUNCA DEBERIA SER VISIBLE.")
                        turno_maquina()
        print("la maquina juego en:", jugada)
        turno_jugador()
        
# si no hay celdas vacias la partida finaliza en empate
def empate():
    celdas_vacias=mirar_celdas_vacias()
    if not celdas_vacias:
        print("Partida Finalizada en empate.")
        return True
    else:
        return False

"""


"""
#empeiza la partida

if turno():
    print("Cara. Empiezas tú")
    turno_jugador()
else:
    print("Cruz. Empieza la maquina")
    turno_maquina()