 # 5. As Organizações Tabajara resolveram dar um aumento de salário
    # aos seus colaboradores e lhe contrataram para desenvolver o
    # programa que calculará os reajustes.
    # Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    # - salários até R$ 280,00 (incluindo) : aumento de 20%
    # - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    # - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

    # - o salário antes do reajuste;
    # - o percentual de aumento aplicado;
    # - o valor do aumento;
    # - o novo salário, após o aumento.

salario = float(input('Digite o seu salário: '))
cinco = 0.05
dez = 0.1
quinze = 0.15
vinte = 0.20

if (salario <= 280.0):
    reajuste = salario * vinte
    print('Salário anterior: %s ' %salario)
    print('Percentual de aumento: %s ' %(vinte * 100),'%')
    print('Aumento: %s ' %reajuste)
    print('Novo salário: %s ' %(salario + reajuste))
elif (salario > 280.0 and salario < 700):
    reajuste = salario * quinze
    print('Salário anterior: %s ' %salario)
    print('Percentual de aumento: %s ' %(quinze * 100),'%')
    print('Aumento: %s ' %(salario * reajuste))
    print('Novo salário: %s ' %reajuste)
elif (salario > 700.0 and salario < 1500.0):
    reajuste = salario * dez
    print('Salário anterior: %s ' %salario)
    print('Percentual de aumento: %s ' %(dez * 100),'%')
    print("Aumento: %s " %reajuste)
    print('Novo salário: %s ' %(salario + reajuste))
else:
    reajuste = salario * cinco
    print('Salário anterior: %s ' %salario)
    print('Percentual de aumento: %s ' %(cinco * 100),'%')
    print('Aumento: %s ' %reajuste)
    print('Novo salário: %s ' %(salario + reajuste))

