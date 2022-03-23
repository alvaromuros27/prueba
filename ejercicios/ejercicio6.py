#Preguntar al usuario por una "String" e imprimir si esta es un palindromo(una palabra que se lee igual como oro)

palabra=input('Escribe una palabra: ')


invertido=palabra[len(palabra)::-1]

if(palabra==invertido):
    print('La palabra es palindroma')
else:
    print('La palabra no es palindroma')
