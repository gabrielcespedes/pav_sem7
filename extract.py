import pandas as pd

def extract(filepath):
    print("Extrayendo datos.")
    data = pd.read_csv(filepath)
    print(f"len{data} registros detectados.")
    return data