dados_Veiculos = {}
veiculos_alugados = {}
DB_Veiculos = "DB_Veiculos.dat"
DB_Veiculos_alugados = "DB_Veiculos_alugados.dat"

class newCarro(object):
    def __init__(self, nome_veiculo, cor_veiculo, ano_veiculo, preco_veiculo, placa_veiculo, renavam_veiculo,
                 km_rodados):
        self.nome_veiculo = nome_veiculo
        self.ano_veiculo = ano_veiculo
        self.preco_veiculo = preco_veiculo
        self.cor_veiculo = cor_veiculo
        self.placa_veiculo = placa_veiculo
        self.renavam_veiculo = renavam_veiculo
        self.km_rodados = km_rodados

    def salvarDados(self):
        with open(DB_Veiculos, "a+") as Arquivo:
            Arquivo.write(self.nome_veiculo + "|" + self.cor_veiculo + "|" + self.ano_veiculo + "|" + self.placa_veiculo + "|" + self.renavam_veiculo + "|" + self.preco_veiculo + "|" + self.km_rodados + "|\n")
            Arquivo.close()


def limparDados():
    Arquivo = open(DB_Veiculos, 'w+')
    Arquivo.writelines("")
    Arquivo.close()


def puxarDados(DB):
    try:
        Arquivo = open(DB, 'r+')
        Linha = Arquivo.readline()
        while Linha:
            valores = Linha.split("|")
            dados_Veiculos[len(dados_Veiculos)] = valores[0], valores[1], valores[2], valores[3], valores[4], valores[5], valores[6]
            Linha = Arquivo.readline()
        Arquivo.close()
    except:
        print("Não existe Dados")

def alugar():
    puxarDados(DB_Veiculos)
    j = 1
    print("Carros disponíveis:")
    for i in dados_Veiculos:
        print(j,"-",dados_Veiculos[i][0])
        j += 1
    print("\n0 - Nenhum")
    escolha_d_carro = int(input("Qual Carro quer alugar?"))
    if escolha_d_carro != 0:
        cont = input("Você irá alugar o veículo:\n",dados_Veiculos[escolha_d_carro-1],"\n Continuar? (S/n)").upper()
        if cont == "S":
            veiculos_alugados = dados_Veiculos[escolha_d_carro - 1][:]
            dados_Veiculos.pop(escolha_d_carro - 1)

def pesquisar(termo):
    puxarDados()
    for i in dados_Veiculos:
        if termo.upper() in dados_Veiculos[i][0].upper():
            print(dados_Veiculos[i])


#VALIDAÇÕES

def validaRenavam(ano, renavam):
    renavam = list(renavam)
    renavam = len(renavam)

    if ano < 2013 and renavam == 9 or ano >= 2013 and renavam == 11:
        return True
    else:
        return False