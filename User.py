Dados_users = {}
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

    def SalvarDados(self):
        with open(DB, "a+") as Arquivo:
            Arquivo.write(self.nome + "`" + self.sobrenome + "`" + self.dataNascimento + "`" + self.cpf + "`" + self.nomeMae + "`" + self.rg + "`" + self.email + '`\n')
            Arquivo.close()
    def getNome(self):
        return


def PuxarDados_User():
    try:
        Arquivo = open(DB, 'r+')
        Linha = Arquivo.readline()
        while Linha:
            valores = Linha.split("`")
            nome_no_bd = valores[0].replace(" ","")
            Dados_users[nome_no_bd] =  valores[0],valores[1],valores[2],valores[3],valores[4], valores[5], valores[6]
            Linha = Arquivo.readline()
        Arquivo.close()

    except:
        print("Não existe Dados")


def LimparDados_User():
    Arquivo = open('DB.dat', 'w+')
    Arquivo.writelines("")
    Arquivo.close()
