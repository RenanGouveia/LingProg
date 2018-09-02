#13. Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

while True:
    print('Caso queira pausar o programa, deixe o nome em Branco')
    nome = str(input('Digite seu nome: '))
    if(nome == ''): break
    print(nome)
    if(len(nome) > 3):
        print('Nome validado.')
    else:
        print('Nome inválido')
    idade = int(input('Digite a idade: '))
    if(idade <= 150 and idade >=0):
        print('Idade validada')
    else:
        print('Idade inválida')

    salario = float(input('Digite o salário: '))
    if(salario > 0):
        print('Salário validado')
    else:
        print('Salário inválido')

    sexo = str(input('Digite o gênero: ')).upper()
    if(sexo in ('M','F')):
        print('Gênero validado')
    else:
        print('Gênero inválido')

    estado_civil = str(input('Digite seu Estado Civil: s, c, v ou d: ')).upper()
    if(estado_civil in ('S', 'c', 'V','D')):
        print('Estado Civil validado')
    else:
        print('Estado Civil inválido')