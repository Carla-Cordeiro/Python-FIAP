nome = input("Digite o nome do paciente: ")
idade = int(input("Digite idade do paciente: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontgiosa? ") .upper()
if idade >=65:
    print("Paciente " + nome + " COM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe para a sala AMARELA")
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
else:
    print("Paciente " + nome + " SEM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe para a sala AMARELA")
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")