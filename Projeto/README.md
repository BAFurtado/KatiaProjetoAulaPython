# Projeto 

Scripts elaborados para o projeto da aula de introdução ao Python oferecida pelo Mestrado Profissional em Políticas Públicas e Desenvolvimento do
Instituto de Pesquisa Econômica Aplicada -- Ipea.

Objetivos: 
1. Conectar ao banco de dados (simulei com o DuckDB)
2. Executar scripts SQL que estão na pasta `sql_consistencia`
3. Salvar arquivos de resultados na pasta `resultado_consistencia`
sempre que houver registros na consulta SQL.

## How to run

### Requirements

1. Install `duckdb 0.3.2` `píp install duckdb==0.3.2`
2. Install xlsxwriter `pip install xlsxwriter`

# Run

`cd Projeto`
`python processa_consistencias.py`
