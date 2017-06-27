#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import User
import Veiculos

# ############################
# 		PY RENT A CAR 		##
# Create by:                ##
#         Bruno and João    ##
###############################

op = ''

while op != 10:
    User.pullData()
    Veiculos.pullData(Veiculos.DB_Veiculos, Veiculos.dados_Veiculos)
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

    op = int(input("// Digite uma opção do menu acima: "))
    if op == 1:

        Nome_User = input("Nome: ")
        User.valName(Nome_User, "Nome")

        Sobrenome_User = input("Sobrenome: ")
        User.valName(Sobrenome_User, "Sobrenome")

        dataN = input("Digite a data de nascimento (dd/mm/aaaa): ")
        while User.valDate(dataN) is False:
            dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")

        CPF = input("CPF: ")
        User.valCpf(CPF)

        Nome_Mae = input("Nome da Mãe: ")
        User.valName(Nome_Mae, "Nome")

        RG = input("RG: ")
        while User.valOthers(RG, 9) is False:
            RG = input("RG Inválido!\nDigite outro RG: ")

        Email = input("Email:")
        User.valEmail(Email)

        CNH = input("CNH: ")
        while User.valOthers(CNH, 10) is False:
            CNH = input("CNH Inválida!\nDigite outra CNH: ")

        Endereco = input("Endereço, no formato (Rua, Número, Cidade-Estado): ")
        User.valAddress(Endereco)

        Fone = input("Telefone (xx)xxxxx-xxxx: ")
        User.valFone(Fone)

        User.newUsuario(Nome_User, Sobrenome_User, dataN, CPF, Nome_Mae, RG, Email, CNH, Endereco, Fone, "0")
    elif op == 2:
        while True:
            termo = input("Digite o nome do cliente: ")
            User.search(termo)
    elif op == 3:
        editar = input("Digite o CPF do cliente que deseja editar: ")
        User.checkUserExist(editar)
        print("O que deseja alterar?")
        print("1 - Nome")
        print("2 - Sobrenome")
        print("3 - Data de nascimento")
        print("4 - CPF")
        print("5 - Nome da mãe")
        print("6 - RG")
        print("7 - Email")
        print("8 - Habilitação")
        print("9 - Endereço")
        print("10 - Telefone")
        print("0 - Voltar")

        op = int(input("Qual campo deseja alterar? "))

        if op == 1:
            Nome_User = input("Digite o novo nome: ")
            User.valName(Nome_User, "Nome")
            User.editUser(editar, Nome_User, op)
        elif op == 2:
            Sobrenome_User = input("Digite o novo sobrenome: ")
            User.valName(Sobrenome_User, "Sobrenome")
            User.editUser(editar, Sobrenome_User, op)
        elif op == 3:
            dataN = input("Digite a nova data de nascimento (dd/mm/aaaa): ")
            while User.valDate(dataN) is False:
                dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")
            User.editUser(editar, dataN, op)
        elif op == 4:
            CPF = input("Digite o novo CPF: ")
            while User.valCpf(CPF) is False:
                CPF = input("CPF Inválido!\nDigite outro CPF: ")
            User.editUser(editar, CPF, op)
        elif op == 5:
            Nome_Mae = input("Digite o novo nome da Mãe: ")
            User.valName(Nome_Mae, "Nome")
            User.editUser(editar, Nome_Mae, op)
        elif op == 6:
            RG = input("RG: ")
            while User.valOthers(RG, 9) is False:
                RG = input("RG Inválido!\nDigite outro RG: ")
            User.editUser(editar, RG, op)
        elif op == 7:
            Email = input("Email:")
            User.valEmail(Email)
            User.editUser(editar, Email, op)
        elif op == 8:
            CNH = input("CNH: ")
            while User.valOthers(CNH, 10) is False:
                CNH = input("CNH Inválida!\nDigite outra CNH: ")
            User.editUser(editar, CNH, op)
        elif op == 9:
            Endereco = input("Endereço, no formato (Rua, Número, Cidade-Estado): ")
            User.valAddress(Endereco)
            User.editUser(editar, Endereco, op)
        if op == 10:
            op = 11
        elif op == 11:
            Fone = input("Telefone (xx)xxxxx-xxxx: ")
            User.valFone(Fone)
            User.editUser(editar, Fone, 10)
        elif op == 0:
            break
        else:
            print("Opcao invalida!")
    elif op == 4:
        optDel = input("Qual o CPF do usuário?")
        User.deleteUser(optDel)
    elif op == 5:
        cpfUser = input("Digite o CPF do usuário que deseja alugar o carro: ")
        plateCar = input("Digite a placa do carro á ser alugado: ")
        User.dataUser[cpfUser][10] += 1
        Veiculos.dados_Veiculos[plateCar][7] += 1
        Veiculos.veiculos_alugados[User.dataUser[cpfUser][4]] = Veiculos.dados_Veiculos[plateCar], 1,
        Veiculos.dados_Veiculos.pop(plateCar)

        print(Veiculos.veiculos_alugados)
    elif op == 7:
        j = 1
        for i in Veiculos.dados_Veiculos:
            print('\t', j, '-', Veiculos.dados_Veiculos[i][0])
            j += 1
        voltar = input("Aperte Enter para continuar...")
    elif op == 9:
        op = ""
        while op != 10:
            Veiculos.pullData(Veiculos.DB_Veiculos, Veiculos.dados_Veiculos)
            print("/// MENU DE VEÍCULOS")
            print("1 - Cadastrar veículos")
            print("2 - Editar veículos")
            print("3 - Excluir veículos")
            print("0 - Voltar")
            op = int(input("Digite uma opção do menu acima: "))

            if op == 1:
                Car_Model = input("Qual o modelo do veículo? ")
                Veiculos.valModel(Car_Model)
                Car_Color = input("Qual a cor do veículo? ")
                Veiculos.valColor(Car_Color)
                Car_Year = input("Qual o ano do veículo? ")
                Veiculos.valYear(Car_Year)
                Car_Price = input("Qual o preço do veículo no formato '000,00' ou '0.000,00'? ")
                Veiculos.valPrice(Car_Price)
                Car_Plate = input("Qual a placa de veículo no formato 'XXX-0000'? ")
                Veiculos.valPlate(Car_Plate)
                Car_Renavam = input("Qual o número renavam do veículo? ")
                Veiculos.valRenaban(Car_Year, Car_Renavam)
                Car_KM = input("Digite os quilômetros rodados do veículo no formato '000000': ")
                Veiculos.valKM(Car_KM)
                Veiculos.newCar(Car_Model, Car_Color, Car_Year, Car_Price, Car_Plate, Car_Renavam, Car_KM, 0)

            elif op == 2:
                editar = input("Digite a placa do veículo que deseja modificar cadastro no foramto 'XXX-0000': ")
                Veiculos.checkCarExist(editar)
                print("O que deseja alterar?")
                print("1 - Cor do veículo")
                print("2 - Preço do aluguel")
                print("3 - Quilômetros rodados do veículo")
                print("0 - Voltar")

                op = int(input("Qual campo deseja alterar? "))

                if op == 1:
                    Car_Color = input("Qual a cor do veículo? ")
                    Veiculos.valColor(Car_Color)
                    Veiculos.carEdit(editar, Car_Color, op)
                elif op == 2:
                    Car_Price = input("Qual o preço do veículo no formato '000,00' ou '0.000,00'? ")
                    Veiculos.valPrice(Car_Price)
                    Veiculos.carEdit(editar, Car_Price, op)
                elif op == 3:
                    Car_KM = input("Digite os quilômetros rodados do veículo no formato '000000': ")
                    Veiculos.valKM(Car_KM)
                    Veiculos.carEdit(editar, Car_KM, op)
                elif op == 0:
                    break
                else:
                    print("Opcao invalida!")

            elif op == 3:
                optDel = input(
                    "Informe a placa do veículo que deseja excluir do banco de dados no formato 'XXX-0000': ")
                Veiculos.deleteCar(optDel)

            elif op == 0:
                break

            else:
                print("OPÇÃO INVÁLIDA!")
    elif op == 10:
        op = ""
        while op != 0:
            Veiculos.pullData(Veiculos.DB_Veiculos_alugados, Veiculos.veiculos_alugados)
            Veiculos.pullData(Veiculos.DB_Veiculos, Veiculos.dados_Veiculos)
            print("///MENU DE HISTÓRICOS")
            print("1 - Consultar histórico das locações efetuadas")
            print("2 - Consultar quais os veículos mais locados")
            print("3 - Consultar os melhores clientes")
            print("4 - Consultar relatórios de locações em um determinado período")
            print("0 - Voltar")
            op = int(input("\n\nDigite uma opção do menu acima: "))

            if op == 1:
                Veiculos.CarsAlugados()
            elif op == 3:
                User.bestClients()
            elif op == 0:
                break
            else:
                print("OPÇÃO INVÁLIDA!")
    elif op == 0:
        break
    else:
        print("OPÇÃO INVÁLIDA!")
