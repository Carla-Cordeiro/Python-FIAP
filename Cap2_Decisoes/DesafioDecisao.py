# DESAFIO
# Solicita nivel de acesso da pessoa (ADM,USR ou GUEST) e gênero
# ADM - "Olá administrador" para homens "Olá administradora" mulheres
# USR - "Olá usuário" ou "olá usuária"
# GUEST - "Olá visitante"
# Outro - "Olá desconhecido(a)"

nivel = input("Digite o nível de acesso (ADM, USR ou GUEST): ").upper()
if nivel == "ADM" or nivel == "USR":
    genero = input("Digite gênero: ").upper()
    if nivel == "ADM":
        if genero == "FEMININO":
            print("Olá administradora")
        else:
            print("Olá administrador")
    else:
        if genero == "FEMININO":
            print("Olá usuária")
        else:
            print("Olá usuário")
elif nivel == "GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido (a)")
