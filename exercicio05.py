minimo= float(input("Qual o valor do salário mínimo atual? "))

while True:
    salario = float(input("Digite o seu salário: "))
    if salario == 0:
        print("Programa terminado")
        break

    divisao = salario / minimo
    print(f"O Seu salário é R$ {salario} e você recebe R$ {divisao} salários mínimos.")