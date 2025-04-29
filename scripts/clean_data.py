import pandas as pd

def clean_dataframe(df):
    df["time"] = pd.to_datetime(df["time"])
    df["updated"] = pd.to_datetime(df["updated"])

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/earthquakes.csv")  
    df_clean = clean_dataframe(df)
    df_clean.to_csv("data/cleaned_data.csv", index=False)
    print("Data cleaned and saved!")

