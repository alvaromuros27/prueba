#Preguntar al usuario un número y decir si es capicuo.
num=input('Escribe un numero ')


if len(num)%2==0:
    s1= num[:len(num)//2]
    s2= num[len(num)//2:]
    invertido=s2[len(s2)::-1]
    if(s1==invertido):
        print('El numero es capicuo')
    else:
        print('No es capicuo')
else:
    s3 = num[:len(num) // 2]
    s4= num[(len(num) // 2)+1:]
    if s3 == s4[::-1]:
        print("El número es capicuo")
    else:
        print('No es capicuo')

