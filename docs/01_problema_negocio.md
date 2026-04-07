## Definición del problema de churn

Para este e-commerce, se considerará a un cliente en churn si no realiza una nueva compra dentro de los 60 días posteriores a su última compra registrada.

Este enfoque se centra en un factor clave para la rentabilidad del negocio. Convertir un cliente nuevo en uno recurrente incrementa su valor a largo plazo (Customer Lifetime Value). Por lo tanto, se asume que un cliente que no compra dentro de un periodo de 60 días tiene una alta probabilidad de haber perdido interés o migrado a la competencia.

## Objetivo del modelo

Se desarrollará un modelo de machine learning que permita predecir la probabilidad de que un cliente no vuelva a comprar dentro de los 60 días posteriores a su última compra.

En consecuencia, este modelo permitirá:

- Identificar clientes con alto riesgo de abandono desde etapas tempranas.
    
- Priorizar estrategias de retención mediante descuentos, recomendaciones o campañas personalizadas.
    
- Incrementar la tasa de recompra.
    
- Mejorar el valor de vida del cliente a largo plazo.
    

## Variables relevantes

El comportamiento de churn estará influenciado por el comportamiento de compra del cliente. Para ello, se considerarán variables como:

- Recencia (tiempo desde la última compra)
    
- Frecuencia de compra
    
- Monto de compra
    
- Comportamiento de compra
    
- Antigüedad del cliente
    

## Tipo de modelo

El problema se abordará como una clasificación binaria:

- 1: Cliente en churn (no realiza una compra dentro de 60 días desde su última compra)
    
- 0: Cliente no en churn (realiza una compra dentro de los 60 días)
    

## Impacto esperado

Se espera que el modelo permita:

- Detectar clientes con alto riesgo de deserción.
    
- Incrementar la tasa de recompra.
    
- Optimizar estrategias de marketing.
    
- Reducir la pérdida de clientes.
    
- Aumentar la rentabilidad del negocio a largo plazo.