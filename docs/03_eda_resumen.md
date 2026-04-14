# EDA – Resumen inicial

## 1. Dataset usado

- Observaciones: 3 941 filas, cada una representa un cliente.
- Variables: 11 columnas con información sobre relación con la empresa (antigüedad, distancia al almacén, quejas, satisfacción, etc.).
- Variable objetivo: `Churn` (binaria), indica si el cliente abandonó o no el negocio.
- Se reemplazaron valores nulos en `Tenure`, `WarehouseToHome` y `DaySinceLastOrder` usando la mediana.

## 2. Distribución de churn

- Proporción de clientes no churn: 83 %.
- Proporción de clientes churn: 17 %.
- El dataset está moderadamente desbalanceado (más clientes que permanecen que los que se van), lo cual es habitual en problemas de churn reales.

## 3. Insights clave de EDA

- Antigüedad (Tenure) está fuertemente asociada al churn: los clientes churn tienen una antigüedad media de 3.72, frente a 11.33 en los clientes no churn. Esto indica que los clientes nuevos están mucho más expuestos a abandonar el negocio.
- Las quejas (Complain) también es una variable importante: los clientes churn presentan un promedio de 0.54 quejas, frente a 0.22 en los clientes no churn. Los clientes que se quejan tienen más probabilidad de irse.
- La variable de satisfacción (SatisfactionScore) no muestra diferencias claras entre grupos; su distribución es muy similar en churn y no churn, por lo que no parece ser un predictor fuerte en esta fase. Incluso, los clientes churn presentan una satisfacción más alta frente los no churn.
- Además de Tenure y Complain, las variables categóricas como PreferedOrderCat y MaritalStatus muestran cambios claros en la composición entre clientes churn y no churn, por lo que se considerarán candidatas del modelo.
- La distribución del churn es relativamente baja (17 %), lo que implica que las métricas del modelo y el tratamiento del desbalance serán relevantes para no ignorar a la minoría de clientes que abandonan. Lo cual se resolverá en etapas posteriores.

## 4. Ideas de variables derivadas

- Binning de Tenure en categorías (por ejemplo: 0–3, 3–6, 6–12, 12+), para capturar y divisar mejor el riesgo de los clientes nuevos y facilitar interpretabilidad.
- Variable binaria `IsNewCustomer` (1 si Tenure < cierto umbral, por ejemplo 3 meses; 0 en caso contrario) para focalizar estrategias de retención temprana.
- Interacciones entre Tenure y Complain (ej. clientes nuevos con quejas) para identificar segmentos especialmente vulnerables.
- Conteos o grupos derivados de otras variables numéricas (p. ej., bandas de DaySinceLastOrder para distinguir clientes activos vs dormidos).

## 5. Próximos pasos

- Profundizar en el análisis de variables categóricas como `PreferedOrderCat` y `MaritalStatus` para entender su relación con el churn.
- Probar modelos de clasificación (árboles, ensembles, etc.) usando `Tenure`, `Complain` y las variables derivadas propuestas.
- Tratar el desbalance de clases con técnicas apropiadas (ajuste de métricas, pesos de clase, undersampling/oversampling).
