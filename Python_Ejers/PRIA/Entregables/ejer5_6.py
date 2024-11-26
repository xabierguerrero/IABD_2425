import re
TELEFONOS = "968 12 23 31, 900 141 142, 945112233, 656-247733"

expresion=r"\b(\d{3} \d{2} \d{2} \d{2}|\d{3} \d{3} \d{3}|\d{9}|\d{3}-\d{6})\b"
ocurrencias=re.finditer(expresion,TELEFONOS)

telefonos_formato=[]

for ocurrencia in ocurrencias:
    formato=(ocurrencia.group()).replace("-","").replace(" ","")
    telefonos_formato.append(formato)

print(telefonos_formato)