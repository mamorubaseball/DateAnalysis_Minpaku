import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import csv

head='id,accommodates,amenities,bathrooms,bed_type,bedrooms,' \
     'beds,cancellation_policy,city,cleaning_fee,description,' \
     'first_review,host_has_profile_pic,host_identity_verified,' \
     'host_response_rate,host_since,instant_bookable,last_review,' \
     'latitude,longitude,name,neighbourhood,number_of_reviews,' \
     'property_type,review_scores_rating,room_type,thumbnail_url,zipcode,y'
head_lst = head.split(',')
standscaler_ok_lst=['accommodates','bathrooms','bedrooms','beds','number_of_reviews','review_scores_rating','y']

#標準化
#pandas_dataの基本操作
"""
df=pd.DataFrame()
a=np.array([1,2,3])
df['a']=[1,2,3]
df['b']=a
print(df)

ここで作成したdfをcsvファイルへ移動
df.tp_csv(file)

# 目的変数を追加
boston_dfにカラム名PRICEとして、bostonのデータtargetをPandasのデータフレームに変換して格納します。
最右端の列に目的変数となる「PRICE」が加わります。
boston_df['PRICE'] = pd.DataFrame(boston.target)
print(boston_df)

列の複数指定
df[[A,B,C]]
"""
def zscore(x, axis = None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd  = np.std(x, axis=axis, keepdims=True)
    zscore = (x-xmean)/xstd
    return zscore

def standscaler():
    # df_s=pd.DataFrame(columns=standscaler_ok_lst)
    df=pd.read_csv('Data/pred.csv')
    df_s=pd.DataFrame()
    for i in range(6):
        sc = StandardScaler()
        sample_data = np.array(df[standscaler_ok_lst[i]])
        x_std=zscore(sample_data)
        # x_std = sc.fit_transform(sample_data.reshape(-1, 1))
        df_s[standscaler_ok_lst[i]]=x_std
    df_s.to_csv('Data/missing_pred_x_std.csv')

def practice_standscaler():
    df=pd.read_csv('Data/no_missing_data.csv')
    sc=StandardScaler()
    sample_data=np.array(df[standscaler_ok_lst[1]])
    x_std=sc.fit_transform(sample_data.reshape(-1,1))


if __name__ == '__main__':
    standscaler()

