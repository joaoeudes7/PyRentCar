#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functions import *

# ############################
# 		PY RENT A CAR 		##
# Create by:                ##
#         Bruno and João    ##
###############################

op = ''

while op != '20':
    U.pullData()
    V.pullData(V.DB_Veiculos, V.dados_Veiculos)
    print('/// MENU DE CADASTRAMENTO')
    print('1 - Cadastrar novo cliente')
    print('2 - Consultar cliente existente')
    print('3 - Atualizar cadastro de cliente')
    print('4 - Excluir cadastro de cliente')
    print('\n/// MENU DE LOCAÇÃO')
    print('5 - Alugar veículos')
    print('6 - Devolução de veículos')
    print('7 - Consultar veículos disponíveis')
    print('8 - Consultar registro de empréstimos efetuados')
    print('9 - Menu de veículos')
    print('\n/// MENU DE HISTÓRICOS')
    print('10 - Consultar históricos da empresa')
    print('\n0 - Sair\n\n')
    op = input("// Digite uma opção do menu acima: ")

    if op == '1':
        menuOp1()
    elif op == '2':
        menuOp2()
    elif op == '3':
        menuOp3()
    elif op == '4':
        menuOp4()
    elif op == '5':
        menuOp5()
    elif op == '7':
        menuOp7()
    elif op == '9':
        menuOp9()
    elif op == '10':
        menuOp10()
    elif op == '0':
        break
    else:
        print("OPÇÃO INVÁLIDA!")
    voltar = input("Aperte Enter para continuar...")
    print("\n" * 30)
