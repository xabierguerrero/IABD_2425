nums = []
prod = 1
print("¿Cuantos numero va a introducir?")

try:
    num=int(input())
except:
    print("Valor no válido introducido")
    exit()

for i in range(num):
   nums.append(int(input("Introduce numero:")))
   prod = prod*nums[i]

print("El producto de los números introducidos es:",prod)