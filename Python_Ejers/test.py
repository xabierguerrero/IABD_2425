import pandas as pd
import numpy as np

pokemon_bw_data="./Python_Ejers/pokemon_bw.csv"
pokemon_bw_df = pd.read_csv(pokemon_bw_data)
print(pokemon_bw_df.head(9))