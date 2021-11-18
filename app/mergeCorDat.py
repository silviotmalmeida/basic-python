# importando as dependências
import os

# envia mensagem de início
print('Iniciando...')

# definindo a localização deste arquivo python
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# abrindo o arquivo CHESF para leitura
fileIn = open(os.path.join(__location__, 'corCHESF.dat'))

# armazenando o conteúdo do arquivo em um array
lines = fileIn.readlines()

# inicializando o array de cores
colors = []

# inicializando o dicionário de cada cor
color = {}

# iterando sobre as linhas do arquivo
for line in lines:

    # separando os dados em um array chave valor
    data = line.split('=')

    # se a chave for ID
    if data[0].strip() == 'ID':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for ORDEM
    if data[0].strip() == 'ORDEM':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR_PERCENT_R
    if data[0].strip() == 'COR_PERCENT_R':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR_PERCENT_G
    if data[0].strip() == 'COR_PERCENT_G':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR_PERCENT_B
    if data[0].strip() == 'COR_PERCENT_B':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for BLINK
    if data[0].strip() == 'BLINK':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR_BLINK
    if data[0].strip() == 'COR_BLINK':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR e o dicionário estiver totalmente populado
    if data[0].strip() == 'COR' and len(color) >= 5:
        # insere a cor no array de cores
        colors.append(color)
        # reinicia o dicionário de cor
        color = {}


# abrindo o arquivo CEPEL para leitura
fileIn = open(os.path.join(__location__, 'corCEPEL.dat'))

# armazenando o conteúdo do arquivo em um array
lines = fileIn.readlines()

# inicializando o dicionário de cada cor
color = {}

# iterando sobre as linhas do arquivo
for line in lines:

    # separando os dados em um array chave valor
    data = line.split('=')

    # se a chave for ID
    if data[0].strip() == 'ID':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for ORDEM
    if data[0].strip() == 'ORDEM':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR_PERCENT_R
    if data[0].strip() == 'COR_PERCENT_R':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR_PERCENT_G
    if data[0].strip() == 'COR_PERCENT_G':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR_PERCENT_B
    if data[0].strip() == 'COR_PERCENT_B':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for BLINK
    if data[0].strip() == 'BLINK':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR_BLINK
    if data[0].strip() == 'COR_BLINK':
        # registra no dicionário
        color[data[0].strip()] = data[1].strip()

    # se a chave for COR e o dicionário estiver totalmente populado
    if data[0].strip() == 'COR' and len(color) >= 5:

        # iterando sobre o array de cores
        for c in colors:

            # se o ID da cor já existir
            if c.get('ID') == color['ID']:
                # quebra o laço e não insere esta cor no array de cores
                break

        # se o loop varreu o array até o final sem quebrar
        else:
            # insere a cor no array de cores
            colors.append(color)
            # reinicia o dicionário de cor
            color = {}

# abrindo o arquivo MERGE para escrita
fileOut = open(os.path.join(__location__, 'corMERGE.dat'), 'w+')

# iterando sobre o array de cores
for c in colors:

    # escrevendo no arquivo
    fileOut.write('COR\n')
    fileOut.write(f'ID = {c.get("ID")}\n')
    fileOut.write(f'ORDEM = {c.get("ORDEM")}\n')
    fileOut.write(f'COR_PERCENT_R = {c.get("COR_PERCENT_R")}\n')
    fileOut.write(f'COR_PERCENT_G = {c.get("COR_PERCENT_G")}\n')
    fileOut.write(f'COR_PERCENT_B = {c.get("COR_PERCENT_B")}\n')

    # se a chave BLINK existir
    if c.get("BLINK") is not None:
        # escreve no arquivo
        fileOut.write(f'BLINK = {c.get("BLINK")}\n')

    # se a chave COR_BLINK existir
    if c.get("COR_BLINK") is not None:
        # escreve no arquivo
        fileOut.write(f'COR_BLINK = {c.get("COR_BLINK")}\n')

    fileOut.write('\n')

# envia mensagem de sucesso
print('Concluído')
