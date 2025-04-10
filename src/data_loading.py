
import os
import pandas as pd
import geopandas as gpd

def list_all_files(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def load_datasets(base_path):
    all_files = list_all_files(base_path)

    tratte_disp = [p for p in all_files if 'tratte_disp' in p]
    tratte_gas = [p for p in all_files if 'tratte_gas' in p]
    rischio = [p for p in all_files if 'part' in p]

    tratte_disp_df = pd.concat([pd.read_parquet(f) for f in tratte_disp], ignore_index=True)
    tratte_gas_df = [gpd.read_parquet(f) for f in tratte_gas]
    rischio_df = pd.concat([pd.read_parquet(f) for f in rischio], ignore_index=True)

    return tratte_disp_df, tratte_gas_df, rischio_df
