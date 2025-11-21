
import pandas as pd
import matplotlib.pyplot as plt

file_name = './data/seoul-metro-inout.csv'
df_raw = pd.read_csv(file_name)
df_raw = df_raw.set_index('station_code')

print('-'*50)
print(df_raw)

