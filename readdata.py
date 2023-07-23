import os
import pandas as pd
import re

# only for csv text data

def read_data(filepath):
    try:
        df_raw = pd.read_csv(filepath)
        print("Read lines: ", len(df_raw))
        return df_raw
    except:
        print("Cannot read file")


