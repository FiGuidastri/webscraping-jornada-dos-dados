import streamlit as st
import pandas as pd
import sqlite3

# conectar ao banco de dados
conn = sqlite3.connect(r'C:\Users\filip\OneDrive\Documentos\Projetos Programação\webscraping-jornada-dos-dados\data\mercadolivre.db')

# carregar os dados da tabela
df = pd.read_sql_query("SELECT * FROM playstation", conn)

# fechar a conexão
conn.close()

# Título do aplicativo
st.title("Dashboard de Preços do PS5")

# melhorar layout
st.subheader("💡 Principais KPIs")
col1, col2, col3 = st.columns(3)

#KPI 1 número de produtos
total_itens = df.shape[0]
col1.metric("Total de videogames: ", total_itens)

#KPI 2 preço médio
preco_medio = df['new_price'].mean()
col2.metric("Preço médio: ", f"R$ {preco_medio:.2f}")

# KPI 3 - Top 5 produtos mais baratos
top5 = df.nsmallest(5, 'new_price')[['title', 'new_price']]
top5 = top5.rename(columns={
    'title': 'Produto',
    'new_price': 'Preço (R$)'
})

st.table(top5)


