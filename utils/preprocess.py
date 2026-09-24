import pandas as pd

def preprocess_input(input_data):
    # Create a DataFrame from input data
    df = pd.DataFrame([input_data])

    # Handle categorical data
    df["City"] = df["City"].astype("category").cat.codes
    df["Weapon Used"] = df["Weapon Used"].astype("category").cat.codes

    # Convert time to numeric
    df["Time of Occurrence"] = pd.to_datetime(df["Time of Occurrence"]).dt.hour

    return df
