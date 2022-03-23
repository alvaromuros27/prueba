#Teniendo 2 listas; escribir un programa que devuelva una lista que devuelva los elementos comunes de las listas y si



l1=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
p = []

print(f"Esta es la lista 1:  {l1}")
print(f"Esta es la lista 2:  {l2}")

for elemento in l1:
    if elemento in l2:
        if elemento not in p:
            p.append(elemento)

print(f"Esta es la lista con los números que aparecen en las dos listas y sin repetirse {p}")