# ---------- Exercício 1 -----------
print("\nExercício 1")
nome = "João"
print(nome)
#------------------------------------
# ---------- Exercício 2 -----------
print("\nExercício 2")
a= 5
b = 10
soma = a+b
subtracao = a-b
divisao = a/b
multiplicacao = a*b

print(f"A soma dos números é: {soma}")
print(f"A subtração dos números é: {subtracao}")
print(f"A divisão dos números é: {divisao}")
print(f"A multiplicação  dos números é: {multiplicacao}")
#------------------------------------
# ---------- Exercício 3 -----------
print("\nExercício 3")
preco = 50
desconto = 10
valor_final = preco-desconto
print(f"\nO resultado com desconto é: {valor_final}")
#------------------------------------
# ---------- Exercício 4 -----------
print("\nExercício 4")
resultado = 10+5*2

print(resultado)
#------------------------------------
# ---------- Exercício 5 ------------
print("\nExercício 5")
valor1 = "150"
valor1 = int(valor1)
resultado_conta = valor1 * 2
print(resultado_conta)
#------------------------------------
# ---------- Exercício 6 ------------
print("\nExercício 6")
lista = [1,2,3,4,5]
print(lista)
lista[1]=20
print(lista)
#------------------------------------
# ---------- Exercício 7 ------------
print("\nExercício 7")
numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))

soma_numeros = numero1 + numero2

print(soma_numeros)
#------------------------------------
# ---------- Exercício 8 ------------
print("\nExercício 8")
x = float(input("Digite o primeiro número:"))
y = float(input("Digite o segundo número:"))

divisao_inteira = x//y

print(divisao_inteira)
#------------------------------------
# ---------- Exercício 9 ------------
print("\nExercício 9")

numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))

print(f"{numero1>numero2}")
#------------------------------------
# ---------- Exercício 10 ------------
print("\nExercício 10")
idade = int(input("quantos anos você tem:"))

dias = idade * 365
print(f"\nVocê viveu {dias} dias")
#------------------------------------
# ---------- Exercício 11 ------------
print("\nExercício 11")
base = int(input("Digite o primeiro número:"))
expoente = int(input("Digite o segundo número:"))

elevado = base ** expoente

print(elevado)
#------------------------------------
# ---------- Exercício 12 ------------
print("\nExercício 12")
preco = int(input("Digite o valor do produto:"))

preco = str(preco)

print(f"\nO preço é R${preco}")
#------------------------------------
# ---------- Exercício 13 ------------
print("\nExercício 13")

raio = int(input("Digite o raio do círculo: "))

area = 3.14 * (raio**2)

print(area)

#------------------------------------
# ---------- Exercício 14 ------------
print("\nExercício 14")

a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))

a,b = b,a

print(f"\nEste é o novo valor de a: {a}")
print(f"\nEste é o novo valor de b: {b}")

#------------------------------------
# ---------- Exercício 15 ------------
print("\nExercício 15")

nota1 = float(input("\nEscreva a primeira nota:"))
nota2 = float(input("\nEscreva a segunda nota:"))
nota3 = float(input("\nEscreva a terceira nota:"))

ponderada= ((nota1*2)+(nota2*3)+(nota3*5))/10

print(f"\nO resultado da média ponderada é: {ponderada}")

#------------------------------------
# ---------- Exercício 16 ------------
import math
print("\nExercício 16")

x1 = float(input("\nEscreva a primeira cordenada x:"))
y1 = float(input("\nEscreva a primeira cordenada y:"))
x2 = float(input("\nEscreva a segunda cordenada x:"))
y2 = float(input("\nEscreva a segunda cordenada y:"))

euclidiana = math.sqrt((x2-x1)**2 + (y2-y1)**2)


print(f"\nA distância entre dois pontos no gráfico é: {euclidiana}")

