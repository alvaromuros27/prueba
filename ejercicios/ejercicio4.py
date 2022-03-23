#Crea un programa que le pregunte al ususario un numero y luego cree una lista de todos los divisores de ese numero


from re import X

p = []
num = int(input('Dime un número '))

x = range(1,num+1)

for elemento in x:
    if(num%elemento==0):
        p.append(elemento)

print(f"Estos son los divisores de {num} : {p}")