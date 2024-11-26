import re
TEXTO = """Se ha facturado un total de 1500 € al usuario test@dominio.es durante 
el año 2019. Otros usuarios, como prueba@otro.com o new@contact.com han gastado 
solamente 500€."""

correos=[]
precios=[]

expresion = r'(?P<correo>\w+@\w+\.\w+)|(?P<precio>\d+(.\d+)?\s?€)'
ocurrencias = re.finditer(expresion, TEXTO)

for ocurrencia in ocurrencias:
    if ocurrencia.group('correo'):
        correos.append(ocurrencia.group('correo'))
    if ocurrencia.group('precio'):
        precios.append(ocurrencia.group('precio'))

print("Correos:",correos)
print("Precios:",precios)