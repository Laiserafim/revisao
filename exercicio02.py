num = float(input("Digite um número: "))

if num < 0 and num % 2 ==0:
    print(f"{num} é Par Negativo")
elif num > 0 and num % 2 ==0:
    print(f"{num} é Par e Positivo ")
elif num > 0 and num % 2 == 1:
    print(f"{num} é impar e Positivo ")
elif num < 0 and num % 2 == 1:
    print(f"{num} é impar e negativo ")