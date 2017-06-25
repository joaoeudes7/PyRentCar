#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import time

dataUser = {}
DB = 'DB_User.dat'


# Acesso aos dados
def pullData():
    with open(DB, 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            dataUser[read[3]] = read[:]

def saveData():
    conteudo = ''
    with open(DB, 'a+') as arquivo:
        for i in dataUser:
            for k in range(len(dataUser[i])):
                conteudo += dataUser[i][k] + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()

# Validando
def cpfExistente(m):
    return bool(m in dataUser)


def valCpf(cpf):
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


def valOthers(variavel, qtd_letras):
    variavel = re.sub('[a-z,A-Z]', '', variavel)
    return bool(len(variavel) == qtd_letras)


def valAddress(m):
    while bool(re.match('[A-Za-z0-9ãõẽíóáç .,º' ']{5,25}', m)) is False:
        m = input('Endereço Inválido!\nDigite um novo endereço, no formato (Rua, Número, Cidade-Estado): ')


def valFone(m):
    while bool(re.match('^\([1-9]{2}\) [2-9]{2,3}[0-9]{2}\-[0-9]{4}$', m)) is False:
        m = input('Número errado!\nDigite outro número: ')


def valEmail(email):
    while bool(re.match('[a-z0-9\-\_\.]+\@[\w\-\_\.]+[a-z]{2,4}', email)) is False:
        email = input('Email Inválido!\nDigite outro email: ')


def valName(m, n):
    while bool(re.match('[a-zA-Zãõçóúáéí ]{2,}', m)) is False:
        m = input(n + ' Inválido!\nDigite outro ' + n + ': ')


def valDate(m):
    try:
        date = time.strptime(m, '%d/%m/%Y')
        return bool(date.tm_year <= (int(time.strftime("%Y")) - 18))
    except:
        return False


# Pesquisa
def search(term):
    for i in dataUser:
        if term.upper() in dataUser[i][0].upper():
            print(dataUser[i])


def showUsers():
    for i in dataUser:
        print(i + 1, ' - ', dataUser[i][0], dataUser[i][1])

# Ediçao de cadastro
def checkUserExist(m):
    while bool(m not in dataUser) is True:
        m = input('CPF não existe nos registros!\nDigite outro CPF: ')


def deleteUser(m):
    del dataUser[m]
    saveData()


def editCPF(m, n, v):
    dataUser[n] = dataUser[m][:]
    dataUser[m][v - 1] = n
    deleteUser(m)


def editUser(m, n, v):
    dataUser[m][v - 1] = n
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
    def __init__(self, a, b, c, d, e, f, g, h, i, j, l):
        dataUser[d] = [a, b, c, d, e, f, g, h, i, j, l]
        saveData()
