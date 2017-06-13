__all__ = ["SalvarDados", "PuxarDados", "LimparDados"]

DB = "DB_Veiculos.dat"


class newCarro(object):
    def __init__(self, nome_veiculo, cor_veiculo, ano_veiculo, preco_veiculo, placa, renavam):
        self.nome_veiculo = nome_veiculo
        self.ano_veiculo = ano_veiculo
        self.preco_veiculo = preco_veiculo
        self.cor_veiculo = cor_veiculo
        self.placa_veiculo = placa
        self.renavam_veiculo = renavam

    def SalvarDados(self):
        with open(DB, "a+") as Arquivo:
            Arquivo.write(
                self.nome_veiculo + "`" + self.cor_veiculo + "`" + self.ano_veiculo + "`" + self.placa_veiculo + "`" + self.renavam_veiculo + "`" + self.preco_veiculo + "\n")
            Arquivo.close()


def LimparDados_Veiculos():
    Arquivo = open(DB, 'w+')
    Arquivo.writelines("")
    Arquivo.close()


def PuxarDados_Veiculos():
    Arquivo = open(DB, 'r+')
    Linha = Arquivo.readline()
    while Linha:
        valores = Linha.split("`")
        len(valores)

        print("\nNome:", valores[0],
              "\nCor:", valores[1],
              "\nAno:", valores[2],
              "\nPlaca:", valores[3],
              "\nRenavam:", valores[4],
              "\nPreço do Aluguel:", valores[5] + "\n")
        Linha = Arquivo.readline()
    Arquivo.close()
