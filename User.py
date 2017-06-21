import re
import time

dateUser = {}
DB = 'DB_User.dat'


# Ações de dados
def pullData():
    try:
        with open(DB, 'r+') as Arquivo:
            Linha = Arquivo.readline()
            while Linha:
                read = Linha.split('|')
                tam = len(dateUser)
                dateUser[tam] = read[0], read[1], read[2], read[3], read[4], read[5], read[6], read[7], read[8], read[9]
                Linha = Arquivo.readline()
            print(dateUser)
    except:
        print('Não existe Dados')

# Validando
def cpfExistente(m):
    for i in range(len(dateUser)):
        return bool(dateUser[i][3] == m)


def validCpf(cpf):
    pullData()
    while cpfExistente(cpf) == True:
        cpf = input("CPF já utilizado!\nDigite outro:")
    cpf = list(cpf)
    for a in range(len(cpf)):
        cpf[a] = int(cpf[a])

    mult = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    mult2 = [11] + mult

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

    if d2 == 10 or d2 == 11:
        d2 = 0
    cpf.append(d2)

    while bool(d1 == cpf[9] and d2 == cpf[10]) is False:
        cpf = input("CPF Inválido!\nDigite outro CPF: ")


def validOthers(variavel, qtd_letras):
    variavel = re.sub('[a-z,A-Z]', '', variavel)
    return bool(len(variavel) == qtd_letras)


def validAddress(m):
    while bool(re.match('[A-Za-z0-9ãõẽíóáç .,º' ']{5,25}', m)) is False:
        m = input('Endereço Inválido!\nDigite um novo endereço, no formato (Rua, Número, Cidade-Estado): ')


def validFone(m):
    while bool(re.match('^\([1-9]{2}\) [2-9]{2,3}[0-9]{2}\-[0-9]{4}$', m)) is False:
        m = input('Número errado!\nDigite outro número: ')


def validEmail(email):
    while bool(re.match('[a-z0-9\-\_\.]+\@[\w\-\_\.]+[a-z]{2,4}', email)) is False:
        email = input('Email Inválido!\nDigite outro email: ')


def validName(m, n):
    while bool(re.match('[a-zA-Zãõçóúáéí ]{2,}', m)) is False:
        m = input(n + ' Inválido!\nDigite outro ' + n + ': ')


def validDate(m):
    try:
        date = time.strptime(m, '%d/%m/%Y')
        return bool(date.tm_year <= (int(time.strftime("%Y")) - 18))
    except:
        return False


# Pesquisa
def search(term):
    for i in dateUser:
        if term.upper() in dateUser[i][0].upper():
            print(dateUser[i])


def showUsers():
    for i in range(len(dateUser)):
        print(i + 1, ' - ', dateUser[i][0], dateUser[i][1])


# Ediçao de cadastro
def saveData():
    conteudo = ''
    with open(DB, 'a+') as arquivo:
        for i in range(len(dateUser)):
            conteudo += dateUser[i][0] + '|' + dateUser[i][1] + '|' + dateUser[i][2] + '|' + dateUser[i][3] + '|' + \
                        dateUser[i][4] + '|' + dateUser[i][5] + '|' + dateUser[i][6] + '|' + dateUser[i][7] + '|' + \
                        dateUser[i][8] + '|' + dateUser[i][9] + '|\n'
        arquivo.writelines(conteudo)

def editUser(m, n, v):
    dateUser[int(m) - 1][v - 1] = n
    saveData()


def deleteUser(opt):
    dateUser.pop([opt - 1])
    saveData()


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


class newUsuario(object):
    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        dateUser[len(dateUser)] = [a, b, c, d, e, f, g, h, i, j]
