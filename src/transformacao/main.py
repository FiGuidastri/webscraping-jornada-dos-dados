
import pandas as pd
import sqlite3
from datetime import datetime

#definir caminho para o arquivo
df = pd.read_json(r'C:\Users\filip\OneDrive\Documentos\Projetos Programação\webscraping-jornada-dos-dados\data\data.jsonl', lines=True)

# setar o pandas para mostrar todas as colunas
pd.options.display.max_columns = None

# adicionar coluna _source
df['_source'] = 'https://lista.mercadolivre.com.br/ps5#D[A:ps5]'

# adicionar coluna _data_coleta
df['_data_coleta'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Garantir que os dados estão no formato correto
df['old_price'] = df['old_price'].astype(str).str.replace('.', '', regex=False)
df['new_price'] = df['new_price'].astype(str).str.replace('.', '', regex=False)

# convertendo os preços para float
df['old_price'] = df['old_price'].astype(float)
df['new_price'] = df['new_price'].astype(float)

# garatindo somente dados com valores válidos
df = df[(df['old_price'] >= 1000) & (df['new_price'] >= 1000)]

# criar conexão com o banco de dados
conn = sqlite3.connect(r'C:\Users\filip\OneDrive\Documentos\Projetos Programação\webscraping-jornada-dos-dados\data\mercadolivre.db')

# criar tabela no banco de dados
df.to_sql('playstation', conn, if_exists='replace', index=False)

#fechar a conexão
conn.close()

