# Lista de features seleccionadas

- Tenure: Si los clientes son más antiguos, se tiene menos probabilidad de churn.
- Complain: Si los clientes más se quejan, existe más probabilidad de churn.
- MaritalStatus y PreferedOrderCat: Variables que pueden explicar algunas diferencias entre segmentos.

# Lista de columnas no elegidas

Como se ve en el apartado anterior, sólo se eligieron 4 para este primer modelo de churn. El resto de columnas se descartó ya que no muestran una relación clara con el churn, como se ha evidenciado en el EDA, o requerían un análisis mucho más profundo como la variable SatisfactionScore u otras.

- WarehouseToHome y NumberOfAddress: En el análisis exploratorio inicial no se observaron diferencias fuertes en su distribución entre clientes churn y no churn. No se identificó un patrón de negocio evidente (por ejemplo, que vivir más lejos del almacén o tener más direcciones esté claramente asociado a irse).

- NumberOfDeviceRegistered: La media de dispositivos registrados es muy similar para clientes churn y no churn, lo que sugiere que esta variable, al menos de forma directa, no discrimina bien el churn.

- DaySinceLastOrder: Aunque conceptualmente podría relacionarse con abandono, las medias por grupo son relativamente cercanas y el patrón no es tan claro como en otras variables. Para mantener un conjunto de features pequeño y explicable, se priorizó Tenure y Complain, dejando DaySinceLastOrder para análisis posterior más detallado (por ejemplo, categorizándolo en rangos de días).

- SatisfactionScore: La distribución de la puntuación de satisfacción es muy similar entre churn y no churn, y en algunos casos los clientes churn incluso presentan valores medios de satisfacción algo mayores que los no churn.
