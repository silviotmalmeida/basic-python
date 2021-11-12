# trata-se da implementação de um gerador de CPF

# importando o gerador de números aleatórios
from random import randint

# laço para evitar geracao de números repetidos
while True:
    # obtendo os nove primeiros dígitos do CPF para calcular os demais
    cpf = str(randint(100000000, 999999999))
    
    # se for repetição
    if not cpf == (cpf[0] * 11):
        break

# se for repetição
if cpf == (cpf[0] * 11):
    
    # envia mensagem de erro
    print(f'CPF {cpf} NÃO é válido!')
    print()
    exit()

# laço para cálculo do primeiro dígito
# iniciando o acumulador
soma = 0

# iniciando o multiplicador
multiplicador = 10

# iterando sobre os nove primeiros dígitos
for digito in cpf:
    
    # incrementando o acumulador com o produto do dígito e multiplicador
    soma += int(digito) * multiplicador
    
    # decrementando o multiplicador para a próxima iteração
    multiplicador -= 1
    
# calculando o primeiro dígito
primeiro_digito = (11 - (soma % 11))

# se o resultado for maior que 9, iguala a zero
primeiro_digito = 0 if (primeiro_digito > 9) else primeiro_digito

# inserindo o dígito ao cpf validado
cpf += str(primeiro_digito)

# laço para cálculo do segundo dígito
# iniciando o acumulador
soma = 0

# iniciando o multiplicador
multiplicador = 11

# iterando sobre o cpf validado
for digito in cpf:
    
    # incrementando o acumulador com o produto do dígito e multiplicador
    soma += int(digito) * multiplicador
    
    # decrementando o multiplicador para a próxima iteração
    multiplicador -= 1

# calculando o segundo dígito
segundo_digito = (11 - (soma % 11))

# se o resultado for maior que 9, iguala a zero
segundo_digito = 0 if (segundo_digito > 9) else segundo_digito

# inserindo o dígito ao cpf validado
cpf += str(segundo_digito)

# envia o CPF gerado
print(f'CPF gerado: {cpf}')
print('')