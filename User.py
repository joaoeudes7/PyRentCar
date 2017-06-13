dados_Users = {}
DB = "DB_User.dat"


class newUsuario(object):
    def __init__(self, nome, sobrenome, dataNascimento, cpf, nomeMae, rg, email, habilitacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dataNascimento = dataNascimento
        self.cpf = cpf
        self.nomeMae = nomeMae
        self.rg = rg
        self.email = email
        self.habilitacao = habilitacao

    pass

    def salvarDados(self):
        with open(DB, "a+") as Arquivo:
            Arquivo.write(
                self.nome + "|" + self.sobrenome + "|" + self.dataNascimento + "|" + self.cpf + "|" + self.nomeMae + "|" + self.rg + "|" + self.email + "|" + self.habilitacao + '|\n')
            Arquivo.close()


def valida_outros(variavel, qtd_letras, txt):
    import re
    while True:
        variavel = input(txt + ":")
        variavel = re.sub("[a-z,A-Z]", "", variavel)
        if len(variavel) == qtd_letras:
            print(variavel)
            break
        else:
            print(txt, "Inválido, digite novamente!")


def puxarDados():
    try:
        Arquivo = open(DB, 'r+')
        Linha = Arquivo.readline()
        while Linha:
            valores = Linha.split("|")
            dados_Users[len(dados_Users)] = valores[0], valores[1], valores[2], valores[3], valores[4], valores[5], \
                                            valores[
                                                6], valores[7]
            Linha = Arquivo.readline()
        Arquivo.close()
    except:
        print("Não existe Dados")


def limparDados_User():
    Arquivo = open(DB, 'w+')
    Arquivo.writelines("")
    Arquivo.close()


# Validando

def val_cpf(cpf):
    soma2, soma1 = 0, 0
    tam = 10
    if len(cpf) != 11:
        return False
    else:
        for j in range(2):
            soma2 = soma1
            soma1 = 0
            for i in range(tam - 1):
                soma1 += int(cpf[i]) * tam
                tam -= 1
            tam = 11
        result1 = 11 - (soma2 % 11)
        result2 = 11 - (soma1 % 11)
        d1 = int(cpf[9])
        d2 = int(cpf[10])

        if cpf[2] == cpf[4] == cpf[9]:
            return False
        else:
            if (d1 == result1) or ((result1 == (10 or 11)) and 0 == d1):
                if (d2 == result2) or ((result2 == (10 or 11)) and 0 == d2):
                    return True
            else:
                return False


def validaEmail(email):
    if len(email) > 11 and (email.find("@") != -1) and (email.find(".") != -1):
        return True
    else:
        return False


def validaRenavam(ano, renavam):
    renavam = list(renavam)
    renavam = len(renavam)

    if ano < 2013 and renavam == 9 or ano >= 2013 and renavam == 11:
        return True
    else:
        return False


def pesquisar(termo):
    puxarDados()
    for i in dados_Users:
        if termo.upper() in dados_Users[i][0].upper():
            print(dados_Users[i])
