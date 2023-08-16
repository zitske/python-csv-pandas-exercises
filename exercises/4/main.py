#4)Salvar localmente o seguinte arquivo:  https://raw.githubusercontent.com/emmendorfer/idwr/main/demo/datasets/amazon.csv
#5) Converter os dados lidos para uma matriz do "numpy" usando "pandas".  Utilizar as funções read_csv() e to_numpy() 

import pandas as pd

df = pd.read_csv('amazon.csv')
df.to_numpy()

print(df)