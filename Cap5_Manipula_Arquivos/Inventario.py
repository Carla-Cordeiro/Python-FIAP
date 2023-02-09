from Funcoes.Funcoes_Arquivos import *

inventario = {}
opcao = chamarMenu()
while 0 < opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:

            lista = linha.split(";")
            print("Data: ", lista[1])
            print("Descrição: ", lista[2])
            print("Departamento: ", lista[3])

            # separacao = linha[linha.find(";") + 1:-1]
            # data = separacao[0:separacao.find(";")]
            # separacao = separacao[separacao.find(";") + 1:-1]
            # descricao = separacao[0:separacao.find(";")]
            # departamento = linha[linha.rfind(";") + 1:-1]
            # print("Data: ", data)
            # print("Descrição: ", descricao)
            # print("Departamento: ", departamento)


    opcao = chamarMenu()

# opcao = int(input("Digite: "
#                   "\n<1> para registrar ativo"
#                   "\n<2> para persistir em arquivo"
#                   "\n<3> para exibir ativos armazenados: "))
# while 0 < opcao < 4:
#     if opcao == 1:
#         resp = "S"
#         while resp == "S":
#             inventario[input("Digite o número patrimonial: ")] = [
#                 input("Digite a data da última atualização: "),
#                 input("Digite a descrição: "),
#                 input("Digite o departamento: ")]
#             resp = input("Digite <S> para continuar.").upper()
#
#     elif opcao == 2:
#         with open("inventario.csv", "a") as inv:
#             for chave, valor in inventario.items():
#                 inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
#                 print("Persistido com sucesso!")
#
#     elif opcao == 3:
#         with open("inventario.csv", "r") as inv:
#             print(inv.readlines())
#         opcao = int(input("Digite: "
#                           "\n<1> para registrar arquivo"
#                           "\n<2> para persistir em arquivo"
#                           "\n<3> para exibir ativos armazenados: "))
