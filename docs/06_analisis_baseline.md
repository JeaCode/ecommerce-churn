# Análisis de primer baseline

## Desempeño general

El modelo baseline de regresión logística obtiene una accuracy de 0.86 en el conjunto de test. Sin embargo, el problema está desbalanceado (≈17% churn), por lo que la accuracy por sí sola no refleja bien su utilidad para el negocio.

## Clase churn

Para la clase churn, el modelo logra una precisión de 0.67 y un recall de 0.38 (F1 ≈ 0.48). Esto significa que, aunque cuando predice churn suele acertar en 2 de cada 3 casos, solo consigue detectar aproximadamente 4 de cada 10 churners.

## Matriz de confusión

La matriz de confusión muestra que el modelo clasifica correctamente a la mayoría de los clientes que no churnean (96% de recall para la clase 0), pero deja escapar a una parte importante de los clientes en riesgo: 84 de 135 churners reales se predicen como “no churn”.

## Síntesis

Como primer modelo baseline, estos resultados son aceptables: el modelo ya es mejor que una regla trivial de “siempre no churn”. No obstante, para un caso de negocio donde interesa captar la mayoría de clientes en riesgo, será importante trabajar en mejorar el recall de la clase churn en sesiones posteriores (probar otros modelos, ajustar umbrales y/o tratar el desbalance).
