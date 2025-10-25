"""
import matplotlib.pyplot as plt

dados1 = ["Sim"] * 20 + ["Não"] * 45
print(dados1)

print(45 + 20)
print(20 / 65)
print(45 / 65)

labels = ['Sim', 'Não']
sizes = [20, 45]
percent_labels = ["30,77%", "69,23%"]  # Corrigido a ordem dos percentuais
colors = ['lightblue', 'lightgreen']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%')  # Adicionado autopct para mostrar percentuais
plt.title("Pesquisa de Opinião")
plt.legend(labels, loc="upper right")  # Corrigido a sintaxe do legend
plt.show()
"""