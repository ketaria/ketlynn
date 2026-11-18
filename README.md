
# Projeto: Análise Estatística do Tempo de Sono

## Descrição

Projeto desenvolvido em Python para analisar os hábitos de sono de uma amostra de pessoas.

O objetivo é utilizar estatística, gráficos e bibliotecas Python para compreender os dados coletados.

## Objetivos

- Organizar os dados de uma pesquisa.
- Calcular a média.
- Calcular a mediana.
- Calcular o desvio padrão amostral.
- Visualizar os resultados em um histograma.
- Identificar a distribuição dos tempos de sono.

## Tecnologias utilizadas

- Python
- NumPy
- Matplotlib
- Google Colab

## Dados da pesquisa

Os dados representam o tempo de sono, em horas, de 15 pessoas.

```python
tempos_sono = [
    6.5, 7, 5, 8, 6, 7.5, 5.5, 6, 9, 7,
    6.5, 4, 8.5, 7, 6
]
```

## Análises realizadas

### Média

Calculada utilizando:

```python
np.mean(tempos_sono)
```

### Mediana

Calculada utilizando:

```python
np.median(tempos_sono)
```

### Desvio padrão

Calculado utilizando o desvio padrão amostral:

```python
np.std(tempos_sono, ddof=1)
```

### Gráfico

O histograma apresenta:

- Barras representando a quantidade de pessoas.
- Linha vermelha representando a média.
- Linha preta tracejada representando a mediana.
- Faixa verde representando o intervalo de um desvio padrão em torno da média.

## Conclusão

A utilização de ferramentas estatísticas permite compreender melhor os hábitos de sono da amostra pesquisada.

A média, a mediana e o desvio padrão ajudam a identificar tendências e variações nos dados.

O projeto também demonstra como Python pode ser utilizado para realizar análises estatísticas e criar visualizações.

## Como executar

1. Instale as bibliotecas:

```bash
pip install numpy matplotlib
```

2. Execute o arquivo:

```bash
python criptogafy.py
```

3. Observe os resultados estatísticos e o gráfico gerado.
