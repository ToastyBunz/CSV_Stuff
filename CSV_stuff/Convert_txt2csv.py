import pandas as pd

read_file = pd.read_csv (r'E:\pythonProject\TensorReview\TF_Questions\household_power_consumption.txt', sep=';')
read_file.to_csv (r'E:\pythonProject\TensorReview\TF_Questions\household_power_consumption.csv', sep=';', index=None)
