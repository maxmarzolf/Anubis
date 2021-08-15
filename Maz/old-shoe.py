import pandas as pd


data = pd.read_csv('datasets/NetflixOriginals.csv', encoding='latin-1')
data.convert_dtypes()
