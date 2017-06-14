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


def valida_outros(variavel, qtd_letras):
    import re
    variavel = re.sub("[a-z,A-Z]", "", variavel)
    if len(variavel) == qtd_letras:
        return True
    else:
        return False


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
	cpf=list(cpf)

	for a in range(len(cpf)):
		cpf[a]=int(cpf[a])
	
	mult=[10, 9, 8, 7, 6, 5, 4, 3, 2] #Lista para multiplicar com os 9 primeiros digitos do cpf
	mult2=[11, 10, 9, 8, 7, 6, 5, 4, 3, 2] #Lista para multiplicar com os 10 primeiros digitos do cpf
	
	soma=0
	soma2=0

	for a in range(len(mult)):
		soma += cpf[a] * mult[a]
	#print(soma) #Para retornar o valor da soma antes da divisao
	d1=11-(soma%11)
	if d1 == 10 or d1 == 11: #Se a soma dos digitos der 10 ou 11 a funcao retornara um 0 ao d1
		d1=0
	cpf.append(d1) #caso o usuario digite o CPF completo sem o decimo e decimo primeiro digito do cpf retire o # no inicio de cpf.append

	for a in range(len(mult2)):
		soma2 += cpf[a] * mult2[a]
	#print(soma2) #Para retornar o valor da soma antes da divisao
	d2=11-(soma2%11)
	if d2 == 10 or d2 == 11: #Se a soma dos digitos der 10 ou 11 a funcao retornara um 0 ao d2
		d2=0
	cpf.append(d2) #caso o usuario digite o CPF completo sem o decimo e decimo primeiro digito do cpf retire o # no inicio de cpf.append

	if d1 == cpf[9] and d2 == cpf[10]:
		return True
	else:
		return False


def validaEmail(email):
    if len(email) > 11 and (email.find("@") != -1) and (email.find(".") != -1):
        return True
    else:
        return False


def pesquisar(termo):
    puxarDados()
    for i in dados_Users:
        if termo.upper() in dados_Users[i][0].upper():
            print(dados_Users[i])
