import os
import datetime

# import IPython
# import IPython.display
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
# import seaborn as sns
# import tensorflow as tf


df = pd.read_csv('E:/pythonProject/TensorReview/TF_Questions/household_power_consumption.csv', sep=';',
                           infer_datetime_format=True, parse_dates={'Datetime':[0,1]}, header=0, low_memory=False, nrows=86400)

# parse_dates={'datetime':[0,1]}
# inspect tools
# print(df.head())
# print(df.isna().sum())

# dropping NaN values
df.replace('?', 'NaN', inplace=True)
df.drop(columns=['Datetime'], inplace=True)
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

# print(type(df.loc[[6839]]))
# for column in df:
#     print(df[column])
# dfn = df.astype({'Global_active_power':'float64'}).dtypes
print((df['Global_active_power']).mean())
# print(dfn.dtypes)
#
print(df.columns)

