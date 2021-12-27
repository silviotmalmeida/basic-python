# trata-se da implementação de uma calculadora de redes IPV4

# importando a biblioteca de expressões regulares
import re

# importando a biblioteca para checagem de números
import checkNumbers


# classe responsável por obter os dados da rede
class Calculadora_IPv4:
    """
    Faz o cálculo de redes IPv4

    Modo de uso 1:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', prefixo=10)

    Modo de uso 2:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', mascara='255.255.255.0')
    """

    # método construtor
    # precisa receber os argumentos ip e máscara ou prefixo
    def __init__(self, ip, mascara=None, prefixo=None):

        # IP conhecido de um host da rede
        self.ip = ip

        # máscara da rede no formato xxx.xxx.xxx.xxx
        self.mascara = mascara

        # prefixo da rede no formato /xx
        self.prefixo = prefixo

        # se não forem fornecidos a máscara e prefixo, lança uma exceção
        if mascara is None and prefixo is None:
            raise ValueError('Precisa enviar máscara ou prefixo')

        # se forem fornecidos a máscara e prefixo, lança uma exceção
        if mascara and prefixo:
            raise ValueError('Precisa enviar máscara ou prefixo, não ambos.')

        # calculando e setando o ip de broadcast
        self._set_broadcast()

        # calculando e setando o ip de rede
        self._set_rede()

    # implementando o getter do atributo rede
    @property
    def rede(self):
        return self._rede

    # implementando o getter do atributo broadcast
    @property
    def broadcast(self):
        return self._broadcast

    # implementando o getter do atributo numero_ips
    @property
    def numero_ips(self):
        return self._get_numero_ips()

    # implementando o getter do atributo ip
    @property
    def ip(self):
        return self._ip

    # implementando o getter do atributo mascara
    @property
    def mascara(self):
        return self._mascara

    # implementando o getter do atributo prefixo
    @property
    def prefixo(self):
        if self._prefixo is None:
            return

        return self._prefixo

    # implementando o setter do atributo ip
    @ip.setter
    def ip(self, valor):

        # se a validação do formato não for bem sucedida:
        if not self._valida_ip(valor):

            # lança uma exceção
            raise ValueError('IP inválido.')

        # setando o atributo _ip
        self._ip = valor

        # setando o atributo _ip_bin após a conversão de decimal para binário
        self._ip_bin = self._ip_to_bin(valor)

    # implementando o setter do atributo mascara
    @mascara.setter
    def mascara(self, valor):

        # se a mascara não for informada:
        if not valor:

            # encerra a execução do setter
            return

        # se a validação do formato não for bem sucedida:
        if not self._valida_ip(valor):

            # lança uma exceção
            raise ValueError('Máscara inválida.')

        # setando o atributo _mascara
        self._mascara = valor

        # setando o atributo _mascara_bin após a conversão de decimal para binário
        self._mascara_bin = self._ip_to_bin(valor)

        # se o atributo _prefixo ainda não foi setado:
        if not hasattr(self, 'prefixo'):

            # setando o atributo prefixo a partir da contagem de 1 na máscara binária
            self.prefixo = self._mascara_bin.count('1')

    # implementando o setter do atributo prefixo
    @prefixo.setter
    def prefixo(self, valor):

        # se o prefixo não for informado:
        if valor is None:

            # encerra a execução do setter
            return

        # iniciando o tratamento de exceções:
        try:

            # convertendo o valor recebido para inteiro
            valor = int(valor)

        # em caso de falha na conversão:
        except:

            # lança uma exceção
            raise ValueError('Prefixo precisa ser um inteiro.')

        # se o valor recebido for maior que 32 ou menor que zero:
        if valor > 32 or valor < 0:

            # lança uma exceção
            raise TypeError('O prefixo deve ser um inteiro entre 0 e 32.')

        # setando o atributo _prefixo
        self._prefixo = valor

        # setando o atributo _mascara_bin a partir da composição de 1 na quantidade do prefixo e
        # 0 até completar 32 números
        self._mascara_bin = (valor * '1').ljust(32, '0')

        # se o atributo _mascara ainda não foi setado:
        if not hasattr(self, 'mascara'):

            # setando o atributo _mascara após a conversão de binário para decimal
            self.mascara = self._bin_to_ip(self._mascara_bin)

    # implementando o método estático para validação do ip
    @staticmethod
    def _valida_ip(ip):

        # criando a regra para verificar se o ip é formado por 4 blocos de 1 a 3 números, separados por ponto
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        # se a validação do ip recebido for bem sucedida:
        if regexp.search(ip):

            # retorna True
            return True

    # implementando o método estático para conversão do ip decimal para binário
    @staticmethod
    def _ip_to_bin(ip):

        # separando os blocos divididos por .
        blocos = ip.split('.')

        # convertendo cada bloco de decimal para binário
        blocos_bin = [bin(int(bloco))[2:].zfill(8) for bloco in blocos]

        # juntando os blocos em uma única string
        blocos_bin_str = ''.join(blocos_bin)

        # calculando o número de bits
        qtd_bits = len(blocos_bin_str)

        # se a quantidade de bits for maior que 32:
        if qtd_bits > 32:

            # lança uma exceção
            raise ValueError('IP ou máscara tem mais que 32 bits.')

        # retorna o valor em binário sem pontos
        return blocos_bin_str

    # implementando o método estático para conversão do ip binário para decimal
    @staticmethod
    def _bin_to_ip(ip):

        # definindo o número de bits por bloco
        n = 8

        # montando um array com os blocos convertidos para decimal
        blocos = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]

        # retornando os blocos convertidos separados por .
        return '.'.join(blocos)

    # método responsável por calcular o ip de broadcast e popular o atributo _broadcast
    def _set_broadcast(self):

        # calculando a quantidade de bits de host a partir do prefixo
        host_bits = 32 - self.prefixo

        # montando o ip de broadcast binário a partir da composição do ip válido
        # até o tamanho do prefixo e completando os demais bits com 1
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')

        # convertendo o ip de broadcast binário para decimal
        self._broadcast = self._bin_to_ip(self._broadcast_bin)

        # retornando o ip de broadcast em decimal
        return self._broadcast

    # método responsável por calcular o ip de rede e popular o atributo _rede
    def _set_rede(self):

        # calculando a quantidade de bits de host a partir do prefixo
        host_bits = 32 - self.prefixo

        # montando o ip de rede binário a partir da composição do ip válido
        # até o tamanho do prefixo e completando os demais bits com 0
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')

        # convertendo o ip de rede binário para decimal
        self._rede = self._bin_to_ip(self._rede_bin)

        # retornando o ip de rede em decimal
        return self._rede

    # método responsável a quantidade de ips válidos na rede
    def _get_numero_ips(self):

        # retornando o resultado
        return 2 ** (32 - self.prefixo)


# método principal da execução
def main():

    # pergunta o ip válido ao usuário
    ip = input('Digite o IP válido: ')

    # pergunta a máscara ou o prefixo da rede ao usuário
    masc_ou_pref = input('Digite a máscara ou o prefixo da rede: ')

    # se o tamanho da variável masc_ou_pref for igual a 2, entende-se que trata do prefixo
    if len(masc_ou_pref) <= 2:

        # iniciando o tratamento de exceções
        try:
            # instanciando a calculadora com ip e prefixo
            calc_ipv4_1 = Calculadora_IPv4(ip, prefixo=masc_ou_pref)

            # imprimindo os resultados na tela
            print(f'IP: {calc_ipv4_1.ip}')
            print(f'Máscara: {calc_ipv4_1.mascara}')
            print(f'Rede: {calc_ipv4_1.rede}')
            print(f'Broadcast: {calc_ipv4_1.broadcast}')
            print(f'Prefixo: {calc_ipv4_1.prefixo}')
            print(f'Número de IPs da rede: {calc_ipv4_1.numero_ips}')

        # em caso de exceção, envia mensagem e encerra o programa
        except Exception as error:
            print(f"Erro no processamento dos dados: {error}")
            exit()

    # senão, entende-se que trata da máscara
    else:

        # iniciando o tratamento de exceções
        try:
            # instanciando a calculadora com ip e máscara
            calc_ipv4_2 = Calculadora_IPv4(ip, mascara=masc_ou_pref)

            print(f'IP: {calc_ipv4_2.ip}')
            print(f'Máscara: {calc_ipv4_2.mascara}')
            print(f'Rede: {calc_ipv4_2.rede}')
            print(f'Broadcast: {calc_ipv4_2.broadcast}')
            print(f'Prefixo: {calc_ipv4_2.prefixo}')
            print(f'Número de IPs da rede: {calc_ipv4_2.numero_ips}')

        # em caso de exceção, envia mensagem e encerra o programa
        except Exception as error:
            print(f"Erro no processamento dos dados: {error}")
            exit()


if __name__ == '__main__':
    main()
