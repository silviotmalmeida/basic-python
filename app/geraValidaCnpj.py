# trata-se da implementação de um validador de CNPJ

# importando a biblioteca para checagem de números
import checkNumbers

# importando o gerador de números aleatórios
from random import randint


# função que formata os números do CNPJ com a máscara padrão
def formata_cnpj(cnpj):
    return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:142]}'


# função que calcula os dígitos verificadores do cnpj
def calcula_digito_verificador_cnpj(cnpj, digito: int):

    # se o argumento digito for 1 ou 2, prossegue:
    if digito == 1 or digito == 2:

        # iniciando o acumulador
        soma = 0

        # iniciando o multiplicador
        # será 5 para o primeiro dígito verificador e 6 para o segundo dígito verificador
        multiplicador = 5 if (digito == 1) else 6

        # iniciando o cnpj
        # terá os 12 primeiros dígitos para o primeiro dígito verificador e 13 para o segundo dígito verificador
        cnpj_parcial = cnpj[0:12] if (digito == 1) else cnpj[0:13]

        # iterando sobre os dígitos
        for digito in cnpj_parcial:

            # incrementando o acumulador com o produto do dígito e multiplicador
            soma += int(digito) * multiplicador

            # decrementando o multiplicador para a próxima iteração
            multiplicador -= 1

            # quando o multiplicador for igual a 1, reseta para 9
            multiplicador = 9 if (multiplicador == 1) else multiplicador

        # calculando o dígito verificador
        digito_verificador = (11 - (soma % 11))

        # se o resultado for maior que 9, iguala a zero
        digito_verificador = 0 if (
            digito_verificador > 9) else digito_verificador

        # retornando o dígito verificador
        return digito_verificador

    # senão
    else:
        # envia mensagem e encerra o programa
        print('O argumento digito deve ser 1 ou 2')
        print()
        exit()


if __name__ == '__main__':

    while(True):

        # pergunta o cnpj ao usuário
        opcao = input(
            'Selecione 1 para gerar e 2 para validar CNPJ. Ou 0 para sair: ')

        if opcao == '0':
            print('Encerrando programa')
            print()
            break

        if opcao == '1':

            # laço para gerar aleatoriamente os doze primeiros dígitos do CNPJ
            while True:
                # obtendo os doze primeiros dígitos do CNPJ para calcular os demais
                # inicializando o CNPJ vazio
                cnpj = ''

                # laço para popular os doze primeiros dígitos
                for x in range(8):
                    # populando aleatoriamente os doze primeiros dígitos
                    cnpj += str(randint(0, 9))

                # se nao for repetição
                if not checkNumbers.is_sequence(cnpj):
                    # sai do laço
                    break

            # inserindo os digitos 0001
            cnpj = cnpj + '0001'

            # calculando o primeiro dígito verificador
            primeiro_digito = calcula_digito_verificador_cnpj(cnpj, 1)

            # inserindo o primeiro dígito verificador
            cnpj_gerado = cnpj + str(primeiro_digito)

            # calculando o segundo dígito verificador
            segundo_digito = calcula_digito_verificador_cnpj(cnpj_gerado, 2)

            # inserindo o segundo dígito verificador
            cnpj_gerado += str(segundo_digito)

            # envia CNPJ gerado
            print(formata_cnpj(cnpj_gerado))
            print('')

        elif opcao == '2':
            # pergunta o cnpj ao usuário
            cnpj = input('Digite o CNPJ: ')

            # removendo os caracteres não numéricos
            cnpj = checkNumbers.only_numbers(cnpj)

            # validando a entrada
            # se o tamanho for igual a 14
            if not checkNumbers.exact_lenght(cnpj, 14):

                # envia mensagem
                print('O CNPJ deve conter 14 números')
                print()
                exit()

            # se for número
            if not checkNumbers.is_number(cnpj):

                # envia mensagem
                print('Digite apenas números.')
                print()
                exit()

            # se for repetição
            if checkNumbers.is_sequence(cnpj):

                # envia mensagem de erro
                print(f'CNPJ {formata_cnpj(cnpj)} NÃO é válido!')
                print()
                exit()

            # calculando o primeiro dígito verificador
            primeiro_digito = calcula_digito_verificador_cnpj(cnpj, 1)

            # calculando o segundo dígito verificador
            segundo_digito = calcula_digito_verificador_cnpj(cnpj, 2)

            # montando o cnpj para validação
            cnpj_montado = cnpj[0:12]
            cnpj_montado += str(primeiro_digito)
            cnpj_montado += str(segundo_digito)

            # se o CNPJ for igual ao CNPJ montado
            if cnpj == cnpj_montado:

                # envia mensagem de sucesso
                print(f'CNPJ {formata_cnpj(cnpj)} é válido!')
                print('')

            # senão
            else:

                # envia mensagem de erro
                print(f'CNPJ {formata_cnpj(cnpj)} NÃO é válido!')
                print('')

        else:
            print('Opção Inválida')
            print()
