
import os
import pyfiglet 
from colorama import Back, Fore, init

init(autoreset=True)


# Limpa o terminal de acordo com o sistema operacional
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

texto_formatado = pyfiglet.figlet_format("Calculadora de Quebra", font="slant", width=200)
print(texto_formatado)
# Exibe a tela inicial do programa
def tela_inicial():
    print(Fore.YELLOW + '-=-' * 30)

    print(' Este programa serve para facilitar o seu cálculo de quebra de pallets.')
    input(' Pressione Enter para continuarmos... ')
    limpar_tela()


# Executa os cálculos e controla o fluxo principal do programa
def logica():
    # Fatores utilizados nos cálculos
    PANO_FATOR = 280
    CAIXA_FATOR = 20

    while True:
        print(Fore.YELLOW + '-=-' * 23)

        try:
            # Recebe a quantidade de panos
            quebra_panos = int(
                input('Digite a quantidade de panos: ')
            )

            # Recebe a quantidade de caixas
            quebra_caixas = int(
                input('Digite a quantidade de caixas (20 un. cada): ')
            )

            # Realiza os cálculos
            total_panos = quebra_panos * PANO_FATOR
            total_caixas = quebra_caixas * CAIXA_FATOR
            total_geral = total_panos + total_caixas

            # Exibe o resultado do cálculo
            print(Fore.GREEN + '\n--- RESULTADO DA QUEBRA ---')
            print(
                Fore.GREEN
                + f'• Panos: {quebra_panos} x {PANO_FATOR} = {total_panos} unidades'
            )
            print(
                Fore.GREEN
                + f'• Caixas: {quebra_caixas} x {CAIXA_FATOR} = {total_caixas}'
                ' unidades'
            )
            print(
                Fore.YELLOW
                + f'TOTAL GERAL DA QUEBRA: {total_geral} unidades no total.\n'
            )

        # Trata entradas que não podem ser convertidas para número inteiro
        except ValueError:
            print(
                Fore.RED
                + 'Erro: Por favor, digite apenas números inteiros válidos.\n'
            )
            continue

        # Pergunta se o usuário deseja realizar outro cálculo
        continuar = (
            input(Fore.CYAN + 'Deseja calcular outro quebra ? [s/n]: ')
            .strip()
            .lower()
        )

        if continuar != 's':
            break

        limpar_tela()


# Exibe a mensagem de encerramento
def tela_final():
    limpar_tela()
    print(Fore.YELLOW + '-=-' * 23)
    print(Back.LIGHTBLACK_EX + ' Obrigado por usar o nosso programa! ')
    input(Back.LIGHTBLACK_EX + ' Pressione ENTER para encerrar... ')
    limpar_tela()


# Inicia o programa
if __name__ == '__main__':
    tela_inicial()
    logica()
    tela_final()
