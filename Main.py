#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import User as U
import Veiculos as V

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

        Nome_User = input("Nome: ")
        U.valName(Nome_User, "Nome")

        Sobrenome_User = input("Sobrenome: ")
        U.valName(Sobrenome_User, "Sobrenome")

        dataN = input("Digite a data de nascimento (dd/mm/aaaa): ")
        while U.valDate(dataN) is False:
            dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")

        CPF = input("CPF: ")
        U.valCpf(CPF)

        Nome_Mae = input("Nome da Mãe: ")
        U.valName(Nome_Mae, "Nome")

        RG = input("RG: ")
        while U.valOthers(RG, 9) is False:
            RG = input("RG Inválido!\nDigite outro RG: ")

        Email = input("Email:")
        U.valEmail(Email)

        CNH = input("CNH: ")
        while U.valOthers(CNH, 10) is False:
            CNH = input("CNH Inválida!\nDigite outra CNH: ")

        Endereco = input("Endereço, no formato (Rua, Número, Cidade-Estado): ")
        U.valAddress(Endereco)

        Fone = input("Telefone (xx)xxxxx-xxxx: ")
        U.valFone(Fone)

        U.newUsuario(Nome_User, Sobrenome_User, dataN, CPF, Nome_Mae, RG, Email, CNH, Endereco, Fone, "0")
        print("Cadastro efetuado com sucesso!")
    elif op == '2':
        termo = input("Digite o CPF do cliente que deseja buscar: ")
        U.search(termo)
    elif op == '3':
        editar = input("Digite o CPF do cliente que deseja editar: ")
        U.checkUserExist(editar)
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

        op = input("Qual campo deseja alterar? ")

        if op == '1':
            Nome_User = input("Digite o novo nome: ")
            U.valName(Nome_User, "Nome")
            U.editUser(editar, Nome_User, op)
        elif op == '2':
            Sobrenome_User = input("Digite o novo sobrenome: ")
            U.valName(Sobrenome_User, "Sobrenome")
            U.editUser(editar, Sobrenome_User, op)
        elif op == '3':
            dataN = input("Digite a nova data de nascimento (dd/mm/aaaa): ")
            while U.valDate(dataN) is False:
                dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")
            U.editUser(editar, dataN, op)
        elif op == '4':
            CPF = input("Digite o novo CPF: ")
            while U.valCpf(CPF) is False:
                CPF = input("CPF Inválido!\nDigite outro CPF: ")
            U.editUser(editar, CPF, op)
        elif op == '5':
            Nome_Mae = input("Digite o novo nome da Mãe: ")
            U.valName(Nome_Mae, "Nome")
            U.editUser(editar, Nome_Mae, op)
        elif op == '6':
            RG = input("RG: ")
            while U.valOthers(RG, 9) is False:
                RG = input("RG Inválido!\nDigite outro RG: ")
            U.editUser(editar, RG, op)
        elif op == '7':
            Email = input("Email:")
            U.valEmail(Email)
            U.editUser(editar, Email, op)
        elif op == '8':
            CNH = input("CNH: ")
            while U.valOthers(CNH, 10) is False:
                CNH = input("CNH Inválida!\nDigite outra CNH: ")
            U.editUser(editar, CNH, op)
        elif op == '9':
            Endereco = input("Endereço, no formato (Rua, Número, Cidade-Estado): ")
            U.valAddress(Endereco)
            U.editUser(editar, Endereco, op)
        elif op == '10':
            Fone = input("Telefone (xx)xxxxx-xxxx: ")
            U.valFone(Fone)
            U.editUser(editar, Fone, 10)
        elif op == '0':
            break
        else:
            print("Opcao invalida!")
    elif op == '4':
        optDel = input("Qual o CPF do usuário?")
        U.deleteUser(optDel)
    elif op == '5':
        cpfUser = input("Digite o CPF do usuário que deseja alugar o carro: ")
        while V.CheckExist(cpfUser, U.dataUser) is False:
            cpfUser = input("CPF não encontrado!\nDigite o CPF do usuário que deseja alugar o carro: ")

        plateCar = input("Digite a placa do carro á ser alugado: ")
        while V.CheckExist(plateCar, V.dados_Veiculos) is False:
            plateCar = input("Placa não encontrada!\nDigite o CPF do usuário que deseja alugar o carro: ")

        V.calendarShow()
        date = input("Data de entrega[dd/mm/aaaa]: ")
        while V.valDate(date) == False:
            date = input("Data Inválida! Data de entrega[dd/mm/aaaa]: ")
        date2 = V.todayDate()
        price = V.diff_days(date) * int(V.dados_Veiculos[plateCar][3])

        print("O preço do aluguel é", price)
        cont = input("Continuar?")

        if cont.upper() == "S":
            pay = input("Pagamento á vista? (S/n)")
            if pay.upper() == "S":
                price = 0
            U.dataUser[cpfUser][10] += 1
            V.dados_Veiculos[plateCar][7] += 1
            V.veiculos_alugados[U.dataUser[cpfUser][3]] = V.dados_Veiculos[plateCar][:], price
            V.dados_Veiculos.pop(plateCar)
            print(V.veiculos_alugados)
    elif op == '7':
        j = 1
        for i in V.dados_Veiculos:
            print('\t', j, '-', V.dados_Veiculos[i][0])
            j += 1
    elif op == '9':
        op = ""
        while op != '10':
            V.pullData(V.DB_Veiculos, V.dados_Veiculos)
            print("/// MENU DE VEÍCULOS")
            print("1 - Cadastrar veículos")
            print("2 - Editar veículos")
            print("3 - Excluir veículos")
            print("0 - Voltar")
            op = input("Digite uma opção do menu acima: ")

            if op == '1':
                Car_Model = input("Qual o modelo do veículo? ")
                V.valModel(Car_Model)
                Car_Color = input("Qual a cor do veículo? ")
                V.valColor(Car_Color)
                Car_Year = input("Qual o ano do veículo? ")
                V.valYear(Car_Year)
                Car_Price = input("Qual o preço do veículo no formato '000' ou '0000'? ")
                V.valPrice(Car_Price)
                Car_Plate = input("Qual a placa de veículo no formato 'XXX-0000'? ")
                V.valPlate(Car_Plate)
                Car_Renavam = input("Qual o número renavam do veículo? ")
                V.valRenaban(Car_Year, Car_Renavam)
                Car_KM = input("Digite os quilômetros rodados do veículo no formato '000000': ")
                V.valKM(Car_KM)
                V.newCar(Car_Model, Car_Color, Car_Year, Car_Price, Car_Plate, Car_Renavam, Car_KM, 0)
                print("Cadastro efetuado com sucesso!")

            elif op == '2':
                editar = input("Digite a placa do veículo que deseja modificar cadastro no foramto 'XXX-0000': ")
                V.checkCarExist(editar)
                print("O que deseja alterar?")
                print("1 - Cor do veículo")
                print("2 - Preço do aluguel")
                print("3 - Quilômetros rodados do veículo")
                print("0 - Voltar")

                op = int(input("Qual campo deseja alterar? "))

                if op == 1:
                    Car_Color = input("Qual a cor do veículo? ")
                    V.valColor(Car_Color)
                    V.carEdit(editar, Car_Color, 2)
                elif op == 2:
                    Car_Price = input("Qual o preço do veículo no formato '000.00' ou '0000.00'? ")
                    V.valPrice(Car_Price)
                    V.carEdit(editar, Car_Price, 4)
                elif op == 3:
                    Car_KM = input("Digite os quilômetros rodados do veículo no formato '000000': ")
                    V.valKM(Car_KM)
                    V.carEdit(editar, Car_KM, 7)
                elif op == 0:
                    break
                else:
                    print("Opcao invalida!")

            elif op == '3':
                optDel = input(
                    "Informe a placa do veículo que deseja excluir do banco de dados no formato 'XXX-0000': ")
                V.deleteCar(optDel)

            elif op == '4':
                break

            else:
                print("OPÇÃO INVÁLIDA!")
    elif op == '10':
        op = ""
        while op != '0':
            V.pullData(V.DB_Veiculos_alugados, V.veiculos_alugados)
            V.pullData(V.DB_Veiculos, V.dados_Veiculos)
            print("///MENU DE HISTÓRICOS")
            print("1 - Consultar histórico das locações efetuadas")
            print("2 - Consultar quais os veículos mais locados")
            print("3 - Consultar os melhores clientes")
            print("4 - Consultar relatórios de locações em um determinado período")
            print("0 - Voltar")
            op = int(input("\n\nDigite uma opção do menu acima: "))

            if op == '1':
                V.CarsAlugados()
            elif op == '3':
                U.bestClients()
            elif op == '0':
                break
            else:
                print("OPÇÃO INVÁLIDA!")
            voltar = input("Aperte Enter para continuar...")
    elif op == '0':
        break
    else:
        print("OPÇÃO INVÁLIDA!")
    voltar = input("Aperte Enter para continuar...")
    print("\n" * 30)
