usuarios = {}
opcao = input("Selecione a opção desejada: \n") + \
        "<1> - INSERIR \n" + "<2> - PESQUISAR \n" + "<3> - EXCLUIR \n" + "<4> - LISTAR \n".upper()

while opcao == "1" or "2" or "3" or "4":
    if opcao == "1":
        chave = input("Digite login: ").upper()
        usuarios[chave] = [input("Digite o nome: ").upper(),
                           input("Digite a data de acesso: ").upper(),
                           input("Digite a ultima estação acessada: ").upper()]

    opcao = input("O que deseja realizar? \n" +
                  "<1> Para INSERIR um novo usuário\n" +
                  "<2> Para PESQUISAR um usuário\n" +
                  "<3> Para EXCLUIR um usuário\n" +
                  "<4> Para LISTAR um usuário: ").upper()
