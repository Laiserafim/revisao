minimo= float(input("Qual o valor do salário mínimo atual? "))
salario = 1

while salario != 0:
    salario = float(input("Digite o seu salário: "))
    divisao = salario / minimo

    print(f"O Seu salário é R$ {salario} e você recebe R$ {divisao} salários mínimos.")
