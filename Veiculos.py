import re

dados_Veiculos = {}
veiculos_alugados = {}
DB_Veiculos = "DB_Veiculos.dat"
DB_Veiculos_alugados = "DB_Veiculos_alugados.dat"

class newCar(object):
    def __init__(self, a, b, c, d, e, f, g):
        dados_Veiculos[len(dados_Veiculos)] = [a, b, c, d, e, f, g]


def saveData():
    conteudo = ''
    Arquivo = open(DB_Veiculos, 'a+')
    for i in range(len(dados_Veiculos)):
        conteudo += dados_Veiculos[i][0] + '|' + dados_Veiculos[i][1] + '|' + dados_Veiculos[i][2] + '|' + dados_Veiculos[i][3] + '|' + \
                    dados_Veiculos[i][4] + '|' + dados_Veiculos[i][5] + '|' + dados_Veiculos[i][6] + '|\n'
    Arquivo.writelines(conteudo)
    Arquivo.close()


def pushData(db, lista):
    try:
        with open(db, 'r+') as Arquivo:
            Linha = Arquivo.readline()
            while Linha:
                valores = Linha.split("|")
                lista[len(dados_Veiculos)] = valores[0], valores[1], valores[2], valores[3], valores[4], valores[5], \
                                             valores[6]
                Linha = Arquivo.readline()
            Arquivo.close()
    except:
        print("Não existe Dados")


def showCars():
    pushData(DB_Veiculos, dados_Veiculos)
    j = 1
    print("Carros disponíveis:")
    # Disponível para alugar
    for i in dados_Veiculos:
        print(j,"-",dados_Veiculos[i][0])
        j += 1


def rentCar():
    showCars()
    print("\n0 - Nenhum")
    escolha_d_carro = int(input("Qual Carro quer alugar?"))
    if escolha_d_carro != 0:
        print("Você irá alugar o veículo:\n", dados_Veiculos[escolha_d_carro - 1], "\n")
        cont = input("Continuar? (S/n)").upper()
        if cont == "S":
            veiculos_alugados = dados_Veiculos[escolha_d_carro - 1][:]
            dados_Veiculos.pop(escolha_d_carro - 1)


def search(term):
    pushData(DB_Veiculos, dados_Veiculos)
    for i in dados_Veiculos:
        if term.upper() in dados_Veiculos[i][0].upper():
            print(dados_Veiculos[i])

#VALIDAÇÕES
def valModel(m):
    while bool(re.match('[a-zA-Z0-9çãõẽéêíóá .,' ']{2,30}', m)) is False:
        m = input("Modelo de veículo inválido!\nDigite um modelo válido: ")

def valColor(c):
    while bool(re.match('[a-zA-Z .' ']{4,8}', c)) is False:
        c = input("Cor inválida!\nDigite uma cor válida: ")

def valYear(y):
    while bool(re.match('[1-2][0-9][0-9][0-9]', y)) is False:
        y = input("Ano inválido!\nDigite um ano válido: ")

def valPrice(p):
    while bool(re.match('[0-9,.]{6,8}', p)) is False:
        p = input("Preço inválido!\nDigite um preço válido no formato '000,00' ou '0.000,00': ")


def valPlate(m):
    while bool(re.match("^\w{3}-\d{4}$", m)) is False:
        m = input("Placa do veículo inválida!\nDigite a placa do carro no formato 'XXX-0000': ")


def valRenaban(a, t):
    while bool((int(a) < 2013 and len(t) == 9) or (int(a) >= 2013 and len(t) == 11)) is False:
        t = input("Número renavam inválido!\nDigite um número renavam válido: ")

def valKM(km):
    while bool(re.match('[0-9]{6}', km)) is False:
        km = input("Quilometragem inválida!\nDigite uma quilometragem válida no formato '000000': ")