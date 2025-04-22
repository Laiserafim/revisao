peso= float(input("Digite o seu peso: "))
altura= float(input("Digite a sua altura: "))

imc= peso / altura**2

print(f"{imc:.1f}")

if imc < 18.6:
    print("Abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print("Peso ideal")
elif imc >= 25.5 and imc <= 20.9:
    print("Levemente acima do peso.")
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau I")
elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade grau II (severa)")
else:
    print("Obesidade grau III (Mórbida)")