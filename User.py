import re
from datetime import datetime

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
    check = re.match("[a-z0-9\-\_\.]+\@[\w\-\_\.]+[a-z]{2,4}", email)
    if check:
        return True
    else:
        return False


def validNomeSobrenome(m):
    if (len(m) <= 3) or re.search("\d+", m):
        return False
    else:
        return True


def validData(m):
    try:
        data = m.split("/")
        dia = data[0]
        mes = data[1]
        ano = data[2]
        nas = datetime(int(ano), int(mes), int(dia))
        return True
    except:
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


def sendEmail():
    import smtplib

    # Informe suas credenciais abaixo.
    remetente = "seuemailaqui@gmail.com"
    senha = "suasenhaaqui"

    # Destinatario e informações da mensagem.
    destinatario = "email@destinatario.com"
    assunto = "Enviando email com python"
    texto = "Esse email foi enviado usando python! :)"

    # Preparando a mensagem
    msg = '\r\n'.join([
        'From: %s' % remetente,
        'To: %s' % destinatario,
        'Subject: %s' % assunto,
        '',
        '%s' % texto
    ])

    # Enviando o email SMTP esta configurado para o remetete usar Gmail.
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(remetente, senha)
    server.sendmail(remetente, destinatario, msg)
    server.quit()
