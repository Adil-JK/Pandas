import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/Lenovo/Desktop/iris_data.csv")
print(data.head())
print(data.tail())

print(data["species"].head(5))
print(data["species"].tail(5))


