# trata-se da implementação de um validador de CPF

# importando a biblioteca para checagem de números
import checkNumbers

# obtem a sugestão de letra
cpf = input('Digite o CPF sem pontos ou traço: ')

# validando a entrada
# se o tamanho for maior que 1
if len(cpf) != 11:
    
    # envia mensagem
    print('O CPF deve conter 11 números')
    print()
    exit()

# se for número
if not checkNumbers.is_number(cpf):
    
    # envia mensagem
    print('Digite apenas números.')
    print()
    exit()
    
# se conter traço
if '-' in cpf:
    
    # envia mensagem
    print('Digite apenas números.')
    print()
    exit()
    
# se conter ponto
if '.' in cpf:
    
    # envia mensagem
    print('Digite apenas números.')
    print()
    exit()
    
# se for repetição
if cpf == (cpf[0] * 11):
    
    # envia mensagem de erro
    print(f'CPF {cpf} NÃO é válido!')
    print()
    exit()

# obtendo os nove primeiros dígitos do CPF para calcular os demais
cpf_validado = cpf[0:9]

# laço para cálculo do primeiro dígito
# iniciando o acumulador
soma = 0

# iniciando o multiplicador
multiplicador = 10

# iterando sobre os nove primeiros dígitos
for digito in cpf_validado:
    
    # incrementando o acumulador com o produto do dígito e multiplicador
    soma += int(digito) * multiplicador
    
    # decrementando o multiplicador para a próxima iteração
    multiplicador -= 1
    
# calculando o primeiro dígito
primeiro_digito = (11 - (soma % 11))

# se o resultado for maior que 9, iguala a zero
primeiro_digito = 0 if (primeiro_digito > 9) else primeiro_digito

# inserindo o dígito ao cpf validado
cpf_validado += str(primeiro_digito)

# laço para cálculo do segundo dígito
# iniciando o acumulador
soma = 0

# iniciando o multiplicador
multiplicador = 11

# iterando sobre o cpf validado
for digito in cpf_validado:
    
    # incrementando o acumulador com o produto do dígito e multiplicador
    soma += int(digito) * multiplicador
    
    # decrementando o multiplicador para a próxima iteração
    multiplicador -= 1

# calculando o segundo dígito
segundo_digito = (11 - (soma % 11))

# se o resultado for maior que 9, iguala a zero
segundo_digito = 0 if (segundo_digito > 9) else segundo_digito

# inserindo o dígito ao cpf validado
cpf_validado += str(segundo_digito)

# se o cpf fpr igual ao cpf validado
if cpf == cpf_validado:
    
    # envia mensagem de sucesso
    print(f'CPF {cpf} é válido!')
    print('')

# senão
else:
    
    # envia mensagem de erro
    print(f'CPF {cpf} NÃO é válido!')
    print('')