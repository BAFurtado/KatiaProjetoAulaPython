

-- Identifica os cursos em que a quantidade de ingressantes de remanescentes é 
-- maior do que o número de vagas remanescentes


SELECT 
	CO_IES, NO_IES, CO_IES_CURSO, NO_CURSO,
	NUM_ING_V_REMA, VAGAS_REMANESCENTE, (NUM_ING_V_REMA - VAGAS_REMANESCENTE) AS DIFERENCA
FROM censup_2020.cursos 
WHERE (
	NUM_ING_V_REMA  > VAGAS_REMANESCENTE 
)
ORDER BY DIFERENCA DESC;

