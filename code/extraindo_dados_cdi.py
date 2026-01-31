import requests
from datetime import datetime
import pandas as pd
import psycopg2

#datas de inicio e fim para extracao dos dados do CDI (PRETENDO AUTOMATIXAR FUTURAMENTE)

data_inicial = '01/01/2025'
data_final = '31/12/2025'
response = requests.get(f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}')

data = response.json()
# transformar em dataframe e ajustar os valores
df = pd.DataFrame(data)
df['valor'] = df['valor'].replace(',','.').astype(float) #converter para float e substituir virgula por ponto
df['data_de_referencia'] = pd.to_datetime(df['data'], format='%d/%m/%Y').dt.date #converter para data
df['capturado_em'] = datetime.now() #data de captura dos dados


# conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    dbname="patrimonio_db",
    user="postgres",
    password="admin",
    port=5432
)
cursor = conn.cursor()
# calcular o fator acumulado do CDI
CDI = df['valor'] 
fator_diario = 1 + (CDI / 100)
df["fator_acumulado_cdi"] = fator_diario.cumprod()


# inserir cada linha do DataFrame
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO cdi_testefake (
            valor,
            data_de_referencia,
            capturado_em,
            fator_acumulado_cdi
        )
        VALUES (%s, %s, %s, %s)
    """, (
        row["valor"],
        row["data_de_referencia"],
        row["capturado_em"],
        row["fator_acumulado_cdi"]
    ))


conn.commit()
cursor.close()
conn.close()
print("Dados inseridos com sucesso!")