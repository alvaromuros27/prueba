# Dada la lista , imprimir la lista con los numeros menores de 5
l = [1,1,2,3,5,8,13,21,34,55,89]
p = []
for elemento in l:
    if(elemento<5):
        p.append(elemento)

print(f"Esta es la lista : {l}")
print(f"Esta es la lista con los números menores de 5 : {p}")

