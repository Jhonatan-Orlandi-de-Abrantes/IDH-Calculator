# Imports/Frameworks
import os, math

# Funções
def pedir_numero(mensagem):
    while True:
        valor = input(mensagem).strip().replace(',', '.')
        try:
            return float(valor)
        except ValueError:
            print('\033[31mDigite apenas números (use vírgula ou ponto para decimais)!\033[m')

def pedir_inteiro(mensagem, opcoes=None):
    while True:
        valor = input(mensagem).strip()
        try:
            num = int(valor)
            if opcoes and num not in opcoes:
                print(f'\033[31mDigite apenas {opcoes}!\033[m')
                continue
            return num
        except ValueError:
            print('\033[31mDigite apenas números inteiros!\033[m')

def forma_de_estudo(escolha):
    global media_anos_de_estudo, expect_anos_estudo
    if escolha == 1:
        media_anos_de_estudo = pedir_numero('Digite a média de anos de estudo do país: \033[33m')
        print('\033[m')
    elif escolha == 2:
        expect_anos_estudo = pedir_numero('Digite a expectativa de anos de estudo do país: \033[33m')
        print('\033[m')

# Código
os.system('cls')
print('Bem vindo ao calculador de IDH! Para isso, responda as seguintes perguntas:')

expect_de_vida = pedir_numero('Digite a expectativa de vida do país: \033[33m')
print('\033[m')

media_anos_de_estudo = 0
expect_anos_estudo = 0

escolha = pedir_inteiro('''Selecione a forma de medida de estudo do seu país digitando seu respectivo número:

\033[33m[1]\033[m Média de anos de estudo
\033[33m[2]\033[m Expectativa de anos de estudo

Resposta: \033[33m''', opcoes=[1, 2])
print('\033[m')
forma_de_estudo(escolha)

RNB = pedir_numero('Digite o número do PIB per capita Ppp do país: \033[33m')
print('\033[m')

# Cálculos
IL = (expect_de_vida - 20) / (85 - 20)
IE_media = (media_anos_de_estudo / 15)
IE_expectativa = (expect_anos_estudo / 18)
IR = ((math.log(RNB) - 4.60) / 6.62)

if escolha == 1:
    multiplicacao = (IL * IE_media * IR)
elif escolha == 2:
    multiplicacao = (IL * IE_expectativa * IR)

IDH = (multiplicacao ** (1/3))
IDH = round(IDH, 3)
IDH = str(IDH).replace('.', ',')

print(f'O IDH desse país é: \033[34m{IDH}\033[m')

input('Pressione ENTER para fechar o código.')