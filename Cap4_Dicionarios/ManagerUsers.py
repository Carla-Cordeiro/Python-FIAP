from Cap4_Dicionarios.Funcoes import *

usuarios = {}

opcao = perguntar()
while opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
    if opcao == "1":
        inserir(usuarios)

    if opcao == "2":
        pesquisar(usuarios, input("Qual login deseja pesquisar? "))

    if opcao == "3":
        excluir(usuarios, input("Qual login deseja excluir? "))

    if opcao == "4":
        listar(usuarios)

    opcao = perguntar()

usuarios = {}
opcao = input("Selecione a opção desejada: \n") + \
        "<1> - INSERIR \n" + "<2> - PESQUISAR \n" + "<3> - EXCLUIR \n" + "<4> - LISTAR \n".upper()

while opcao == "1" or "2" or "3" or "4":
    if opcao == "1":
        chave = input("Digite login: ").upper()
        usuarios[chave] = [input("Digite o nome: ").upper(),
                           input("Digite a data de acesso: ").upper(),
                           input("Digite a ultima estação acessada: ").upper()]
