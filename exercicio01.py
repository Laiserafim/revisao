a= int(input("Digite um número: "))
b= int(input("Digite o segundo número: "))
c= int(input("Digite o terceiro número: "))
soma= a + b
print(f"{soma}")
if soma < c:
    print(f"A soma de A + B é {soma} e é menor que C: ({c})")
else:
    print("C é menor que a soma")