import User
import Veiculos

DB = "DB_User.dat"
# ############################
# 		PY RENT A CAR 		##
# Create by:                ##
#         Bruno and João    ##
###############################

op, cnh, rg = '', '', ''

while op != 10:
    User.pushData()
    Veiculos.pushData()
    print('''/// MENU DE CADASTRAMENTO
1 - Cadastrar novo cliente
2 - Consultar cliente existente
3 - Atualizar cadastro de cliente
4 - Excluir cadastro de cliente
\n/// MENU DE LOCAÇÃO
5 - Alugar veículos
6 - Devolução de veículos
7 - Consultar veículos disponíveis
8 - Consultar registro de emprśtimos efetuados
9 - Menu de veículos
\n/// MENU DE HISTÓRICOS
10 - Consultar históricos da empresa
\n0 - Sair\n\n''')

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

        Fone = input("Telefone (xx) xxxxx-xxxx: ")
        User.valFone(Fone)

        User.newUsuario(Nome_User, Sobrenome_User, dataN, CPF, Nome_Mae, RG, Email, CNH, Endereco, Fone)
        User.saveData()
    elif op == 2:

        while True:
            termo = input("Digite o nome do cliente: ")
            User.search(termo)

    elif op == 3:
        User.showUsers()

        editar = input("Qual cliente quer editar?")
        print("O que deseja alterar?")
        print("1 - Nome")
        print("2 - Sobrenome")
        print("3 - Data de nascimento")
        print("4 - CPF")
        print("5 - Nome da mãe")
        print("6 - RG")
        print("7 - Email")
        print("8 - Habilitação")
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
        elif op == 0:
            break
        else:
            print("Opcao invalida!")
    elif op == 4:
        User.showUsers()
        optDel = input("Qual destes quer remover?")
        User.deleteUser(optDel)
    elif op == 9:
        op = ""
        while op != 10:
            print("MENU DE VEÍCULOS")
            print("1 - Cadastrar veículos")
            print("2 - Editar veículos")
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
                Car_Plate = input("Qual a placa de veículo no formato 'XXX0000'? ")
                Veiculos.valPlate(Car_Plate)
                # Validação em Falta
                Car_Renavam = input("Qual o número renavam do veículo? ")
                Veiculos.valRenaban(Car_Year, Car_Renavam)
                # Validação em Falta
                Car_KM = input("Digite os quilômetros rodados do veículo no formato '000000': ")
                Veiculos.valKM(Car_KM)
                Veiculos.newCar(Car_Model, Car_Color, Car_Year, Car_Price, Car_Plate, Car_Renavam, Car_KM)
                Veiculos.saveData()

            elif op == 0:
                print()

            else:
                print("OPÇÃO INVÁLIDA!")

    elif op == 10:
        op = ""
        while op != 10:
            print("MENU DE HISTÓRICOS")
            print("1 - Consultar histórico das locações efetuadas")
            print("2 - Consultar quais os veículos mais locados")
            print("3 - Consultar os melhores clientes")
            print("4 - Consultar relatórios de locações em um determinado período")
            print("0 - Voltar")
            op = int(input("Digite uma opção do menu acima: "))

            if op == 0:
                print()

            else:
                print("OPÇÃO INVÁLIDA!")

    elif op == 0:
        break

    else:
        print("OPÇÃO INVÁLIDA!")
