from Funcoes.Funcoes_JSON import *

inventario = ler_arquivo("inventario_json.json")
opcao = chamarMenu()
while 0 < opcao < 3:
    if opcao == 1:
        print(registrar(inventario, "inventario_json.json"))
    elif opcao == 2:
        exibir("inventario_json.json")

    opcao = chamarMenu()

# import json
# import os
#
# if os.path.exists("inventario_json.json"):
#     with open("inventario_json.json", "r") as arq_json:
#         inventario = json.load(arq_json)
#
# else:
#     inventario = {}
#
# opcao = int(input("Digite: "
#                   "\n<1> para registrar ativo"
#                   "\n<2> para exibir ativos armazenados"))
# while 0 < opcao < 3:
#     if opcao == 1:
#         resp = "S"
#         while resp == "S":
#             inventario[input("Digite o número patrimonial: ")] = [
#                 input("Digite a data da última atualização: "),
#                 input("Digite a descrição: "),
#                 input("Digite o departamento: ")]
#             resp = input("Digite <S> para continuar. ").upper()
#         with open("inventario_json.json", "w") as arq_json:
#             json.dump(inventario, arq_json)
#         print("JSON GERADO")
#
#     elif opcao == 2:
#         with open("inventario_json.json", "r") as arq_json:
#             resultado = json.load(arq_json)
#             for chave, dado in inventario.items():
#                 print("Data: ", dado[0])
#                 print("Descrição: ", dado[1])
#                 print("Departamento: ", dado[2])
#
#     opcao = int(input("Digite: "
#                       "\n<1> para registrar ativo: "
#                       "\n<2> para exibir ativos armazenados: "))
