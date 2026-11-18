
import numpy as np
import matplotlib.pyplot as plt

# Dados da pesquisa: tempo de sono em horas
tempos_sono = [
    6.5, 7, 5, 8, 6, 7.5, 5.5, 6, 9, 7,
    6.5, 4, 8.5, 7, 6
]

# Cálculos estatísticos
media = np.mean(tempos_sono)
mediana = np.median(tempos_sono)

# Desvio padrão amostral
desvio = np.std(tempos_sono, ddof=1)

# Intervalo de um desvio padrão em torno da média
valor_minimo = media - desvio
valor_maximo = media + desvio

# Exibição dos resultados
print(f"Média: {media:.2f} horas")
print(f"Mediana: {mediana:.2f} horas")
print(f"Desvio padrão: {desvio:.2f} horas")

print(
    f"O tempo está entre: "
    f"{valor_minimo:.2f} e {valor_maximo:.2f} horas"
)

# Criação do histograma
plt.hist(
    tempos_sono,
    bins=8,
    color="steelblue",
    edgecolor="black",
    label="Tempo de sono"
)

# Linha da média
plt.axvline(
    media,
    color="red",
    label="Média"
)

# Linha da mediana
plt.axvline(
    mediana,
    color="black",
    linestyle="--",
    label="Mediana"
)

# Faixa de um desvio padrão
plt.axvspan(
    valor_minimo,
    valor_maximo,
    color="green",
    alpha=0.15,
    label="Intervalo de desvio padrão"
)

# Personalização do gráfico
plt.xlabel("Tempo de sono (horas)")
plt.ylabel("Quantidade de pessoas")
plt.title("Análise estatística do tempo de sono")
plt.legend()
plt.show()
