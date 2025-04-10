
import pandas as pd

def aggregate_features_by_codsistema(tratte_gas_df):
    return tratte_gas_df.groupby(['CODSISTEMA', 'YEAR']).agg(
        unique_IDSAP=('IDSAP', 'nunique'),
        materiale_1=('MATERIALE', lambda x: (x == 1).sum()),
        materiale_2=('MATERIALE', lambda x: (x == 2).sum()),
        materiale_3=('MATERIALE', lambda x: (x == 3).sum()),
        materiale_4=('MATERIALE', lambda x: (x == 4).sum()),
        unique_MATERIALE=('MATERIALE', 'nunique'),
        avg_ANNO_POSA=('ANNO_POSA', 'mean'),
        oldest_ANNO_POSA=('ANNO_POSA', 'min'),
        newest_ANNO_POSA=('ANNO_POSA', 'max'),
        avg_DIAMETRO=('DIAMETRO', 'mean'),
        smallest_DIAMETRO=('DIAMETRO', 'min'),
        biggest_DIAMETRO=('DIAMETRO', 'max'),
        tipo_23_pct=('TIPO', lambda x: (x == 23).mean() * 100),
        tipo_24_pct=('TIPO', lambda x: (x == 24).mean() * 100),
        tipo_25_pct=('TIPO', lambda x: (x == 25).mean() * 100),
        avg_x=('avg_x', 'mean'),
        avg_y=('avg_y', 'mean'),
        n_dislocazioni=('n_dislocazioni', 'sum'),
        AGE=('AGE', 'mean'),
        max_n_dislocazioni=('n_dislocazioni', 'max'),
        max_AGE=('AGE', 'max'),
        min_AGE=('AGE', 'min')
    ).reset_index()

def create_dispersion_summary(tratte_disp_df, idsap_codsistema):
    merged = pd.merge(tratte_disp_df, idsap_codsistema, on="IDSAP", how="left").dropna()
    merged = merged.drop(columns="IDSAP")
    grouped = merged.groupby(["CODSISTEMA", "YEAR", "MONTH"]).sum()["dispersione"].reset_index()
    return grouped

def create_lag_features(df, groupby_col='CODSISTEMA', target_col='dispersione', lags=6):
    df = df.sort_values([groupby_col, "YEAR", "MONTH"])
    for lag in range(1, lags + 1):
        df[f'{target_col}_lag_{lag}'] = df.groupby(groupby_col)[target_col].shift(lag)
    return df
