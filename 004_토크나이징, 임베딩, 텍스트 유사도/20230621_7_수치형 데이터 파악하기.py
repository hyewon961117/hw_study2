import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
print(df.head())
print(len(df))
print(df.shape)
print(df.info())