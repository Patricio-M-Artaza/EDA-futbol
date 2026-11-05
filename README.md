# EDA-futbol
# ¿El mercado paga la edad o el rendimiento?

Analisis exploratorio del valor de mercado de futbolistas de las cinco grandes ligas europeas, a partir de datos de Transfermarkt.

## Pregunta

¿El mercado paga mas por la edad o por el rendimiento? ¿Y en que casos el valor se aleja de lo que el rendimiento sugiere?

## Hipotesis y resultados

| Hipotesis | Resultado |
|---|---|
| **H1.** En menores de 23, el valor de mercado se asocia mas con la edad que con el rendimiento (`ga_90`). | **No se confirma.** En 455 jugadores-temporada, el valor se relaciona mas con el rendimiento (correlacion 0,49) que con la edad (-0,20). |
| **H2.** Pasados los 28 años el valor cae aunque el rendimiento se mantenga. | **Se confirma.** Entre los tramos 23-27 y 28 o mas, el valor mediano baja un 67% (de 15 M a 5 M) y el `ga_90` mediano solo un 8%. |
| **H3.** El rendimiento ofensivo explica el valor de forma distinta segun la posicion, y hay jugadores cuyo valor se aleja mucho de lo que sugiere su rendimiento. | **Se confirma por posicion, con matices.** En Atacante(Attack) el rendimiento pesa mas que la edad (0,51 contra -0,46); en Mediocampista(Midfield) pesa mas la edad (-0,48 contra 0,37). Ademas se listan los casos con mayor desajuste entre ranking de valor y ranking de rendimiento (temporada 2025/26). |

## Datos y alcance

- **Fuente:** dataset de Transfermarkt publicado en Kaggle (tablas `players`, `player_valuations` y `appearances`). Enlace de descarga: "(https://github.com/dcaribou/transfermarkt-datasets)"
- **Ligas:** Las cinco grandes ligas europeas: LaLiga(Espana), Premier League(Inglaterra), Bundesliga(Alemania), Ligue 1(Francia), Serie A(Italia).
- **Rendimiento:** `ga_90` (goles mas asistencias por 90 minutos), calculado solo con partidos de liga de LaLiga, Premier League, Serie A, Bundesliga y Ligue 1. No se cuentan Champions League ni copas.
- **No se compara entre ligas.** Los jugadores de las cinco ligas se analizan juntos y se separan solo por posicion.
- **Posiciones:** Atacante(Attack) y Mediocampista(Midfield).
- **Filtro:** al menos 900 minutos jugados en la temporada.
- **Temporadas:** 2023/24, 2024/25 y 2025/26 (2.579 filas jugador-temporada).
- **Rendimiento:** `ga_90`, goles mas asistencias por 90 minutos.
- **Valor:** ultima valoracion de mercado de cada jugador en la temporada.

## Estructura del repositorio

```
├── presentacion/        Presentacion e imagenes de los graficos (img/)
├── src/
│   ├── data/            CSV originales y dataset de 3 temporadas (no se suben a GitHub)
│   ├── notebooks/       Notebook del analisis
│   └── utils/           Funcion construir_temporada
└── README.md
```

## Como reproducirlo

1. Descargar los datos de Transfermarkt y dejar los CSV en `src/data/`.
2. Abrir el notebook de `src/notebooks/` y ejecutarlo de arriba a abajo.
3. Los graficos se guardan en `presentacion/img/`.

## Limitaciones

- **Asociacion, no causa.** Las correlaciones muestran que variables se mueven juntas, no por que.
- **El valor de Transfermarkt es una estimacion** que ya incorpora la edad y el potencial del jugador. Se muestra que esa estimacion sigue ciertos patrones, no como se comporta el mercado real de traspasos.
- **`ga_90` solo mide goles y asistencias.** Subestima el aporte de los mediocampistas (recuperar, distribuir), por eso hay mediocampistas defensivos con valor alto y `ga_90` cercano a cero.
- **Sesgo de supervivencia en los veteranos.** Con el filtro de 900 minutos, los mayores de 28 que quedan suelen ser los que siguen rindiendo, asi que su rendimiento sale algo inflado.
- **Un mismo jugador puede aparecer en varias temporadas.** Las 2.579 filas no son 2.579 jugadores distintos.
- **No se analiza la liga.** El análisis de H3 se limita a la posicion.
- Una fila queda sin tramo de edad por no tener fecha de nacimiento.

## Tecnologias
Python, pandas, NumPy, matplotlib, seaborn.

