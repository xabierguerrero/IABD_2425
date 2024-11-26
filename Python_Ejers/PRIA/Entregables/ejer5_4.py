import re
TEXTO = "Me lo he pasado muy muy muy bien."
sin_exagerar=re.sub(r"(\b\w+\b )\1+", r"\1",TEXTO)
print(sin_exagerar)