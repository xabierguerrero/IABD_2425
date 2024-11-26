import pandas as pd
import time
import os


fichero_csv="./datos/2018.csv"
fichero_parquet="./datos/2018.parquet.gzip"


vuelos_df = pd.read_csv(fichero_csv)
print(vuelos_df.head())

start_time = time.time()
vuelos_df.to_parquet(fichero_parquet,compression="gzip")
tiempo=time.time() - start_time


parquet_stats=os.stat(fichero_parquet)


vuelos_df_2=pd.read_parquet(fichero_parquet)
print(vuelos_df_2.head())

print("Tiempo de creacion del archivo parquet:",tiempo)
print("Tamaño del archivo parquet(Bytes):",parquet_stats.st_size)
print(vuelos_df.info())