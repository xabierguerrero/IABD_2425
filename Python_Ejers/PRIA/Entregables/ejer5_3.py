import re

TEXTO = "¡¡¡¡¡¡¡QUÉ SORPRESA!!!!!!!"

no_gritar=re.sub(r"(\W)\1+",r"\1",TEXTO)
print(no_gritar)