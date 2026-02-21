try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
except ZeroDivisionError:
    print("Erro: Não é possível dividir um número por zero.")
except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")
else:
    # Este bloco só roda se não houver erro de divisão por zero ou de valor
    print(f"O resultado da divisão é: {resultado}")
    print("A divisão foi realizada com sucesso!")