def perguntar():
    resposta = input("O que deseja realizar? \n" +
                     "<1> Para INSERIR um novo usuário\n" +
                     "<2> Para PESQUISAR um usuário\n" +
                     "<3> Para EXCLUIR um usuário\n" +
                     "<4> Para LISTAR um usuário: ").upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a data de acesso: ").upper(),
                                                     input("Digite a ultima estação acessada: ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome: " + lista[0])
        print("Último acesso: " + lista[1])
        print("Última estação: " + lista[2])


def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto exluído.")


def listar(dicionario):
    for chave, valor in dicionario.itens():
        print("Objeto: ")
        print("Login: ", chave)
        print("Dados: ", valor)
