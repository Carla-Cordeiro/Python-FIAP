#Texto base
#Filtros: possui doença infectocontagiosa; idade; está gestante.

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?") .upper()

#Possui doença infectocontagiosa?

if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente " + nome + " para a sala AMARELA.")
elif doenca_infectocontagiosa == "NAO":
    print("Encaminhe o paciente " + nome + " para a sala BRANCA.")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM OU NAO")

#Idade

if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o gênero do paciente: ") .upper()
    if genero == "FEMININO" and idade >10:
        gravidez = input("A paciente está gravida? ") .upper()
        if gravidez == "SIM":
            print("Paciente " + nome + " COM prioridade.")
        else:
            print("Paciente " + nome + " SEM prioridade.")
    else:
        print("Paciente " + nome + " SEM prioridade.")