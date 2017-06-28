import Veiculos as V

# Modelo_carro = input("Qual o modelo do Carro?")
# Cor_carro = input("Qual a cor?")
# Ano_carro = input("Ano do carro?")
# Preco_carro = input("Qual o preço do Alugueu?")
# Placa_carro = input("Placa?")
# Renavam_carro = input("Renavam?")
# km = input("KM rodados?")
# Modelo_carro = "Civic"
# Cor_carro = "Preto"
# Ano_carro = "2016"
# Preco_carro = "100"
# Placa_carro = "GTA-2017"
# Renavam_carro = "XXXXXXX"
# km = "100"

# Carro = Veiculos.newCarro(Modelo_carro,Cor_carro,Ano_carro,Preco_carro,Placa_carro,Renavam_carro,km)
# Carro.salvarDados()
# termo = input("Por qual termo deseja pesquisar?")
# Veiculos.pesquisar(termo)



# Nome_User = input("Nome:")
# Sobrenome_User = input("Sobrenome:")
# Data_Nasc = input("Data de Nascimento:")
# CPF = input("CPF:")
# Nome_Mae = input("Nome da Mãe:")
# RG = input("RG:")
# Email = input("Email:")
# CNH = input("Habilitação:")
# Endereco = input("Endereco:")
# Telefone = input("Telefone:")
#
# User.newUsuario(Nome_User, Sobrenome_User, Data_Nasc, CPF, Nome_Mae, RG, Email, CNH, Endereco, Telefone)
# ser.salvarDados()
# User.puxarDados()
# print(User.dados_Users)
#

# while True:
#     cpf = input("CPF: ")
#     if User.val_cpf(cpf) == True:
#         print("CPF Válido")
#         break
#     else:
#         print("Inválido! Digite novamente!")


# #
# # Veiculos.alugar()
# cnh,rg = '',''
#
# def pratudo(variavel, qtd_letras,txt):
#     while True:
#         variavel = input(txt+":")
#         variavel = re.sub("[a-z,A-Z]", "", variavel)
#         if len(variavel) == qtd_letras:
#             print(variavel)
#             break
#         else:
#             print(txt,"Inválido, digite novamente!")
#
# CPF
#
# soma2, soma1 = 0, 0
# tam = 10
#
# if len(cpf) != 11:
#     return False
#
# else:
#     for j in range(2):
#         soma2 = soma1
#         soma1 = 0
#
#         for i in range(tam - 1):
#             soma1 += int(cpf[i]) * tam
#             tam -= 1
#
#         tam = 11
#     result1 = 11 - (soma2 % 11)
#     result2 = 11 - (soma1 % 11)
#     d1 = int(cpf[9])
#     d2 = int(cpf[10])
#
#     if cpf[2] == cpf[4] == cpf[9]:
#         return False
#
#     else:
#         if (d1 == result1) or ((result1 == (10 or 11)) and 0 == d1):
#             if (d2 == result2) or ((result2 == (10 or 11)) and 0 == d2):
#                 return True
#         else:
#             return False

# cnh=input("cnh: ")
# print(User.valida_outros(cnh,10))
# rg=input("RG: ")
# print(User.valida_outros(rg,9))

# cpf = input("cpf: ")
# print(User.val_cpf(cpf))

# Nome_User = input("Nome: ")
# User.validNomeSobrenome(Nome_User, "Nome")

#
# dataN = input("Digite a data de nascimento (dd/mm/aaaa): ")
# while User.validData(dataN) == False:
#     dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ")
#
# placa = input("Placa: ")
# Veiculos.validaPlaca(placa)
# import re
#
#
# def validNomeSobrenome(m):
#     return bool(re.match("[a-zA-Zãõçóúáé ]{2,}", m))
#
#
# nome = input("Nome:   ")
# while validNomeSobrenome(nome) == False:
#     nome = input("Nome inválido! Digite um Nome válido: ")
#
# )
#
# User.newUsuario('Nome_User', 'Sobrenome_User', 'dataN', 'CPF', 'Nome_Mae', 'RG', 'Email', 'CNH', 'Endereco', 'Fone',
#                 "0")
# User.newUsuario('Nome_User', 'Sobrenome_User', 'dataN', 'CPF', 'Nome_Mae', 'RG', 'Email', 'CNH', 'Endereco', 'Fone',
#                 "0")

# Veiculos.todayDate()
# Veiculos.nowHour()
# Veiculos.calendarShow()

# Fone = input("Telefone (xx) xxxxx-xxxx: ")
# # User.valFone(Fone)
#
# RG = input("RG: ")
# while User.valOthers(RG, 9) is False:
#     RG = input("RG Inválido!\nDigite outro RG: ")

# V.pullData(V.DB_Veiculos, V.dados_Veiculos)
#
#
# def OthrsExist(m):
#     return not bool(m in V.dados_Veiculos)
#
#
# def valPlate(m):
#     while bool((re.match("^\w{3}-\d{4}$", m) and OthrsExist(m))) is False:
#         m = input("Placa do veículo inválida!\nDigite a placa do carro no formato 'XXX-0000': ")
#
#
# m = input("Digite a placa do carro no formato 'XXX-0000': ")
# valPlate(m)

data = input("[dd/mm/aaaa]: ")
print(V.valDate(data))
