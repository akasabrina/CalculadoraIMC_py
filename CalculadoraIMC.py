# Library
import os

# Código
flag = True
while flag == True:
    os.system("cls")
    peso = float(input("Qual o seu peso(kg)? "))
    altura = float(input("Qual a sua altura(m)? "))

    if (peso <= 0) or (altura <= 0):
        print("\n\n---Digite números válidos---\n\n")
        os.system("pause")
        flag = True
    else:
        imc = peso / (altura**2)

        print(f"\nSeu IMC é {imc:.2f}")

        if imc < 18.5:
            print("\nIMC menor que 18.50 --> Abaixo do peso normal.\n")
        elif imc < 25:
            print("\nIMC entre 18.50 e 24.9 --> Peso Normal.\n")
        elif imc < 30:
            print("\nIMC entre 25 e 29.9 --> Excesso de Peso.\n")
        elif imc < 35:
            print("\nIMC entre 30 e 34.9 --> Obesidade Grau I.\n")
        elif imc < 40:
            print("\nIMC entre 35 e 39.9 --> Obesidade Grau II(severa).\n")
        else:
            print("\nIMC maior ou igual a 40 --> Obesidade Grau III(morbida).\n")
        
        mensagem = input("Gostaria de calcular novamente?(S/N) ")
        msg = mensagem.upper()
        if msg == "S":
            flag = True
        else:
            flag = False
