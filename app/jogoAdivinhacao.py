# trata-se da implementação de um jogo de adivinhação, tipo forca

# importando a biblioteca para checagem de números
import checkNumbers

# obtem a palavra secreta do jogador 1
palavra_secreta = 'panela'.upper()

# inicializando a lista com as letras já selecionadas
digitadas = []

# inicializando a lista com as letras acertadas
acertadas = []

# definindo o número de chances permitidas
chances = 3

# laço infinito de execução do jogo
while True:

    # se não existirem mais chances:
    if chances <= 0:

        # envia a mensagem
        print('Você perdeu!!!')
        print()

        # encerra o jogo
        break

    # obtem a sugestão de letra
    letra = input('Digite uma letra: ').upper()

    # validando a entrada da sugestão de letra
    # se o tamanho for maior que 1
    if len(letra) > 1:

        # envia mensagem
        print('Digite apenas uma letra.')
        print()

        # passa para a próxima iteração
        continue

    # se for número
    if checkNumbers.is_number(letra):

        # envia mensagem
        print('Digite apenas letras.')
        print()

        # passa para a próxima iteração
        continue

    # se já estiver sido digitada
    if letra in digitadas:
        # envia mensagem
        print('Esta letra já foi digitada anteriormente.')
        print()

        # passa para a próxima iteração
        continue

    # populando a lista de letras digitadas
    digitadas.append(letra)

    # se a letra existir na palavra secreta
    if letra in palavra_secreta:

        # envia mensagem
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')

        # populando a lista de letras acertadas
        acertadas.append(letra)

    # senão
    else:

        # envia mensagem
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')

        # decrementa as chances
        chances -= 1

        # envia mensagem
        print(f'Você ainda tem {chances} chances.')

    # inicializando a exibição da palavra secreta parcial
    secreto_temporario = ''

    # iterando sobre a palavra secreta
    for letra_secreta in palavra_secreta:

        # se a letra atual tiver sido selecionada
        if letra_secreta in acertadas:

            # exibe a letra
            secreto_temporario += letra_secreta

        # senão
        else:

            # exibe um *
            secreto_temporario += '*'

    # se a palavra secreta parcial corresponder a palavra secreta
    if secreto_temporario == palavra_secreta:

        # envia mensagem
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        print('')

        # encerra o jogo
        break

    # senão
    else:

        # exibe a palavra secreta parcial
        print(f'A palavra secreta está assim: {secreto_temporario}')
        print('')

    # exibe uma linha em branco para a próxima iteração
    print()
