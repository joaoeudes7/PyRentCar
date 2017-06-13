from Veiculos import newCarro, PuxarDados_Veiculos,LimparDados_Veiculos
from User import newUsuario,PuxarDados_User,LimparDados_User,Dados_users


Modelo_carro = input("Qual o modelo do Carro?")
Cor_carro = input("Qual a cor?")
Ano_carro = input("Ano do carro?")
Preco_carro = input("Qual o preço do Alugueu?")
Placa_carro = input("Placa?")
Renavam_carro = input("Renavam?")

Carro = newCarro(Modelo_carro,Cor_carro,Ano_carro,Preco_carro,Placa_carro,Renavam_carro)

newCarro.SalvarDados()

LimparDados_Veiculos()

PuxarDados_Veiculos()


Nome_User = input("Nome:")
Sobrenome_User = input("Sobrenome:")
Data_Nasc = input("Data de Nascimento:")
CPF= input("CPF:")
Nome_Mae = input("Nome da Mãe:")
Rg = input("RG:")
Email = input("Email:")
Habilitação = input("Habilitação:")


Usuario = newUsuario(Nome_User,Sobrenome_User,Data_Nasc,CPF,Nome_Mae,Rg,Email,Habilitação)
Usuario.SalvarDados()
PuxarDados_User()
print(Dados_users)