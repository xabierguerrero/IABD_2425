import random
import termcolor

POSICIONES=[['1','2','3'],
            ['4','5','6'],
            ['7','8','9']]

JUGADOR="X"
MAQUINA="O"

VICTORIA_JUGADOR=termcolor.colored(JUGADOR, 'red')
VICTORIA_MAQUINA=termcolor.colored(MAQUINA, 'blue')

CONDS = [['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']]


celdas_global=[['1','2','3'],
               ['4','5','6'],
               ['7','8','9']]


def turno():
    lanzar=random.choice([True,False])
    return lanzar

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
    print(tablero.format(celdas_global[0][0],celdas_global[0][1],celdas_global[0][2],
                        celdas_global[1][0],celdas_global[1][1],celdas_global[1][2],
                        celdas_global[2][0],celdas_global[2][1],celdas_global[2][2]))
    return

def fin_partida():
    dibujar_tablero()
    exit()



def mirar_celdas_vacias():
    celdas_vacias=[]
    valores_vacios=['1','2','3','4','5','6','7','8','9']
    for x in range(3):
        for y in range(3):
            if celdas_global[x][y] in valores_vacios:
                celdas_vacias.append(POSICIONES[x][y])
    return celdas_vacias


def mirar_ocupado(opciones):
    celdas=[]
    for x in range(3):
        for y in range(3):
            if celdas_global[x][y] == opciones:
                celdas.append(POSICIONES[x][y])
    return celdas



def gana(ganador):
    win_cons=CONDS
    if ganador==MAQUINA:
        celdas=mirar_ocupado(MAQUINA)
    else:
        celdas=mirar_ocupado(JUGADOR)
    for con in win_cons:
        if len(list(set(celdas).intersection(con)))==3:
            for x in range(3):
                for y in range(3):
                    if POSICIONES[x][y] in con:
                        if ganador==MAQUINA:
                            celdas_global[x][y]=VICTORIA_MAQUINA
                        else:
                            celdas_global[x][y]=VICTORIA_JUGADOR
            return True

    return False

def check_con(win_loose):
    condicion='0'
    celdas_vacias=mirar_celdas_vacias()
    if win_loose==True: #True es buscar victoria
        celdas=mirar_ocupado(MAQUINA)
    else: # False es buscar derrota
        celdas=mirar_ocupado(JUGADOR)
    cons=CONDS
    opciones=[]
    for con in cons:
        if len(list(set(celdas).intersection(con)))==2:
            condicion=str(list(set(con).difference(celdas)))[2]
            if condicion in celdas_vacias:
                opciones.append(condicion)
    return opciones


def jugada_optima():
    optimo='0'
    esquinas=['1','3','7','9']
    aristas=['2','4','6','8']
    celdas_libres =mirar_celdas_vacias()
    celdas_maquina=mirar_ocupado(MAQUINA)
    celdas_jugador=mirar_ocupado(JUGADOR)
    if len(check_con(True))>0:
        optimo=random.choice(check_con(True))

    elif len(check_con(False))>0:
        optimo=random.choice(check_con(False))
    else:
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
                # Sin condiciones de victoria ni derrota el centro siempre está libre
                optimo='5'
            case 4: # Vamos segundos y es nuestro tercer turno
                #el jugador no ha creado diagona XOX, ya no es posible ganar con esquinas
                optimo=random.choice(list(set(celdas_libres).intersection(aristas)))
            case _: # no hay caso con 3 casillas que no tenga win_cons ni loose_cons
                    # caso 2 y 1 se pueden resolver con azar
                optimo=random.choice(celdas_libres)
    return optimo  

def tomar_casilla(casilla,jugador):
    match casilla:
        case '1':
            celdas_global[0][0]=jugador
        case '2':
            celdas_global[0][1]=jugador
        case '3':
            celdas_global[0][2]=jugador
        case '4':
            celdas_global[1][0]=jugador
        case '5':
            celdas_global[1][1]=jugador
        case '6':
            celdas_global[1][2]=jugador
        case '7':
            celdas_global[2][0]=jugador
        case '8':
            celdas_global[2][1]=jugador
        case '9':
            celdas_global[2][2]=jugador
        case _:
            if jugador==JUGADOR:
                print("Error. Valor no valido introducido.")
                turno_jugador()
            else:    
                print("Algo ha salido catastroficamente mal. ESTE MENSAJE DE TEXTO NUNCA DEBERIA SER VISIBLE.")
                exit() 
    return  

def turno_jugador():
    if empate():
        fin_partida()

    if gana(MAQUINA):
            print("Victoria de la Maquina.")
            fin_partida()
    else:
        dibujar_tablero()
        try:
            celdas_vacias=mirar_celdas_vacias()

            casilla=str(input("Introduce la casilla en la que quieres poner tu marca(X):"))
            if str(casilla) not in celdas_vacias:
                print("ERROR. Esa casilla ya está ocupada.")
                turno_jugador()
            else:
                tomar_casilla(casilla,JUGADOR)
        except:
            print("ERROR. Valor no valido introducido.")
            turno_jugador()
        turno_maquina()  

def turno_maquina():
    if empate():
        fin_partida()

    if gana(JUGADOR):
        print("Victoria del Jugador.")
        fin_partida()
    else:
        dibujar_tablero()
        casilla=jugada_optima()
        tomar_casilla(casilla,MAQUINA)         
        print("la maquina juega en:", casilla)
        turno_jugador()
        
# si no hay celdas vacias la partida finaliza en empate
def empate():
    celdas_vacias=mirar_celdas_vacias()
    if not celdas_vacias:
        print("Partida Finalizada en empate.")
        return True
    else:
        return False