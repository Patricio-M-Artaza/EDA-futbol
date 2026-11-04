# EDA-futbol
# ¿El mercado paga la edad o el rendimiento?

Análisis exploratorio del valor de mercado de futbolistas de las cinco grandes ligas europeas, a partir de datos de Transfermarkt.

## Pregunta

¿El mercado paga más por la edad o por el rendimiento? ¿Y en qué casos el valor se aleja de lo que el rendimiento sugiere?

## Hipótesis y resultados

| Hipótesis | Resultado |
|---|---|
| **H1.** En menores de 23, el valor de mercado se asocia más con la edad que con el rendimiento (`ga_90`). | **No se confirma.** En 455 jugadores-temporada, el valor se relaciona más con el rendimiento (correlación 0,49) que con la edad (-0,20). |
| **H2.** Pasados los 28 años el valor cae aunque el rendimiento se mantenga. | **Se confirma.** Entre los tramos 23-27 y 28 o más, el valor mediano baja un 67% (de 15 M a 5 M) y el `ga_90` mediano solo un 8%. |
| **H3.** El rendimiento ofensivo explica el valor de forma distinta según la posición, y hay jugadores cuyo valor se aleja mucho de lo que sugiere su rendimiento. | **Se confirma por posición, con matices.** En Attack el rendimiento pesa más que la edad (0,51 contra -0,46); en Midfield pesa más la edad (-0,48 contra 0,37). Además se listan los casos con mayor desajuste entre ranking de valor y ranking de rendimiento (temporada 2025/26). |

## Datos y alcance

- **Fuente:** dataset de Transfermarkt publicado en Kaggle (tablas `players`, `player_valuations` y `appearances`). Enlace de descarga: "(https://github.com/dcaribou/transfermarkt-datasets)"
- **Ligas:** las cinco grandes ligas europeas.
- **Posiciones:** Attack y Midfield.
- **Filtro:** al menos 900 minutos jugados en la temporada.
- **Temporadas:** 2023/24, 2024/25 y 2025/26 (2.579 filas jugador-temporada).
- **Rendimiento:** `ga_90`, goles más asistencias por 90 minutos.
- **Valor:** última valoración de mercado de cada jugador en la temporada.

## Estructura del repositorio

```
├── presentacion/        Presentación e imágenes de los gráficos (img/)
├── src/
│   ├── data/            CSV originales y dataset de 3 temporadas (no se suben a GitHub)
│   ├── notebooks/       Notebook del análisis
│   └── utils/           Función construir_temporada
└── README.md
```

## Cómo reproducirlo

1. Descargar los datos de Transfermarkt y dejar los CSV en `src/data/`.
2. Abrir el notebook de `src/notebooks/` y ejecutarlo de arriba a abajo.
3. Los gráficos se guardan en `presentacion/img/`.

## Limitaciones

- **Asociación, no causa.** Las correlaciones muestran qué variables se mueven juntas, no por qué.
- **El valor de Transfermarkt es una estimación** que ya incorpora la edad y el potencial del jugador. Se muestra que esa estimación sigue ciertos patrones, no cómo se comporta el mercado real de traspasos.
- **`ga_90` solo mide goles y asistencias.** Subestima el aporte de los mediocampistas (recuperar, distribuir), por eso hay mediocampistas defensivos con valor alto y `ga_90` cercano a cero.
- **Sesgo de supervivencia en los veteranos.** Con el filtro de 900 minutos, los mayores de 28 que quedan suelen ser los que siguen rindiendo, así que su rendimiento sale algo inflado.
- **Un mismo jugador puede aparecer en varias temporadas.** Las 2.579 filas no son 2.579 jugadores distintos.
- **No se analiza la liga.** El análisis de H3 se limita a la posición.
- Una fila queda sin tramo de edad por no tener fecha de nacimiento.

## Tecnologías
Python, pandas, NumPy, matplotlib, seaborn.

