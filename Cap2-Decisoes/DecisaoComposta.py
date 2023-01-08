#Texto base
#Filtro: paciente com doença infectocontagiosa e atendimento preferencial
#Sala branca: paciente sem doença infectoc. mas com ou sem prioridade
#Sala amarela: pacientes com doenças infectoc. mas com ou sem prioridade

nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doenca_infectocontagiosa = input("O paciente possui suspeita de doença infectocontagiosa? ").upper()
if idade >=65 and doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome + " será direcionado a sala AMARELA e POSSUI atendimento prioritário.")
elif idade <65 and doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome + " será direcionado a sala AMARELA e NÃO POSSUI atendimento prioritário.")
elif idade >= 65 and doenca_infectocontagiosa == "NÃO":
    print("O paciente " + nome + " será direcionado a sala BRANCA e POSSUI atendimento prioritário.")
elif idade < 65 and doenca_infectocontagiosa == "NÃO":
    print("O paciente " + nome + " será direcionado a sala BRANCA e NÃO POSSUI atendimento prioritário.")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO")