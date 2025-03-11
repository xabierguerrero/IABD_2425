#! /usr/bin/python3
import pandas as pd
import seaborn as sns
from hdfs import InsecureClient
import io

df_titanic = sns.load_dataset('titanic')

url = "http://master:9870"
usuario = "ubuntu"
client = InsecureClient(url, usuario)
fichero = "/practicas/titanic.csv"


buffer=io.StringIO()
df_titanic.to_csv(buffer,index=False)

with client.write(fichero, encoding='utf-8') as writer:
        writer.write(buffer.getvalue())

