nome = "João Eudes"
sobrenome = "Lima"
dataNascimento = "20/09/1997"
cpf = "018.050.254-90"

DB = "DB_User.dat"



class Usuario(object):
    def __init__(self, nome, sobrenome, dataNascimento, cpf, nomeMae, rg, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dataNascimento = dataNascimento.trim()
        self.cpf = cpf.trim()
        self.nomeMae = nomeMae
        self.rg = rg.trim()
        self.email = email.trim()

    def SalvarDados(self):
        with open(DB, "a+") as Arquivo:
            Arquivo.write(
                self.nome + "`" + self.sobrenome + "`" + self.dataNascimento + "`" + self.cpf + "`" + self.nomeMae + "`" + self.rg + "`" + self.email + "\n")
            Arquivo.close()

    def PuxarDados(self):
        Arquivo = open(DB, 'r+')
        Linha = Arquivo.readline()

        while Linha:
            valores = Linha.split("`")
            len(valores)
            print("Nome:", valores[0],
                  "\nSobrenome:", valores[1],
                  "\nData do Nascimento:", valores[2],
                  "\nCPF:", valores[3],
                  "\nNome da Mãe:", valores[4],
                  "\nRG:", valores[5],
                  "\nEmail:", valores[6] + "\n\n")
            Linha = Arquivo.readline()
        Arquivo.close()

    def LimparDados(self):
        Arquivo = open('DB.dat', 'w+')
        Arquivo.writelines("")
        Arquivo.close()
