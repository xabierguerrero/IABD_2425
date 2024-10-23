from funciones import turno,turno_jugador,turno_maquina

if turno():
    print("Cara. Empiezas tú")
    turno_jugador()
else:
    print("Cruz. Empieza la maquina")
    turno_maquina()