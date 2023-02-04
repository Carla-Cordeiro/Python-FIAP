nome = input("Digite o nome do funcionário: ")
empresa = input("Digite o nome da instituição: ")
qtde_funcionarios =int(input("Digite a quantidade de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print("O funcionário " + nome +" trabalha na empresa " + empresa + ".")
print("A empresa " + empresa + " possui ", qtde_funcionarios, " funcionários.")
print("A média de mensalidade é de: " + str(mediaMensalidade) + ".")

print(" -------------------------- Verificação do tipo de Dado --------------------------")
print("O tipo da dado da variável [nome] é: ", type(nome))
print("O tipo da dado da variável [empresa] é: ", type(empresa))
print("O tipo da dado da variável [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variável [mediaMensalidade] é: ", type(mediaMensalidade))
