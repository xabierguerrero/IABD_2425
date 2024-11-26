import re
correo="nombre@dominio.ext"
no_correo="Juan"

def es_email(entrada):
    expresion=r"[a-zA-Z0-9.-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}"
    
    return re.search(expresion,entrada) is not None

print(es_email(correo))
print(es_email(no_correo))