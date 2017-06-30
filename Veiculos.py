#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import calendar
import re
from datetime import datetime

dados_Veiculos = {}
veiculos_alugados = {}
DB_Veiculos = "DB_Veiculos.dat"
DB_Veiculos_alugados = "DB_Veiculos_alugados.dat"


def saveData(db, lista):
    conteudo = ''
    with open(db, 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in lista:
            for k in range(len(lista[i])):
                conteudo += str(lista[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()


def pullData(db, lista):
    with open(db, 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read[7] = int(read[7])
            read[8] = int(read[8])
            read.pop(len(read) - 1)
            lista[read[4]] = read[:]


def pullDataAlugados():
    with open(DB_Veiculos_alugados, 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            veiculos_alugados[read[4]] = read[:]

def CarsAlugados():
    j = 1
    print("Carros alugados:")
    # Disponível para alugar
    for i in dados_Veiculos:
        print(j, "-", veiculos_alugados[i][0])
        j += 1


def showCars():
    j = 1
    print("Carros disponíveis:")
    # Disponível para alugar
    for i in dados_Veiculos:
        print(j, "-", dados_Veiculos[i][0])
        j += 1


def rentCar():
    showCars()
    print("\n0 - Nenhum")
    escolha_d_carro = int(input("Qual Carro quer alugar?"))
    if escolha_d_carro != 0:
        print("Você irá alugar o veículo:\n", dados_Veiculos[escolha_d_carro - 1], "\n")
        cont = input("Continuar? (S/n)").upper()
        if cont == "S":
            veiculos_alugados = dados_Veiculos[escolha_d_carro - 1][:]
            dados_Veiculos.pop(escolha_d_carro - 1)


def search(term):
    pullData(DB_Veiculos, dados_Veiculos)
    for i in dados_Veiculos:
        if term.upper() in dados_Veiculos[i][0].upper():
            print(dados_Veiculos[i])


# VALIDAÇÕES
def valModel(m):
    while bool(re.match('[a-zA-Z0-9çãõẽéêíóá .,' ']{2,30}', m)) is False:
        m = input("Modelo de veículo inválido!\nDigite um modelo válido: ")


def valColor(c):
    while bool(re.match('[a-zA-Z .' ']{4,8}', c)) is False:
        c = input("Cor inválida!\nDigite uma cor válida: ")


def valYear(y):
    while bool(re.match('[1-2][0-9][0-9][0-9]', y)) is False:
        y = input("Ano inválido!\nDigite um ano válido: ")


def valPrice(p):
    while bool(re.match('[0-9]{2,5}', p)) is False:
        p = input("Preço inválido!\nDigite um preço válido no formato '000' ou '0000': ")


def OthrsExist(m):
    return not bool(m in dados_Veiculos)


def CheckExist(m, v):
    return bool(m in v)


def valDate(m):
    if (re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}', m)):
        m = datetime.strptime(m, "%d/%m/%Y")
        d = datetime.strptime(todayDate(), "%d/%m/%Y")
        if m > d:
            return True
        else:
            return False
    else:
        return False


def valPlate(m):
    while bool((re.match("^\w{3}-\d{4}$", m) and OthrsExist(m))) is False:
        m = input("Placa do veículo inválida!\nDigite a placa do carro no formato 'XXX-0000': ")


def valRenaban(a, t):
    while bool((int(a) < 2013 and len(t) == 9) or (int(a) >= 2013 and len(t) == 11)) is False:
        t = input("Número renavam inválido!\nDigite um número renavam válido: ")


def valKM(km):
    while bool(re.match('[0-9]{1,6}', km)) is False:
        km = input("Quilometragem inválida!\nDigite uma quilometragem válida no formato '000000': ")


def diff_days2(data):
    data2 = datetime.now().date()
    data = datetime.strptime(data, "%d/%m/%Y").date()
    dif = data2 - data
    dif = dif.days
    return int(dif)


def diff_days(data):
    data2 = datetime.now().date()
    data = datetime.strptime(data, "%d/%m/%Y").date()
    dif = data - data2
    dif = dif.days
    return int(dif)


def todayDate():
    now = datetime.now()
    return ("%s/%s/%s" % (now.day, now.month, now.year))

def calendarShow():
    now = datetime.now()
    cal = calendar.month(now.year, now.month)
    print("Aqui está o calendário:")
    print(cal)


class newCar(object):
    def __init__(self, a, b, c, d, e, f, g, h, i):
        dados_Veiculos[e] = [a, b, c, d, e, f, g, h, i]
        saveData(DB_Veiculos, dados_Veiculos)


# Ediçao de cadastro de carros
def checkCarExist(m):
    while bool(m not in dados_Veiculos) is True:
        m = input("A placa do carro não existe nos registros!\nDigite uma placa válida no formato 'XXX-0000': ")


def carEdit(m, n, v):
    dados_Veiculos[m][v - 1] = n
    saveData(DB_Veiculos, dados_Veiculos)


def deleteCar(m):
    del dados_Veiculos[m]
    saveData(DB_Veiculos, dados_Veiculos)

def bestCars():
    melhoresCli = {}
    for i in dados_Veiculos:
        if dados_Veiculos[i][7] != 0:
            melhoresCli[len(melhoresCli)] = dados_Veiculos[i][0], dados_Veiculos[i][7]
    melhoresCli = sorted(melhoresCli.values(), reverse=True)[:]

    print("///Nome do carro/Quantidade de alugueis:")
    for i in melhoresCli:
        print("\t", i[0], " | ", i[1])