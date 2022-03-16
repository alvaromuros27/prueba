#CREAR PROGRAMA QUE LE PREGUNTE AL USUARIO SU NOMBRE Y EDAD, Y EN QUE AÑO TENDRA 100 AÑOS

name = input('¿como te llamas?')
age = input('¿que edad tienes?')

edad = 100-int(age)
year= 2022+edad
print(f"En el año {year} {name} tendra 100 años")