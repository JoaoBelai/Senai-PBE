palindromo1 = "Ana Ana"
palindromo2 = "1DSTB-SENAI"
palindromo3 = "Subi no Onibus"

tratado_palindromo1 = palindromo1.replace(" ", "").lower()
tratado_palindromo2 = palindromo2.replace(" ", "").lower()
tratado_palindromo3 = palindromo3.replace(" ", "").lower()

print(tratado_palindromo3)
print(tratado_palindromo3[::-1])

if tratado_palindromo1 == tratado_palindromo1[::-1]:
    print(f"A frase {palindromo1} é um palindromo!")
else:
    print(f"A frase {palindromo1} não é um palindromo!")

if tratado_palindromo2 == tratado_palindromo2[::-1]:
    print(f"A frase {palindromo2} é um palindromo!")
else:
    print(f"A frase {palindromo2} não é um palindromo!")

if tratado_palindromo3 == tratado_palindromo3[::-1]:
    print(f"A frase {palindromo3} é um palindromo!")
else:
    print(f"A frase {palindromo3} não é um palindromo!")