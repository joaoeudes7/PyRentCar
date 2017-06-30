import User as U
import Veiculos as V

DB = ["DB_Veiculos.dat", "DB_Veiculos_alugados.dat", "DB_Historico.dat", "DB_User.dat"]


def creatFileIfNotExist():
    for i in DB:
        file = open(i, 'a+').close()


def dataPullAll():
    creatFileIfNotExist()
    U.pullData()
    V.pullData()
    V.pullDataAlugados()
    V.pullDataHistorico()


def menuOp1():
    Nome_User = input("Nome: ")
    U.valName(Nome_User, "Nome")

    Sobrenome_User = input("Sobrenome: ")
    U.valName(Sobrenome_User, "Sobrenome")

    dataN = input("Digite a data de nascimento (dd/mm/aaaa): ")
    while U.valDate(dataN) is False:
        dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")

    CPF = input("CPF: ")
    while not U.valCpf(CPF):
        CPF = input("CPF Inválido!\nDigite outro CPF: ")

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

    U.newUsuario(Nome_User, Sobrenome_User, dataN, CPF, Nome_Mae, RG, Email, CNH, Endereco, Fone, 0)
    print("Cadastro efetuado com sucesso!")


def menuOp2():
    termo = input("Digite o CPF do cliente que deseja buscar: ")
    U.search(termo)


def menuOp3():
    cpf = input("Digite o CPF do cliente que deseja editar: ")
    U.checkUserExist(cpf)
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
        U.editUser(cpf, Nome_User, op)
    elif op == '2':
        Sobrenome_User = input("Digite o novo sobrenome: ")
        U.valName(Sobrenome_User, "Sobrenome")
        U.editUser(cpf, Sobrenome_User, op)
    elif op == '3':
        dataN = input("Digite a nova data de nascimento (dd/mm/aaaa): ")
        while U.valDate(dataN) is False:
            dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")
        U.editUser(cpf, dataN, op)
    elif op == '4':
        CPF = input("Digite o novo CPF: ")
        while U.valCpf(CPF) is False:
            CPF = input("CPF Inválido!\nDigite outro CPF: ")
        U.editUser(cpf, CPF, op)
    elif op == '5':
        Nome_Mae = input("Digite o novo nome da Mãe: ")
        U.valName(Nome_Mae, "Nome")
        U.editUser(cpf, Nome_Mae, op)
    elif op == '6':
        RG = input("RG: ")
        while U.valOthers(RG, 9) is False:
            RG = input("RG Inválido!\nDigite outro RG: ")
        U.editUser(cpf, RG, op)
    elif op == '7':
        Email = input("Email:")
        U.valEmail(Email)
        U.editUser(cpf, Email, op)
    elif op == '8':
        CNH = input("CNH: ")
        while U.valOthers(CNH, 10) is False:
            CNH = input("CNH Inválida!\nDigite outra CNH: ")
        U.editUser(cpf, CNH, op)
    elif op == '9':
        Endereco = input("Endereço, no formato (Rua, Número, Cidade-Estado): ")
        U.valAddress(Endereco)
        U.editUser(cpf, Endereco, op)
    elif op == '10':
        Fone = input("Telefone (xx)xxxxx-xxxx: ")
        U.valFone(Fone)
        U.editUser(cpf, Fone, 10)
    else:
        print("Opcao invalida!")
    print("\nModificado com sucesso!\n")


def menuOp4():
    optDel = input("Informe o CPF do usuário que deseja excluir do nosso banco de dados: ")
    U.deleteUser(optDel)


def menuOp5():
    cpfUser = input("Digite o CPF do usuário que deseja alugar o carro: ")
    while V.CheckExist(cpfUser, U.dataUser) is False:
        cpfUser = input("CPF não encontrado!\nDigite o CPF do usuário que deseja alugar o carro: ")

    V.showCars()

    plateCar = input("Digite a placa do carro á ser alugado: ")
    while V.CheckExist(plateCar, V.dados_Veiculos) is False:
        plateCar = input("Placa não encontrada!\nDigite o CPF do usuário que deseja alugar o carro: ")

    if V.dados_Veiculos[plateCar][8] == 0:
        print("Veículo não disponível no momento!\n Status: ALUGADO!")
    else:
        V.calendarShow()

        dateDevolution = input("Data de entrega[dd/mm/aaaa]: ")
        while V.valDate(dateDevolution) == False:
            date = input("Data Inválida! Data de entrega[dd/mm/aaaa]: ")

        price = V.diff_days(dateDevolution) * int(V.dados_Veiculos[plateCar][3])

        print("O preço do aluguel é", price)
        cont = input("Continuar(S/n)? ")

        if cont.upper() == "S":
            pay = input("Pagamento á vista(S/n)? ")

            if pay.upper() == "S":
                price = 0

            U.dataUser[cpfUser][10] += 1
            V.rentCar(plateCar, cpfUser, price, dateDevolution)
            U.saveData()

            email = U.dataUser[cpfUser][6]
            cpf = U.dataUser[cpfUser][3]
            nameCar = V.dados_Veiculos[plateCar][0]
            print("Enviando e-mail de confirmação...")
            U.sendEmail(email, cpf, nameCar, price, V.todayDate(), dateDevolution, "Aluguel")
            V.saveData(V.DB_Veiculos, V.dados_Veiculos)
            print("E-mail enviado!")


def menuOp6():
    plateCar = input("Digite a placa do carro: ")
    dataDeEntrega = V.veiculos_alugados[plateCar][3]
    diff = V.diff_days2(dataDeEntrega)

    if diff >= 1:
        print("Você irá pagar Juros!\nVocê agora deve: ", V.veiculos_alugados[plateCar][1] * diff)
        cont = input("Aperte Enter para confirmar o pagamento e a devolução!")

    cpf = V.veiculos_alugados[plateCar][0]
    email = U.dataUser[cpf][6]
    nameCar = V.dados_Veiculos[plateCar][0]
    V.veiculos_alugados.pop(plateCar)
    V.dados_Veiculos[plateCar][8] += 1
    V.saveData(V.DB_Veiculos_alugados, V.veiculos_alugados)
    V.saveData(V.DB_Veiculos, V.dados_Veiculos)
    print(nameCar, "devolvido.")
    print("Enviando e-mail de confirmação...")
    U.sendEmail(email, cpf, nameCar, "", "", "", "Devolução")
    print("E-mail enviado!")
    cont = input("Aperte Enter para confirmar a devolução!")


def menuOp7():
    j = 1
    for i in V.dados_Veiculos:
        if V.dados_Veiculos[i][8] != 0:
            print('\t', j, '-', V.dados_Veiculos[i][0])
            j += 1
        else:
            print("Não há veículos disponíveis!")


def menuOp9():
    V.pullData()
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
        V.newCar(Car_Model, Car_Color, Car_Year, Car_Price, Car_Plate, Car_Renavam, Car_KM, 0, 1)
        print("Cadastro efetuado com sucesso!")

    elif op == '2':
        editar = input("Digite a placa do veículo que deseja modificar cadastro no foramto 'XXX-0000': ")
        V.checkCarExist(editar)
        print("O que deseja alterar?")
        print("1 - Cor do veículo")
        print("2 - Preço do aluguel")
        print("3 - Quilômetros rodados do veículo")
        print("0 - Voltar")
        while op != '10':
            op = input("Qual campo deseja alterar? ")

            if op == "1":
                Car_Color = input("Qual a cor do veículo? ")
                V.valColor(Car_Color)
                V.carEdit(editar, Car_Color, 2)
            elif op == "2":
                Car_Price = input("Qual o preço do veículo no formato '000.00' ou '0000.00'? ")
                V.valPrice(Car_Price)
                V.carEdit(editar, Car_Price, 4)
            elif op == "3":
                Car_KM = input("Digite os quilômetros rodados do veículo no formato '000000': ")
                V.valKM(Car_KM)
                V.carEdit(editar, Car_KM, 7)
            elif op == "0":
                break


def menuOp10():
    op = ""
    while op != '6':
        dataPullAll()
        op = input("\n\nDigite uma opção do menu acima: ")

        if op == '1':
            V.bestCars()
        elif op == '2':
            U.bestClients()
        elif op == '3':
            V.showHistoric()
        elif op == '0':
            break
        else:
            print("OPÇÃO INVÁLIDA!")
