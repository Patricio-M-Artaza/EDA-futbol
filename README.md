# EDA-futbol
# ¿Se paga por la edad o por el rendimiento? Mercado de futbolistas en las 5 grandes ligas

Analisis exploratorio de datos (EDA) sobre el valor de mercado de los futbolistas
de Premier League, LaLiga, Serie A, Bundesliga y Ligue 1.
Proyecto individual.

## Pregunta
¿El mercado paga más por la edad o por el rendimiento? ¿Dónde hay jugadores
sobrevalorados o infravalorados?

## Hipótesis
1. En menores de 23, el valor de mercado se asocia más con la edad que con el rendimiento.
2. Pasados los 28, el valor cae aunque el rendimiento (goles + asistencias por 90 min) se mantenga.
3. Existen jugadores con un valor muy distinto al que sugiere su rendimiento, dentro de su posición.

## Datos
[Transfermarkt datasets](https://github.com/dcaribou/transfermarkt-datasets)
(descargados de Kaggle): `players`, `player_valuations` y `appearances`.
Los CSV no se incluyen en el repo por su tamaño; hay que descargarlos y colocarlos en `src/data/`.

## Alcance y limitaciones
- **Rendimiento = goles + asistencias por 90 minutos (`ga_90`).** Mide solo la contribución ofensiva. Los jugadores de rol defensivo o de construcción (por ejemplo, mediocentros defensivos o porteros) quedan con valores bajos sin que eso implique peor rendimiento.
- Se analizan solo **delanteros y mediocampistas** de las 5 grandes ligas. Defensas y porteros quedan fuera porque `ga_90` no refleja su trabajo.
- Se incluyen solo jugadores con **900 minutos o más** en la temporada, para evitar valores inflados por pocos minutos. Esto deja fuera a suplentes y a muchos juveniles.
- **Valor de mercado ≠ precio pagado.** Es la estimación de Transfermarkt, no el dinero de un traspaso.
- Los resultados muestran **asociaciones**, no causas.

## Estructura
- `src/memoria.ipynb`: resumen del análisis
- `src/notebooks/`: notebooks de pruebas
- `src/utils/`: funciones auxiliares
- `src/data/`: datos (no incluidos)
- `presentacion/`: presentación final



## Tecnologías
Python, pandas, NumPy, matplotlib

