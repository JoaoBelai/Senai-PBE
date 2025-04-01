#-------- Exercício 1 -------
numero = int(input("Digite um número:"))

if numero % 2 == 0:
    print(f"\nO número {numero} é par")
else:
    print(f"\nO número {numero} é ímpar")

#---------- Exercício 2 -----------
numero1 = int(input("Digite um número:"))

if numero1 > 10:
    print(f"\nO número {numero1} é maior que 10")
elif numero1 == 10:
    print(f"\nO número {numero1} é igual a 10")
else:
    print(f"\nO número {numero1} é menor que 10")

#---------- Exercício 3 -----------
idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("\nVocê é maior de idade")
else:
    print(f"\nVocê é menor de idade")

#---------- Exercício 4 -----------
idade = int(input("Digite sua idade:"))

if idade < 16:
    print(f"\nVocê tem {idade} anos, não pode votar")
elif idade == 16 or idade == 17 or idade >= 70:
    print(f"\nVocê tem {idade} anos, seu voto é opcional")
else:
    print(f"\nVocê tem {idade} anos, seu voto é obrigatório")

#---------- Exercício 5 -----------
num = int(input("Digite um número:"))

if num < 0:
    print(f"\no número é negativo")
elif num > 0:
    print(f"\nO número é positivo")
else:
    print(f"\nO número é igual a 0")

# ---------- Exercício 6 -----------
nota = float(input("Digite a nota:"))

if nota < 0 or nota > 10:
    print(f"\nNota inválida")
elif nota >= 9:
    print(f"\nNota A")
elif nota >= 7:
    print(f"\nNota B")
elif nota >= 5:
    print(f"\nNota C")
elif nota >= 3:
    print(f"\nNota D")
else:
    print(f"\nNota E")
# ---------- Exercício 7 -----------
idade = int(input("Digite a sua idade:"))

if idade <= 12:
    print(f"Você tem {idade} anos, você tem direito ao desconto de crianças")
elif idade >= 60:
    print(f"Você tem {idade} anos, você tem direito ao desconto de idosos")
else:
    print(f"Você tem {idade} anos, não tem direito a desconto")

# ---------- Exercício 8 -----------
lado1 = float(input("Digite o primeiro lado do triângulo:"))
lado2 = float(input("Digite o segundo lado do triângulo:"))
lado3 = float(input("Digite o terceiro lado do triângulo:"))

if lado1 >= lado2 + lado3 or lado3 >= lado1 + lado2 or lado2 >= lado1 + lado3:
    print("\nTriângulo inválido")
else:
    print("\nTriângulo é válido")
    if lado1 == lado2 and lado2 == lado3:
        print("\nTriângulo equilátero")
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print("\nTriângulo ecaleno")
    else:
        print("\nTriângulo isósceles")

# ---------- Exercício 9 -----------
valor = float(input("Digite o valor da sua compra:"))

if valor < 100:
    desconto = valor * 0.05
    final = valor - desconto
    print(f"\nO valor final com desconto é de: {final}")
elif valor > 500:
    desconto = valor * 0.15
    final = valor - desconto
    print(f"\nO valor final com desconto é de: {final}")
else:
    desconto = valor * 0.10
    final = valor - desconto
    print(f"\nO valor final com desconto é de: {final}")

# ---------- Exercício 10 -----------
ano = int(input("Digite o ano a ser testado:"))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"\nO ano {ano} é bissexto")
else:
    print(f"\nO ano {ano} não é bissexto")

# ---------- Exercício 11 -----------
altura = float(input("Digite sua altura em metros: "))
peso = float(input("digite seu peso em kg: "))

imc = peso / altura ** 2

if imc < 18.5:
    print("\nAbaixo do peso")
elif imc < 24.9:
    print("\nPeso Normal")
elif imc < 29.9:
    print("\nSobrepeso")
else:
    print("\nObesidade")

# ---------- Exercício 12 -----------
num1 = float(input("Escreva o primeiro número: "))
num2 = float(input("Escreva o segundo número: "))
num3 = float(input("Escreva o terceiro número: "))

if (num1 > num2 and num2 > num3) or (num1 == num2 and num2 > num3):
    print("\nVocê escreveu em ordem decrescente")
elif (num1 < num2 and num2 < num3) or (num1 == num2 and num2 < num3):
    print("\nVocê escreveu em ordem crescente")
elif num1 == num2 and num2 == num3:
    print("\nOs números são iguais")
else:
    print("\nNenuma ordem válida")

#-------------Exercício 13-------------
temperatura = float(input("Digite a temperatura em Celcius: "))

if temperatura < 10:
    print("\nO tempo está frio")
elif temperatura < 25:
    print("\nO tempo está aconchegante")
elif temperatura < 40:
    print("\nO tempo está quente")
else:
    print("\nO tempo está muito quente")

#-------------Exercício 14-------------
data = input("Digite a data nesse formato dd/mm/aaaa: ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

print(f"\n{ano}-{mes}-{dia}")

# -------------Exercício 15-------------
import re

senha = input("Digite sua senha: ")

quantidade = len(senha)

if quantidade >= 8:
    if re.search(r'[a-z]', senha):
        if re.search(r'[A-Z]', senha):
            if re.search(r'[0-9]', senha):
                if re.search(r'[@!#$%&*]', senha):
                    print("\nSenha válida")

                else:
                    print("\nSenha Inválida, ela deve conter no mínimo um caractere especial")
            else:
                print("\nSenha Inválida, ela deve conter no mínimo um número")
        else:
            print("\nSenha Inválida, ela deve conter no mínimo uma letra maiúscula")
    else:
        print("\nSenha Inválida, ela deve conter no mínimo uma letra minúscula")

else:
    print("\nSenha Inválida, ela deve ter no mínimo 8 dígitos")

#-------------Exercício 16-------------
import math
valor = float(input("Digite o número iremos calcular a raiz quadrada: "))

if valor >= 0:
    if valor <= 100:
        raiz = math.sqrt(valor)
        print(f"\nA raiz quadrade de {valor} é {raiz:.2f}")
    else:
        print("\nNúmero muito grande, reduza para um valor abaixo de 100")
else:
    print("\nNão é possível calcular raiz quadrada de um número negativo")

# -------------Exercício 17-------------
data = input("Digite a data nesse formato dd/mm/aaaa: ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

dia = int(dia)
mes = int(mes)
ano = int(ano)

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):

    if mes == 2:
        if dia >= 1 and dia <= 29:
            print(f"\n{ano}-{mes}-{dia}")
        else:
            print("\nDia inválido")

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:
            print(f"\n{ano}-{mes}-{dia}")
        else:
            print("\nDia inválido")

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print(f"\n{ano}-{mes}-{dia}")
        else:
            print("\nDia inválido")

    else:
        print("\nMês inválido")
else:
    if mes == 2:
        if dia >= 1 and dia <= 28:
            print(f"\n{ano}-{mes}-{dia}")
        else:
            print("\nDia inválido")

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:
            print(f"\n{ano}-{mes}-{dia}")
        else:
            print("\nDia inválido")

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print(f"\n{ano}-{mes}-{dia}")
        else:
            print("\nDia inválido")

    else:
        print("\nMês inválido")

#-------------Exercício 18-------------
expressao= input("Digite a conta que deseja fazer: ")

resultado = eval(expressao)

print(f"\nO resultado da expressão apresentada é: {resultado}")

#--------- DESAFIO ----------
print("\nDesafio")
import re

cpf = input("\nDigite um Cpf:")
cpf = re.sub("[.]","", cpf)
cpf = re.sub("-","", cpf)

num1 = int(cpf[0])
num2 = int(cpf[1])
num3 = int(cpf[2])
num4 = int(cpf[3])
num5 = int(cpf[4])
num6 = int(cpf[5])
num7 = int(cpf[6])
num8 = int(cpf[7])
num9 = int(cpf[8])
num10 = int(cpf[9])
num11 = int(cpf[10])

if len(cpf) == 11:
    somaverif = (num1*10) + (num2*9) + (num3*8) + (num4*7) +(num5*6) + (num6*5) + (num7*4) +(num8*3) +(num9*2)
    resto = somaverif % 11
    if resto < 2:
        estadonum10 = num10 == 0
    else:
        estadonum10 = num10 == 11-resto

    somaverif = (num1*11) + (num2*10) + (num3*9) + (num4*8) + (num5*7) + (num6*6) + (num7*5) + (num8*4) + (num9*3) + (num10*2)
    resto = somaverif % 11
    if resto < 2:
        estadonum11 = num11 == 0
    else:
        estadonum11 = num11 == 11-resto

    if estadonum10 == False or estadonum11 == False:
        print("\nCPF inválido!")
    else:
        print("\nCPF válido!")
else:
    print("\nCPF inválido!")
