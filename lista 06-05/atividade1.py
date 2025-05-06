produtos = {
    "Produto A" : 5.0,
    "Produto B" : 8.0,
    "Produto C" : 12.0
}
chave = 0

for chave in produtos:
    produtos[chave] *= 2

print(f"O novo valor para a promoção é: {produtos}")
