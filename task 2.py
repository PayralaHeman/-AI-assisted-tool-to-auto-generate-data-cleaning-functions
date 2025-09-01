import pandas as pd
import numpy as np

# Example dataset with missing values & duplicates
data = {
    "Stock": ["AAPL", "AAPL", "GOOG", "MSFT", "MSFT", None],
    "Price": [150, 150, np.nan, 300, 300, 400],
    "Volume": [1000, 1000, 2000, np.nan, 2000, 3000]
}

df = pd.DataFrame(data)
print("📊 Original Data:\n", df)

# --- AI-Assisted Cleaning Functions ---

def handle_missing_values(df, strategy="fill", fill_value=0):
    """
    Handles missing values in a DataFrame.
    strategy: 'drop' -> remove rows with NaN
              'fill' -> replace NaN with fill_value
    """
    if strategy == "drop":
        return df.dropna()
    elif strategy == "fill":
        return df.fillna(fill_value)
    else:
        raise ValueError("Invalid strategy. Use 'drop' or 'fill'.")

def remove_duplicates(df):
    """
    Removes duplicate rows from a DataFrame.
    """
    return df.drop_duplicates()

# Apply cleaning
df_clean = handle_missing_values(df, strategy="fill", fill_value=0)
df_clean = remove_duplicates(df_clean)

print("\n✅ Cleaned Data:\n", df_clean);