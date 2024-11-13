import pandas as pd
import yaml
import time

with open("params.yaml") as f:
    params = yaml.safe_load(f)

def load_data(path):
    return pd.read_csv(path)

def preprocess(data):
    # Example preprocessing: handling missing values and encoding
    # data = data.fillna(data.mean())
    return data

if __name__ == "__main__":
    data = load_data(params["data_path"])
    processed_data = preprocess(data)

    processed_data.to_csv(params["processed_data_path"], index=False)
