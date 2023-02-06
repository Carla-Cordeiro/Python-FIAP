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
