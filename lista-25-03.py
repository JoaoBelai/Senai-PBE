#-------- Exercício 1 -------

#----------------------------
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


