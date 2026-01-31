import psycopg2
from datetime import datetime


saldo_raw = 'R$ 5.000,0'# Exemplo de saldo inicial

def tratar_saldo(saldo):
    # Remover o símbolo de moeda e espaços e substitui vírgula por ponto
    saldo = saldo.replace('R$', '').replace(' ', '').replace(',', '.')
    return float(saldo)

saldo_reformulado = tratar_saldo(saldo_raw)

# conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    dbname="patrimonio_db",
    user="postgres",
    password="admin",
    port=5432
)
cursor = conn.cursor()


#criando tabelas adicionais
instituicao = "Santander"
saldo = saldo_reformulado
moeda = "BRL"
data_de_referencia = datetime.now().date()
capturado_em = datetime.now()


# Inserir dados na tabela
cursor.execute("""
    INSERT INTO patrimonio_testefake(
        instituicao,
        saldo,
        moeda,
        data_de_referencia,
        capturado_em
    )
    VALUES (%s, %s, %s, %s, %s)
""", (
    instituicao,
    saldo,
    moeda,
    data_de_referencia,
    capturado_em
))
               
cursor.commit()
cursor.close()
conn.close()
print("Dados inseridos com sucesso!")