import math
def reward_function(params):
	# Parámetros de entrada
	speed = params['speed']  # Velocidad del coche
	steering_angle = abs(params['steering_angle'])  # Ángulo de dirección en grados (positivo)
	track_width = params['track_width']  # Ancho de la pista
	distance_from_center = params['distance_from_center']  # Distancia desde el centro de la pista
	is_offtrack = params['is_offtrack']  # Si el coche se ha salido de la pista
	waypoints = params['waypoints']  # Lista de puntos de referencia de la pista
	closest_waypoints = params['closest_waypoints']  # Índices de los puntos más cercanos


	# Definimos un umbral de distancia para considerar el coche como 'centrado'
	marker_1 = 0.1 * track_width
	marker_2 = 0.25 * track_width


	# Ponderación inicial de la recompensa
	reward = 1.0


	
	# Penalizar si el coche se sale de la pista
	if is_offtrack:
		return 1e-3  # Penalización fuerte


	# Incentivar que el coche esté cerca del centro de la pista
	if distance_from_center <= marker_1:
		reward += 1.5
	elif distance_from_center <= marker_2:
		reward += 0.5
	else:
		reward += 0.1  # Menor recompensa cuanto más lejos del centro


	# Incentivar el drifting en las curvas usando el ángulo de dirección y velocidad
	if steering_angle > 15 and speed > 2.5:  # Solo si tiene un buen ángulo de giro y velocidad alta
		reward += (steering_angle / 30.0) * speed  # Más recompensa para giros amplios y alta velocidad


	# Penalización si el ángulo es muy bajo en las curvas (no intenta derrapar)
	if steering_angle < 10:
		reward *= 0.8  # Penalización si no intenta girar lo suficiente


	# Penalización por girar innecesariamente en tramos rectos
	is_straight_path = distance_from_center <= marker_1 
	if is_straight_path and steering_angle > 5:  # Si el coche está centrado y gira 
		reward *= 0.7  # Penalización por pequeños giros innecesarios
	if is_straight_path and steering_angle > 15:  # Más penalización para giros grandes
		reward *= 0.5


    # Incentivar alineación con la trayectoria ideal
	# Obtener el vector de la dirección del coche respecto a la pista
	next_waypoint = waypoints[closest_waypoints[1]]
	prev_waypoint = waypoints[closest_waypoints[0]]
    
	track_direction = math.atan2(next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0])
	heading = params['heading']  # Dirección del coche en grados
	direction_diff = abs(track_direction - math.radians(heading))
	direction_diff = min(direction_diff, math.pi)  # Asegurar el menor ángulo


	# Penalizar si la dirección del coche se desvía mucho de la dirección ideal
	DIRECTION_THRESHOLD = 0.2  # En radianes (~11.5 grados)
	if direction_diff > DIRECTION_THRESHOLD:
		reward *= 0.5




	return float(reward)
