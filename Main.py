#import
import User

###############################
## 		PY RENT A CAR 		##
## Create by:               ##
##        Bruno and João    ##
###############################

op, cnh, rg = '', '', ''

while op != 10:
    print('''MENU DE CADASTRAMENTO
1 - Cadastrar novo cliente
2 - Consultar cliente existente
3 - Atualizar cadastro de cliente
4 - Excluir cadastro de cliente
\nMENU DE LOCAÇÃO
5 - Alugar veículos
6 - Consultar veículos disponíveis
7 - Consultar registro de emprśtimos efetuados
8 - Consultar tabela de preços
\nMENU DE HISTÓRICOS
9 - Consultar históricos da empresa
\n0 - Sair''')

    op = int(input("Digite uma opção do menu acima: "))

    if op == 1:
        # Nome_User = input("Nome:")
        # Sobrenome_User = input("Sobrenome:")
        # Data_Nasc = input("Data de Nascimento:")
        # CPF = input("CPF:")
        # Nome_Mae = input("Nome da Mãe:")
        User.valida_outros(rg, 9, "RG")
        Email = input("Email:")
        while User.validaEmail(Email) == False:
            Email = input("Email Inválido! Digite outro Email:")
        User.valida_outros(cnh, 10, "CNH/Habilitação")

    if op == 9:
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
                break

            else:
                print("OPÇÃO INVÁLIDA!")

    elif op == 0:
        break

    else:
        print("OPÇÃO INVÁLIDA!")
