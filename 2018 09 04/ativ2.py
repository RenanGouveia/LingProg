# 2. Faça um Programa que verifque se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra')).upper()

if (letra in ('A', 'E', 'I', 'O', 'U')):
    print(letra ,'é uma vogal')
else:
    print( letra ,' não é uma vogal')

