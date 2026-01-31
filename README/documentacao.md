📊 Projeto: Acompanhamento de Patrimônio vs CDI/Selic (Power BI + Python + SQL)

🎯 Objetivo do projeto

Criar um dashboard em Power BI para acompanhar a evolução do meu patrimônio ao longo do tempo e compará-lo com um benchmark de renda fixa (CDI), utilizando dados reais e cálculos de crescimento acumulado.

O foco do projeto é:
Comparar desempenho real do patrimônio vs rendimento teórico da Selic
Trabalhar com séries temporais financeiras
Construir uma base sólida e flexível para automatização futura
Aplicar boas práticas de modelagem, DAX e engenharia de dados básica

🧱 Arquitetura geral

O projeto é dividido em três partes principais:

# 1 Python (Extração de dados)

Responsável por:
Extração automática de dados do CDI / Selic via API pública
Tratamento do meu saldo
Envio de dados transformados para o banco de dados no SQL

# 2 SQL (Armazenamento de Dados e Criação de Constrainsts)

Responsável por:
Armazenar os dados estraidos em tabelas

# 3 Power BI (Modelagem + Visualização)

Responsável por:
Criação de medidas DAX
Visualização comparativa em gráficos de linha

Isso permite:

Uso correto de funções de inteligência temporal
Comparações consistentes entre patrimônio e benchmark
Escalabilidade do modelo no futuro

💰 Tabela de Patrimônio

Contém as colunas:
instituicão
saldo
data_de_referência(Data em que o saldo se encontra no determinado valor)
capturado_em(datetime em que os dados foram extraidos)
crescimento(o cresciento percentual comparado ao mês anterior)
AnoMes

A partir dela, foram criadas medidas para:

Patrimônio inicial
Patrimônio Atual
Saldo Real Mensal //(saldo mensal em reais)
diferença %
Diferença Absoluta(R$)
Patrimonio Final Simulado no cdi

✔️ Meses sem dados

Quando não existe dado em determinado mês:
O gráfico mantém o último valor conhecido
Evita quedas artificiais para zero
Garante continuidade visual e analítica

📈 Tabela CDI / Selic

Contém as Colunas:

Os dados não representam o “valor do CDI”, mas sim o fator diário de rendimento, permitindo simular corretamente quanto um capital renderia ao longo do tempo.

O crescimento foi calculado de forma exponencial (juros compostos), respeitando a lógica financeira real.
Não é feita soma de percentuais. Cada período rende sobre o valor acumulado anterior.

📅 Tabela Calendário

Foi criada uma tabela calendário pelo próprio Power BI dedicada, utilizada como dimensão de tempo e relacionada às demais tabelas por data.

Contém as colunas:
Date
Ano
MesNumero
MesNome
AnoMes

## Python — Extração de Dados

    Os códigos em Python foram divididos em 2 Arquivos:

# extraindo_dados_cdi.py

Consumo de API pública do Banco Central
Extração dos dados de rendimento diário (CDI)
Criação de colunas para o banco de dados
Transformação dos dados
Upload dos dados para o banco de dados.
Essa parte já está funcional e automatizada.

# extraindo_dados_meus.py

Coleta do Saldo Atual(essa parte deve ser feita manualmente)
Tratamento do Saldo
Criação de novas colunas para serem adicionadas no banco de dados
Upload dos dados para o banco de dados

⚠️ Limitação atual

❌ Não foi possível automatizar a extração do saldo da corretora

Motivo:
A corretora só disponibiliza APIs oficiais para contas PJ
Não há API pública ou documentação para contas PF
Automatização via scraping pode violar termos de uso(além de não dar certo por conta do token de autenticação)
Por enquanto, o saldo do patrimônio é atualizado manualmente.

Essa limitação já está mapeada e faz parte do roadmap do projeto.

# Próximos Passos (Roadmap)

Automatizar a execução do script Python (ex: agendador / Airflow no futuro)
Melhorar o layout e design do dashboard
Tornar a atualização do patrimônio mais fluida (se surgir API oficial)

# Aprendizados do Projeto

Tratamento de dados com python
Integração de python com API
Diferença entre taxa e rendimento efetivo
Importância de juros compostos em benchmarks
Uso prático de DAX para cenários reais
Integração entre Python, SQL e Power BI

# Considerações finais

Este projeto foi pensado como um primeiro projeto real, com foco em aprendizado, flexibilidade e evolução contínua.
Não é um produto final fechado, mas uma base sólida para crescer futuramente.
