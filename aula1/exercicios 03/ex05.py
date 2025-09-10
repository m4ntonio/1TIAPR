preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
total = preco_unitario * quantidade

if quantidade > 10:
    total *= 0.9  # aplica 10% de desconto

print(f"O valor total da compra é: R$ {total:.2f}")