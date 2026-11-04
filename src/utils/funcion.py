import pandas as pd
import numpy as np

def construir_temporada(players, valuations, appearances, inicio, fin, ligas=("ES1", "GB1", "IT1", "L1", "FR1"), min_minutos=900):
    inicio, fin = pd.Timestamp(inicio), pd.Timestamp(fin) # Timestamp representa un punto especifico de tiempo. 

    # Rendimiento por jugador en la temporada
    mask = (appearances["competition_id"].isin(ligas) & (appearances["date"] >= inicio) & (appearances["date"] <= fin))
    rend = (appearances[mask].groupby("player_id")[["minutes_played", "goals", "assists"]].sum().reset_index())

    # Última valoración de la temporada
    val = valuations[(valuations["date"] >= inicio) & (valuations["date"] <= fin)]
    val = val.sort_values("date").groupby("player_id").tail(1) # Solo para que muestre el ultimo dato. 
    val = val[["player_id", "market_value_in_eur"]]

    # Unir, calcular edad y rendimiento
    df = rend.merge(val, on="player_id", how="inner")
    df = df.merge(players[["player_id", "name", "date_of_birth", "position"]], on="player_id", how="left")
    df["edad"] = (fin - df["date_of_birth"]).dt.days / 365.25 # Divido por 365.25 por los anios bisiestos.

    df = df[df["position"].isin(["Attack", "Midfield"]) & (df["minutes_played"] >= min_minutos)].copy()
    df["ga_90"] = (df["goals"] + df["assists"]) / df["minutes_played"] * 90 # Multiplico por 90 que son los minutos de un partido sino daria los "ga_90" por minuto.
    df["temporada"] = f"{inicio.year}/{fin.year}" # Lo uso para decir desde que temporada hasta que temporada quiero que tome. 
    
    return df