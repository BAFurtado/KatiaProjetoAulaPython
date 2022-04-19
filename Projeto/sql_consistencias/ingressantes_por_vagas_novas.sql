

-- Identifica os cursos em que a quantidade de ingressantes de vagas novas eh
-- maior do que o numero de vagas novas


SELECT 
	CO_IES, NO_IES, CO_IES_CURSO, NO_CURSO,
	NUM_ING_V_NOVAS, VAGAS_NOVAS, (NUM_ING_V_NOVAS - VAGAS_NOVAS) AS DIFERENCA
FROM censup_2020.cursos 
WHERE (
	NUM_ING_V_NOVAS  > VAGAS_NOVAS 
)
ORDER BY DIFERENCA DESC;

