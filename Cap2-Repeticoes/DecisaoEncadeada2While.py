resposta = "SIM"
while resposta == "SIM":

    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()

    # Possui doença infectocontagiosa?

    while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
        print("Digite SIM ou NAO")
        doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente " + nome + " para a sala AMARELA.")
    else:
        print("Encaminhe o paciente " + nome + " para a sala BRANCA.")

    # Idade

    if idade >= 65:
        print("Paciente COM prioridade")
    else:
        genero = input("Digite o gênero do paciente: ").upper()
        if genero == "FEMININO" and idade > 10:
            gravidez = input("A paciente está gravida? ").upper()
            if gravidez == "SIM":
                print("Paciente " + nome + " COM prioridade.")
            else:
                print("Paciente " + nome + " SEM prioridade.")
        else:
            print("Paciente " + nome + " SEM prioridade.")
