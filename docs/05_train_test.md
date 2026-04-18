
# Análisis de división de dataset en train y test

## Tamaño de train y test

Dividí el dataset en train y test usando un test_size con un 20%.
Train: 3152 (80%)
Test: 789 (20%)

## Distribución de churn en ambos conjuntos

### Distribución global de churn

- No churn: 82.897742%
- Churn: 17.102258%

### Distribución en train (estratificada)

- No churn: 82.899746%
- Churn: 17.100254%

### Distribución en test

- No churn: 82.889734%
- Churn: 17.110266%

## Decisión inicial sobre técnicas para desbalance

El target está desbalanceado (82.897742% no churn y 17.102258% churn). Esto implica que métricas como accuracy no sea útil para el análisis de churn en este dataset.
