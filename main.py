import pandas as pd

def remove_empty_rows(df):
    # if all values are empty
    return df.dropna(how='all')

def remove_empty_columns(df):
    return df.dropna(axis=1, how='all')

def strip_whitespace(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()
    return df.replace('', pd.NA)

# add methods above as custom methods to DataFrame
pd.DataFrame.remove_empty_rows = remove_empty_rows
pd.DataFrame.remove_empty_columns = remove_empty_columns
pd.DataFrame.strip_whitespace = strip_whitespace

if __name__ == "__main__":
    df = pd.read_csv("responses.csv").strip_whitespace().remove_empty_rows().remove_empty_columns()
    df.to_csv("responses_clean.csv", index=False)
