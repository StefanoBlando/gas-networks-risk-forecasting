
import pandas as pd
import numpy as np

def rischio_df_preprocessing(rischio_df):
    rischio_df.columns = ["DATA", "IDSAP", "risk_level"]
    rischio_df["YEAR"] = rischio_df["DATA"].apply(lambda x: str(x).split("-")[0])
    rischio_df["MONTH"] = rischio_df["DATA"].apply(lambda x: str(x).split("-")[1])
    rischio_df = rischio_df.drop(columns="DATA")
    rischio_df = rischio_df.astype(float)
    return rischio_df

def tratte_disp_df_preprocessing(tratte_disp_df):
    tratte_disp_df["YEAR"] = tratte_disp_df["DATA"].apply(lambda x: x.split("-")[0])
    tratte_disp_df["MONTH"] = tratte_disp_df["DATA"].apply(lambda x: x.split("-")[1])
    tratte_disp_df = tratte_disp_df[["YEAR", "MONTH", "IDSAP"]]
    tratte_disp_df["dispersione"] = 1
    tratte_disp_df = tratte_disp_df.groupby(["IDSAP", "YEAR", "MONTH"]).sum()["dispersione"].to_frame().reset_index()
    tratte_disp_df = tratte_disp_df.astype(float)
    return tratte_disp_df

def extract_coordinates(geometry):
    if geometry.geom_type == 'MultiLineString':
        coords = [list(line.coords) for line in geometry.geoms]
    else:
        coords = list(geometry.coords)
    n = len(coords[0])
    coords = np.squeeze(np.array(coords)).T.mean(axis=1)
    return coords[0], coords[1], n

def tratte_gas_preprocessing(tratte_gas_df):
    if "YEAR" not in tratte_gas_df.columns:
        tratte_gas_df["YEAR"] = 2023

    avg_x, avg_y, n_dislocazioni = [], [], []
    for geom in tratte_gas_df["geometry"]:
        x, y, n = extract_coordinates(geom)
        avg_x.append(x)
        avg_y.append(y)
        n_dislocazioni.append(n)

    tratte_gas_df["n_dislocazioni"] = n_dislocazioni
    tratte_gas_df["avg_x"] = avg_y
    tratte_gas_df["avg_y"] = [-i for i in avg_x]
    tratte_gas_df["AGE"] = tratte_gas_df["YEAR"] - tratte_gas_df["ANNO_POSA"]
    tratte_gas_df = tratte_gas_df.drop(columns="geometry")
    tratte_gas_df = tratte_gas_df.astype(float)
    return tratte_gas_df
