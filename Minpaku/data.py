import csv
import pandas as pd

def data_half():
    df=pd.read_csv('Data/train.csv')
    half_df=df[:20000]
    half_df.to_csv('Data/half_train.csv')



