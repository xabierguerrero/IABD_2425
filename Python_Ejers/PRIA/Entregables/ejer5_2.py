import re

TEXTO = """En 1492 los Reyes Católicos financiaron el proyecto del navegante Cristóbal 
Colón en la búsqueda de una nueva ruta comercial con Asia a través del océano 
Atlántico, y proclamarían la expulsión de los judíos. La llegada al Nuevo Mundo 
y la posterior conquista de América forjaron la creación del Imperio español. 
Durante los siguientes siglos España se alzaría como actor principal del mundo 
occidental y primera potencia de la época. Durante los siglos xvi y xvii 
tendría lugar también la época de mayor apogeo de la cultura y las artes 
hispanas conocida como Siglo de Oro.

El Imperio español en 1580, tras la unificación de la península ibérica bajo un 
único rey español Felipe II, comprendía América del Sur, América Central y el 
Caribe, grandes áreas de América del Norte en diferentes grados de influencia o 
control, las islas Filipinas en Asia, así como enclaves de diversa importancia 
en las costas de África y la India. Incluía además numerosas posesiones en 
Europa, los Países Bajos españoles, el Ducado de Milán o el Reino de Nápoles, la 
mayoría de ellas perdidas tras la paz de Utrecht de 1713."""

años=re.findall(r"\d{4}",TEXTO)
print(años)