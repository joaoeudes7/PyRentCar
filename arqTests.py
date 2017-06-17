# import re

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
# CPF= input("CPF:")
# Nome_Mae = input("Nome da Mãe:")
# Rg = input("RG:")
# Email = input("Email:")
# Habilitação = input("Habilitação:")
#
#
# Usuario = User.newUsuario(Nome_User,Sobrenome_User,Data_Nasc,CPF,Nome_Mae,Rg,Email,Habilitação)
# Usuario.salvarDados()
# User.puxarDados()
# # print(User.dados_Users)
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
import re


def validNomeSobrenome(m):
    return bool(re.match("[a-zA-Zãõçóúáé ]{2,}", m))


nome = input("Nome:   ")
while validNomeSobrenome(nome) == False:
    nome = input("Nome inválido! Digite um Nome válido: ")
