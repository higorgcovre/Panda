# Lógica de programação

# Passo 0 - Entender o desafio que você quer resolver
# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta vendas)
import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir("C:\\Users\\Hígor Covre\\Desktop\\Python\\Vendas")
print(lista_arquivo)

# criando uma tabela do python vazia
tabela_total = pd.DataFrame()

# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivo:
    # se tem "Vendas" no nome do arquivo, então
    if "Vendas" in arquivo:
        # importar o arquvio
        tabela = pd.read_csv(
            f"C:\\Users\\Hígor Covre\\Desktop\\Python\\Vendas\\{arquivo}")
        # adicionando conteudo a tabela vazia
        tabela_total = tabela_total._append(tabela)


# Passo 3 - Tratar / Compilar as bases de dados
print(tabela_total)

# Passo 4 - Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto')[["Quantidade Vendida"]].sum().sort_values(by="Quantidade Vendida", ascending=False)

#tabela_produtos = tabela_total[["Quantidade Vendida"]]
print(tabela_produtos)


# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto')[['Faturamento']].sum().sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_lojas = tabela_total.groupby('Loja')[['Faturamento']].sum().sort_values(by='Faturamento', ascending=False)
print(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show() 