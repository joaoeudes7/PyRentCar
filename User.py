import re

dados_Users = {}
DB = "DB_User.dat"


class newUsuario(object):
    def __init__(self, a, b, c, d, e, f, g, h):
        self.nome = a
        self.sobrenome = b
        self.dataNascimento = c
        self.cpf = d
        self.nomeMae = e
        self.rg = f
        self.email = g
        self.habilitacao = h

    def salvarDados(self):
        with open(DB, "a+") as Arquivo:
            Arquivo.write(
                self.nome + "|" + self.sobrenome + "|" + self.dataNascimento + "|" + self.cpf + "|" + self.nomeMae + "|" + self.rg + "|" + self.email + "|" + self.habilitacao + '|\n')
            Arquivo.close()


# Ações de dados
def puxarDados():
    try:
        Arquivo = open(DB, 'r+')
        Linha = Arquivo.readline()
        while Linha:
            valor = Linha.split("|")
            dados_Users[len(dados_Users)] = valor[0], valor[1], valor[2], valor[3], valor[4], valor[5], valor[6], valor[
                7]
            Linha = Arquivo.readline()
        Arquivo.close()
    except:
        print("Não existe Dados")


def limparDados_User():
    puxarDados()
    Arquivo = open(DB, 'w+')
    Arquivo.writelines("")
    Arquivo.close()


# Validando
def val_cpf(cpf):
    cpf = list(cpf)

    for a in range(len(cpf)):
        cpf[a] = int(cpf[a])

    mult = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    mult2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    soma = 0
    soma2 = 0

    for a in range(len(mult)):
        soma += cpf[a] * mult[a]

    d1 = 11 - (soma % 11)
    if d1 == 10 or d1 == 11:
        d1 = 0
    cpf.append(d1)

    for a in range(len(mult2)):
        soma2 += cpf[a] * mult2[a]
    d2 = 11 - (soma2 % 11)
    if (12 == (10 or 11)):
        d2 = 0
    cpf.append(d2)

    if d1 == cpf[9] and d2 == cpf[10]:
        return True
    else:
        return False


def valida_outros(variavel, qtd_letras):
    variavel = re.sub("[a-z,A-Z]", "", variavel)
    if len(variavel) == qtd_letras:
        return True
    else:
        return False


def validaEmail(email):
    if len(email) > 11 and (email.find("@") != -1) and (email.find(".") != -1):
        return True
    else:
        return False


def validNomeSobrenome(m):
    if (len(m) <= 3) or re.search("\d+", m):
        return False
    else:
        return True


def validData(m):
    data = m.split("/")
    dia = data[0]
    mes = data[1]
    ano = data[2]
    if (2 == (len(dia) and len(mes) and len(ano))) and (0 < dia <= 31) and (0 < mes <= 12) and (1900 < ano):
        return True
    else:
        data = []
        return False

# Pesquisa
def pesquisar(termo):
    puxarDados()
    for i in dados_Users:
        if termo.upper() in dados_Users[i][0].upper():
            print(dados_Users[i])


def mostrarUsers():
    puxarDados()
    for i in range(len(dados_Users)):
        print(i + 1, " - ", dados_Users[i][0], dados_Users[i][1])


# Ediçao de cadastro
def salvarDepois():
    for i in range(len(dados_Users)):
        with open(DB, "a+") as Arquivo:
            Arquivo.writelines(
                dados_Users[i][0] + "|" + dados_Users[i][1] + "|" + dados_Users[i][2] + "|" + dados_Users[i][3] + "|" +
                dados_Users[i][4] + "|" + dados_Users[i][5] + "|" + dados_Users[i][6] + "|" + dados_Users[i][7] + '|\n')
    Arquivo.close()


def removerUser(opt):
    dados_Users.pop([opt - 1])
    salvarDepois()
