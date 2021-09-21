import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score
from sklearn.metrics import confusion_matrix
import numpy as np
import xgboost as xgb
import pickle
import seaborn as sns
from sklearn import preprocessing
from sklearn.metrics import mean_absolute_error
from sklearn import linear_model
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import requests
from bs4 import BeautifulSoup
import sys
from yahoo_finance_api2.exceptions import YahooFinanceError
from yahoo_finance_api2 import share
import pandas as pd
import streamlit as st
import warnings
warnings.simplefilter('ignore')


def model():
    df=pd.read_csv('tokyo_city.csv')
    df=df[['accommodates','bedrooms','beds','cleaning_fee','city_price','price']].dropna()
    x=df[['accommodates','bedrooms','beds','cleaning_fee','city_price']]
    y=df['price']
    array_x=preprocessing.minmax_scale(x)
    x = pd.DataFrame(array_x)
    n=int(0.8*len(df))
    train_x,train_y=x[:n],y[:n]
    test_x,test_y=x[n:],y[n:]
    model=linear_model.LinearRegression()
    model.fit(train_x,train_y)
    coef=model.coef_
    intercept=model.intercept_
    y_pred=np.dot(np.array(coef),np.array(test_x).T)+intercept
    # 評価関数
    # mean_absolute_error(test_y, y_pred)

def y(x_lst):
    coef=np.array([ 37631.22223465,  63457.61229447, -42512.95306984,  17304.98345339,
            26557.39331928])
    intercept=-1318.9019422050533
    y_pred=np.dot(np.array(coef),np.array(x_lst).T)+intercept
    return y_pred


st.title('Arbnbの価格予測システム')
st.markdown("""
このアプリの使用は **Airbnb ** のデータをリスト化し、平均株価を表示する
* **Python ライブラリ:** base64,sklearn, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** 'https://www.airbnb.jp/'
""")

# st.sidebar.header('場所')
erea_list=['千代田区','中央区','港区','新宿区','文京区','台東区','墨田区','江東区','品川区','目黒区','大田区','世田谷区','渋谷区','中野区','杉並区',
 '豊島区','北区','荒川区','板橋区','練馬区','足立区','葛飾区','江戸川区','八王子市','立川市','武蔵野市',
 '三鷹市','青梅市','府中市','昭島市','調布市','町田市','小金井市','小平市','日野市','東村山市','国分寺市',
 '国立市','福生市','狛江市','東大和市','清瀬市','東久留米市','武蔵村山市',
 '多摩市','稲城市','羽村市','あきる野市','西東京市']
city_dict={'千代田区': 2771400,'中央区': 1300500,'港区': 2009300,'新宿区': 803500,'文京区': 999600,
 '台東区': 916300,'墨田区': 439300,'江東区': 480900,'品川区': 849300,'目黒区': 951300,'大田区': 528200,
 '世田谷区': 636200,'渋谷区': 1311500,'中野区': 597000,'杉並区': 541900,'豊島区': 631800,'北区': 531700,'荒川区': 508900,
 '板橋区': 433100,'練馬区': 394400,'足立区': 314200,'葛飾区': 319700,'江戸川区': 363200,
 '八王子市': 116700,'立川市': 250700,'武蔵野市': 565300,'三鷹市': 414000,'青梅市': 94500,
 '府中市': 292700,'昭島市': 186700,'調布市': 338000,'町田市': 156700,'小金井市': 337900,'小平市': 229900,'日野市': 190800,'東村山市': 187300,
 '国分寺市': 289100,'国立市': 340000,'福生市': 165100,'狛江市': 308800,'東大和市': 169500,
 '清瀬市': 185600,'東久留米市': 215500,'武蔵村山市': 122100,'多摩市': 184400,'稲城市': 228000,'羽村市': 140000,'あきる野市': 98600,'西東京市': 288700}

selected_erea = st.selectbox(
    '宿泊する場所を選択：',
    erea_list
)
#df[['accommodates', 'bedrooms', 'beds', 'cleaning_fee', 'city_price', 'price']].dropna()
accommodates = st.number_input('宿泊人数',0,100,1)
bedrooms=st.number_input('部屋の数',0,100,1)
beds=st.number_input('ベッドの数',0,100,1)
cleaning_fee=st.number_input('クリーニング費用',0,10000000,0)
city_price=city_dict[selected_erea]


x_lst=[accommodates,bedrooms,beds,cleaning_fee,city_price]
array_x=preprocessing.minmax_scale(x_lst)

st.markdown(f"""
あなたの宿泊施設の適切価格は{int(y(array_x))}円です。

データ分析によって、より多くの売り上げをあげたい方の相談をおまちしております。
""")


































