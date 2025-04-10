
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from ctgan import CTGAN

def preprocess_for_ctgan(df, numerical_columns, categorical_columns):
    numerical_columns = [col for col in numerical_columns if col in df.columns]
    categorical_columns = [col for col in categorical_columns if col in df.columns]

    if numerical_columns:
        df[numerical_columns] = MinMaxScaler().fit_transform(df[numerical_columns])

    columns_for_training = numerical_columns + categorical_columns
    return df, columns_for_training, categorical_columns

def train_ctgan(df, columns_for_training, categorical_columns, epochs=100, batch_size=500):
    ctgan = CTGAN(
        embedding_dim=128,
        generator_dim=(256, 256),
        discriminator_dim=(256, 256),
        generator_lr=2e-4,
        discriminator_lr=2e-4,
        batch_size=batch_size,
        epochs=epochs,
        verbose=True
    )
    ctgan.fit(df[columns_for_training], discrete_columns=categorical_columns)
    return ctgan

def generate_synthetic_data(ctgan, original_df, n_samples=1200):
    synthetic_data = ctgan.sample(n_samples)
    for col in original_df.columns:
        if col not in synthetic_data.columns:
            synthetic_data[col] = 0
    synthetic_data = synthetic_data[original_df.columns]
    return synthetic_data

def save_synthetic_data(synthetic_data, filename='augmented_gas_dispersion_data_ctgan.csv'):
    synthetic_data.to_csv(filename, index=False)
