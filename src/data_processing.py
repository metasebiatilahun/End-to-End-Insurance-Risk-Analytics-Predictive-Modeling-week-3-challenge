
import pandas as pd

def load_data(path):
    return pd.read_csv(path, parse_dates=['ClaimDate'])

def compute_loss_ratio(df):
    # handle zero premium
    df = df.copy()
    df['TotalPremium'] = df['TotalPremium'].replace(0, pd.NA)
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
    return df
