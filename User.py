import re
from datetime import datetime

dados_Users = {}
DB = 'DB_User.dat'


# Ações de dados
def puxarDados():
    try:
        Arquivo = open(DB, 'r+')
        Linha = Arquivo.readline()
        tam = len(dados_Users)
        while Linha:
            read = Linha.split('|')
            dados_Users[tam] = read[0], read[1], read[2], read[3], read[4], read[5], read[6], read[7], read[8], read[9]
            Linha = Arquivo.readline()
        Arquivo.close()
    except:
        print('Não existe Dados')


class newUsuario(object):
    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        dados_Users[len(dados_Users)] = a, b, c, d, e, f, g, h, i, j


def getNome(i):
    return dados_Users[i][0]


def getSobrenome(i):
    return dados_Users[i][1]


def getDataNasc(i):
    return dados_Users[i][2]


def getCpf(i):
    return dados_Users[i][3]


def getNomeMae(i):
    return dados_Users[i][4]


def getRG(i):
    return dados_Users[i][5]


def getEmail(i):
    return dados_Users[i][6]


def getCnh(i):
    return dados_Users[i][7]


def getEndereco(i):
    return dados_Users[i][8]


def getTelefone(i):
    return dados_Users[i][9]


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
    if 12 == (10 or 11):
        d2 = 0
    cpf.append(d2)

    return bool(d1 == cpf[9] and d2 == cpf[10])


def valida_outros(variavel, qtd_letras):
    variavel = re.sub('[a-z,A-Z]', '', variavel)
    return bool(len(variavel) == qtd_letras)


def validaEndereco(m):
    while bool(re.match('[A-Za-z0-9ãõẽíóáç .,º ]{5,25}', m)) is False:
        m = input('Endereço Inválido!\nDigite um novo endereço: ')


def validaFone(m):
    while bool(re.match('^\([1-9]{2}\) [2-9]{2,3}[0-9]{2}\-[0-9]{4}$', m)) is False:
        m = input('Número errado!\nDigite outro número: ')


def validaEmail(email):
    while bool(re.match('[a-z0-9\-\_\.]+\@[\w\-\_\.]+[a-z]{2,4}', email)) is False:
        email = input('Email Inválido!\nDigite outro email: ')


def validNomeSobrenome(m, n):
    while bool(re.match('[a-zA-Zãõçóúáé ]{2,}', m)) is False:
        m = input(n + ' Inválido!\nDigite outro ' + n + ': ')


def validData(m):
    try:
        data = m.split('/')
        dia = data[0]
        mes = data[1]
        ano = data[2]
        nas = datetime(int(ano), int(mes), int(dia))
        return True
    except:
        return False


# Pesquisa
def pesquisar(termo):
    for i in dados_Users:
        if termo.upper() in getNome(i).upper():
            print(dados_Users[i])


def mostrarUsers():
    for i in range(len(dados_Users)):
        print(i + 1, ' - ', dados_Users[i][0], dados_Users[i][1])


# Ediçao de cadastro
def salvarDados():
    for i in range(len(dados_Users)):
        with open(DB, 'a+') as Arquivo:
            Arquivo.writelines(
                getNome(i) + '|' + getSobrenome(i) + '|' + getDataNasc(i) + '|' + getCpf(i) + '|' + getNomeMae(
                    i) + '|' +
                getRG(i) + '|' + getEmail(i) + '|' + getCnh(i) + '|' + getEndereco(i) + '|' + getTelefone(i) + '|\n')
    Arquivo.close()


def editUser(m, n, v):
    dados_Users[int(m) - 1][v - 1] = n
    salvarDados()


def removerUser(opt):
    dados_Users.pop([opt - 1])
    salvarDados()


def sendEmail():
    import smtplib

    # Informe suas credenciais abaixo.
    remetente = 'seuemailaqui@gmail.com'
    senha = 'suasenhaaqui'

    # Destinatario e informações da mensagem.
    destinatario = 'email@destinatario.com'
    assunto = 'Enviando email com python'
    texto = 'Esse email foi enviado usando python! :)'

    # Preparando a mensagem
    msg = '\r\n'.join([
        'From: %s' % remetente,
        'To: %s' % destinatario,
        'Subject: %s' % assunto,
        '',
        '%s' % texto
    ])

    # Enviando o email SMTP esta configurado para o remetete usar Gmail.
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(remetente, senha)
    server.sendmail(remetente, destinatario, msg)
    server.quit()
