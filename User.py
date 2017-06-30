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
            read[10] = int(read[10])
            dataUser[read[3]] = read[:]

def saveData():
    conteudo = ''
    with open(DB, 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in dataUser:
            for k in range(len(dataUser[i])):
                conteudo += str(dataUser[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)

# Validando
def cpfExistente(m):
    return bool(m in dataUser)


def valCpf(cpf):
    while cpfExistente(cpf) is True:
        cpf = input("CPF já utilizado!\nDigite outro:")
        if len(cpf) != 11:
            return False
        else:
            if not re.match("[0-9]", cpf):
                return False
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
            return bool(d1 == cpf[9] and d2 == cpf[10])


def valOthers(variavel, qtd_letras):
    return bool(re.match("[0-9]{"+str(qtd_letras)+"}", variavel))


def valAddress(m):
    while bool(re.match('[A-Za-z0-9ãõẽíóáç .,º' ']{5,25}', m)) is False:
        m = input('Endereço Inválido!\nDigite um novo endereço, no formato (Rua, Número, Cidade-Estado): ')


def valFone(m):
    while bool(re.match('^\([1-9]{2}\)[2-9]{2,3}[0-9]{2}\-[0-9]{4}$', m)) is False:
        m = input('Número errado!\nDigite outro número: ')


def valEmail(email):
    while bool(re.match('[a-z0-9\-\_\.]+\@[\w\-\_\.]+[a-z]{2,4}', email)) is False:
        email = input('Email Inválido!\nDigite outro email: ')


def valName(m, n):
    while bool(re.match('[^0-9][a-zA-Zãõçóúáéí ]{2,}', m)) is False:
        m = input(n + ' Inválido!\nDigite outro ' + n + ': ')


def valDate(m):
    try:
        date = time.strptime(m, '%d/%m/%Y')
        return bool(date.tm_year <= (int(time.strftime("%Y")) - 18))
    except:
        return False


def bestClients():
    melhoresCli = {}
    for i in dataUser:
        if dataUser[i][10] != 0:
            melhoresCli[len(melhoresCli)] = dataUser[i][0], dataUser[i][10]
    melhoresCli = sorted(melhoresCli.values(), reverse=True)[:]

    print("///Nome do cliente/Quantidade de alugueis:")
    for i in melhoresCli:
        print("\t", i[0], " | ", i[1])

# Pesquisa
def search(term):
    if term in dataUser:
        print(dataUser[term])
    else:
        print("Usuário não existe!")


def showUsers():
    j = 1
    for i in dataUser:
        print(j, ' - ', dataUser[i][0], dataUser[i][1])
        j += 1
# Ediçao de cadastro
def checkUserExist(m):
    while bool(m not in dataUser) is True:
        m = input('CPF não existe nos registros!\nDigite outro CPF: ')

def deleteUser(m):
    del dataUser[m]
    saveData()
    print("Cadastro excluído com sucesso!")

def editCPF(m, n, v):
    dataUser[n] = dataUser[m][:]
    dataUser[m][v - 1] = n
    deleteUser(m)


def editUser(m, n, v):
    dataUser[m][int(v) - 1] = n
    saveData()


def sendEmail(email, cpf, nameCar, price, today, dateReceive, by):

    import smtplib

    # Informe suas credenciais abaixo.
    remetente = "contato.pyrentacar@gmail.com"
    senha = "Pyrentacar2017"

    # Destinatario e informações da mensagem.
    destinatario = email
    assunto = 'Confirmação de ' + by
    if by == "Aluguel":
        texto = "Olá, " + dataUser[cpf][
            0] + "\nVocê alugou o veículo " + nameCar + " na data de hoje (" + today + "), com prazo de entrega até o dia " + dateReceive + ".\nValor a ser pago na devolução do veículo: R$" + str(
            price) + " reais.\nAgradecemos a preferência."
    else:
        texto = "Olá, " + dataUser[cpf][
            0] + "\nAviso de devoloção do veículo " + nameCar + "!\nAgradecemos a preferência."

    # Preparando a mensagem
    msg = '\r\n'.join([
        'From: %s' % remetente,
        'To: %s' % destinatario,
        'Subject: %s' % assunto,
        '',
        '%s' % texto
    ])
    try:
        # Enviando o email SMTP esta configurado para o remetete usar Gmail.
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.encode('utf-8'))
        server.quit()
    except:
        print("Erro ao enviar o email!\nVerifique sua conexão com a internet ou o email do usuário se está correto!")

class newUsuario(object):
    def __init__(self, a, b, c, d, e, f, g, h, i, j, l):
        dataUser[d] = [a, b, c, d, e, f, g, h, i, j, l]
        saveData()
