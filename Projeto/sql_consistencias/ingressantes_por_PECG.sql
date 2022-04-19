-- Identifica os cursos em que todos os ingressantes ingressaram  
-- com forma de ingresso igual a Convênico PEC-G


SELECT 
    CO_IES, NO_IES, CO_IES_CURSO, NO_CURSO,
    NUM_ING_V_DECJ,  NUM_ING
FROM censup_2020.cursos 
WHERE (
    NUM_ING_V_PECG = NUM_ING and NUM_ING > 0 
);

