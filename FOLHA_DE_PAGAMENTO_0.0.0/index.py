 

#valor_hora = float(input('Digite o valor da hora de trabalho (somente numeros): '))
#horas_trabalhadas = float(input('Digite quantas horas trabalhada no mes (somente numeros): '))





# Dados para calculo da folha

salario_bruto = float(input('Digite um salario (somente numeros): ')) # Informar salario

inss_desc = 0  # desconto de inss
porcentagem_inss = 0 # porcentagem aplicada

# descobrindo a aliquota

if salario_bruto > 0 and salario_bruto <= 1302.00:
    inss_desc = 0.075
    porcentagem_inss = '7,5%'

elif salario_bruto > 1302.01 and salario_bruto <= 2571.29:
    inss_desc = 0.09
    porcentagem_inss = '9%'

elif salario_bruto > 2571.30 and salario_bruto <= 3856.94:
    inss_desc = 0.12
    porcentagem_inss = '12%'

else:
    inss_desc = 0.14
    porcentagem_inss = '14%'

valor_inss = salario_bruto * inss_desc # valor do inss dado pelo valor do salario bruto * desconto do inss

base_irrf = salario_bruto - valor_inss # base irrf / ou imposto de renda


# conseguindo o valor da aliquota do imposto de renda

porcentagem_irrf = 0

if base_irrf > 0 and base_irrf <= 1903.98:
    porcentagem_irrf = 0

elif base_irrf > 1903.99 and base_irrf <= 2826.65:
    porcentagem_irrf = 0.075

elif base_irrf > 2826.66 and base_irrf <=  3751.05:
    porcentagem_irrf = 0.15

elif base_irrf > 3751.06 and base_irrf <= 4664.68:
    porcentagem_irrf = 0.225

else:
    porcentagem_irrf = 0.275


salario_liquido = salario_bruto - valor_inss


print(salario_bruto)
print('----------------')
print(porcentagem_inss)
print('----------------')
print(valor_inss)
print('----------------')
print(base_irrf)
print('-----------------')
print(porcentagem_irrf)
print('-----------------')
print(salario_liquido)



