# import
import User

###############################
## 		PY RENT A CAR 		##
## Create by:               ##
##        Bruno and João    ##
###############################

op, cnh, rg = '', '', ''

while op != 10:
    print('''/// MENU DE CADASTRAMENTO
1 - Cadastrar novo cliente
2 - Consultar cliente existente
3 - Atualizar cadastro de cliente
4 - Excluir cadastro de cliente
\n/// MENU DE LOCAÇÃO
5 - Alugar veículos
6 - Consultar veículos disponíveis
7 - Consultar registro de emprśtimos efetuados
8 - Consultar tabela de preços
\n/// MENU DE HISTÓRICOS
9 - Consultar históricos da empresa
\n0 - Sair\n\n''')

    op = int(input("// Digite uma opção do menu acima: "))
    if op == 1:

        Nome_User = input("Nome: ")
        while User.validNomeSobrenome(Nome_User) == False:
            Nome_User = input("Nome Inválido!\nDigite outro Nome: ")

        Sobrenome_User = input("Sobrenome: ")
        while User.validNomeSobrenome(Sobrenome_User) == False:
            Sobrenome_User = input("Nome Inválido!\nDigite outro Nome: ")

        dataN = input("Digite a data de nascimento (dd/mm/aaaa): ")
        while User.validData(dataN) == False:
            dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")

        CPF = input("CPF: ")
        while User.val_cpf(CPF) == False:
            CPF = input("CPF Inválido!\nDigite outro CPF: ")

        Nome_Mae = input("Nome da Mãe: ")
        while User.validNomeSobrenome(Nome_Mae) == False:
            Nome_Mae = input("Nome Inválido!\nDigite outro Nome: ")

        RG = input("RG: ")
        while User.valida_outros(RG, 9) == False:
            RG = input("RG Inválido!\nDigite outro RG: ")

        Email = input("Email:")
        while User.validaEmail(Email) == False:
            Email = input("Email Inválido!\nDigite outro Email:")

        CNH = input("CNH: ")
        while User.valida_outros(CNH, 10) == False:
            CNH = input("CNH Inválida!\nDigite outra CNH: ")

    elif op == 2:

        while True:
            termo = input("Digite o nome do cliente: ")
            User.pesquisar(termo)

    elif op == 3:

        User.mostrarUsers()

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
