#11. Faça um programa que faça 5 perguntas para uma pessoa
#sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no fnal emitir uma classifcação sobre a
#participação da pessoa no crime. Se a pessoa responder
#positivamente a 2 questões ela deve ser classifcada como
#"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
#contrário, ele será classifcado como "Inocente".

interrogado = str(input('Por gentileza, insira seu nome: ')).upper()

pergunta1 = int(input('Telefonou para a vítima? Sim = 1 ou Não = 0: '))
pergunta2 = int(input('Esteve no local do crime?Sim = 1 ou Não = 0: '))
pergunta3 = int(input('Mora perto da vítima? Sim = 1 ou Não = 0: '))
pergunta4 = int(input('Devia para a vítima? Sim = 1 ou Não = 0: '))
pergunta5 = int(input('Já trabalhou com a vítima? Sim = 1 ou Não = 0: '))

crime = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]

if(sum(crime) > 1 and sum(crime) <= 2):
    print(interrogado, 'você é uma pessoa Suspeita do crime.')
elif(sum(crime) > 2 and sum(crime) <= 4):
    print(interrogado, 'você é Cúmplice do crime.')
elif(sum(crime) == 5):
    print(interrogado, 'você é o Assassino, está preso.')
else:
    print(interrogado, 'você é uma pessoa Inocente.')
