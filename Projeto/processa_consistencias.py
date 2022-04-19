"""
Processa os scripts de inconsistências do banco de dados e gera
relatórios em Excel com o resultado.
"""

import os  # biblioteca para interagir com o sistema operacional
import duckdb  # biblioteca de conexão com o banco de dados DuckDB
import pandas as pd

# Constantes do projeto

DUCKDB_DATABASE = r'C:\Users\katia\PycharmProjects\AulaIPEA\Projeto\censup2020.duckdb'
DIR_SQL_CONSISTENCIAS = r'C:\Users\katia\PycharmProjects\AulaIPEA\Projeto\sql_consistencias'
DIR_XLSX_CONSISTENCIAS = r'C:\Users\katia\PycharmProjects\AulaIPEA\Projeto\resultado_consistencias'

# Conexão com banco de dados
con = duckdb.connect(DUCKDB_DATABASE)

# Loop para processar os scripts
for sql_file_name in os.listdir(DIR_SQL_CONSISTENCIAS):

    # sql_file_name = os.listdir(DIR_SQL_CONSISTENCIAS)[0]  # FIXME: SÓ PARA TESTE!
    sql_file_path = os.path.join(DIR_SQL_CONSISTENCIAS, sql_file_name)

    # Carrega o script sql na memória
    with open(sql_file_path, 'r') as sql_file:
        sql_file_lines = sql_file.readlines()

    sql_query = ''.join(sql_file_lines)
    # print(sql_query)

    # Executa o script sql e guarda em um pandas DataFrame
    resultado = pd.read_sql_query(sql_query, con)

    # Pula a execução de relatórios sem resultados
    num_linhas = resultado.shape[0]
    if num_linhas == 0:
        continue

    xlsx_file_name = os.path.splitext(sql_file_name)[0] + '.xlsx'
    xlsx_file_path = os.path.join(DIR_XLSX_CONSISTENCIAS, xlsx_file_name)

    # Exporta a tabela de inconsistências para o Excel
    # O argumento 'engine' pode ser 'openpyxl' ou 'xlsxwriter'
    with pd.ExcelWriter(xlsx_file_path, engine='xlsxwriter') as xlsx_file:
        resultado.to_excel(xlsx_file, sheet_name="Resultado", index=False)

# Fecha a conexão com o banco de dados
con.close()
