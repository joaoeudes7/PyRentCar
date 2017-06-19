# import
import User
import Veiculos

DB = "DB_User.dat"
###############################
## 		PY RENT A CAR 		##
## Create by:               ##
##        Bruno and João    ##
###############################

op, cnh, rg = '', '', ''

while op != 10:
    User.puxarDados()
    Veiculos.puxarDados()
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
\n/// MENU DE HISTÓRICOS
9 - Consultar históricos da empresa
\n0 - Sair\n\n''')

    op = int(input("// Digite uma opção do menu acima: "))
    if op == 1:

        Nome_User = input("Nome: ")
        User.validNomeSobrenome(Nome_User, "Nome")

        Sobrenome_User = input("Sobrenome: ")
        User.validNomeSobrenome(Sobrenome_User, "Sobrenome")

        dataN = input("Digite a data de nascimento (dd/mm/aaaa): ")
        while User.validData(dataN) is False:
            dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")

        CPF = input("CPF: ")
        while User.val_cpf(CPF) is False:
            CPF = input("CPF Inválido!\nDigite outro CPF: ")

        Nome_Mae = input("Nome da Mãe: ")
        User.validNomeSobrenome(Nome_Mae, "Nome")

        RG = input("RG: ")
        while User.valida_outros(RG, 9) is False:
            RG = input("RG Inválido!\nDigite outro RG: ")

        Email = input("Email:")
        User.validaEmail(Email)

        CNH = input("CNH: ")
        while User.valida_outros(CNH, 10) is False:
            CNH = input("CNH Inválida!\nDigite outra CNH: ")

        Endereco = input("Endereço: ")
        User.validaEndereco(Endereco)

        Fone = input("Telefone (xx) xxxxx-xxxx: ")
        User.validaFone(Fone)

        User.newUsuario(Nome_User, Sobrenome_User, dataN, CPF, Nome_Mae, RG, Email, CNH, Endereco, Fone)

    elif op == 2:

        while True:
            termo = input("Digite o nome do cliente: ")
            User.pesquisar(termo)

    elif op == 3:
        User.mostrarUsers()

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
            User.validNomeSobrenome(Nome_User, "Nome")
            User.editUser(editar, Nome_User, op)
        elif op == 2:
            Sobrenome_User = input("Digite o novo sobrenome: ")
            User.validNomeSobrenome(Sobrenome_User, "Sobrenome")
            User.editUser(editar, Sobrenome_User, op)
        elif op == 3:
            dataN = input("Digite a nova data de nascimento (dd/mm/aaaa): ")
            while User.validData(dataN) is False:
                dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")
            User.editUser(editar, dataN, op)
        elif op == 4:
            CPF = input("Digite o novo CPF: ")
            while User.val_cpf(CPF) is False:
                CPF = input("CPF Inválido!\nDigite outro CPF: ")
            User.editUser(editar, CPF, op)
        elif op == 5:
            Nome_Mae = input("Digite o novo nome da Mãe: ")
            User.validNomeSobrenome(Nome_Mae, "Nome")
            User.editUser(editar, Nome_Mae, op)
        elif op == 6:
            RG = input("RG: ")
            while User.valida_outros(RG, 9) is False:
                RG = input("RG Inválido!\nDigite outro RG: ")
            User.editUser(editar, RG, op)
        elif op == 7:
            Email = input("Email:")
            User.validaEmail(Email)
            User.editUser(editar, Email, op)
        elif op == 8:
            CNH = input("CNH: ")
            while User.valida_outros(CNH, 10) is False:
                CNH = input("CNH Inválida!\nDigite outra CNH: ")
            User.editUser(editar, CNH, op)
        elif op == 0:
            break
        else:
            print("Opcao invalida!")
    elif op == 4:
        User.mostrarUsers()
        optDel = input("Qual destes quer remover?")
        User.removerUser(optDel)
    elif op == 9:
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
