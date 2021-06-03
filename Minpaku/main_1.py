import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model

"""
使えるデータが変更となったので、やり直し。
Columns:[accommodates, amenities, bed_type, cancellation_policy, city, cleaning_fee, description, instant_bookable, latitude, longitude, name, number_of_reviews, property_type, room_type]

数値データ：[accommodates,number_of_reviews]
相関関係にあるデータを使用する
使用するデータ：[accommodates, amenities,number_of_reviews,review_score_rating,city,property_type]

気をつけること
トレーニングは欠損値のある列があってもok.そのデータは学習に使わなければいいから。
テスト（予測に使うデータは欠損値あるとプログラムは動かない)


"""

#質的変数（説明変数が文字列であるデータの処理)、相関関係のあるデータを抽出
def make_train_data(origin,result):
    #数値計算
    df=pd.read_csv('{}'.format(origin))
    #アメニティの種類数
    amenities=[]
    for i in df['amenities']:
        amenities.append(len(i))
    train_df=pd.get_dummies(df['city'])
    train_df['amenities']=np.array(amenities)
    train_df['accommodates']=np.array(df['accommodates'])
    train_df['number_of_reviews']=np.array(df['number_of_reviews'])
    train_df['review_scores_rating']=np.array(df['review_scores_rating'])
    train_df['review_scores_rating'].replace('',np.nan, inplace=True)
    #下のままだと、代入されていないからダメ
    # train_df['review_scores_rating'].fillna(train_df['review_scores_rating'].mean())
    train_df=train_df.fillna(train_df.mean())
    # train_df['y']=df['y']
    train_df.to_csv('{}'.format(result),index=False)

#標準化(平均0、分散1)
def std_data(origin,result):
    df=pd.read_csv('{}'.format(origin))
    # df.drop('y',axis=1)
    sc=StandardScaler()
    #Standscaler使うときは以下の3つが必要
    sc.fit(df)
    sc.fit_transform(df)
    train_std = pd.DataFrame(sc.transform(df), columns=df.columns)
    # train_std['y']=df['y']
    train_std.to_csv('{}'.format(result))

#正規化(最小値0,最大値1)
def min_max_normalization(origin,result):
    df=pd.read_csv('{}'.format(origin))
    # df.drop('y',axis=1)
    sc=MinMaxScaler()
    #Standscaler使うときは以下の3つが必要
    sc.fit(df)
    sc.fit_transform(df)
    train_std = pd.DataFrame(sc.transform(df), columns=df.columns)
    # train_std['y']=df['y']
    train_std.to_csv('{}'.format(result),index=False)

def Linermodel():
    df=pd.read_csv('csv1/train_minmax.csv',index_col=0)
    model=linear_model.LinearRegression()
    df1=df.drop(columns=['y'])
    df2=df['y']
    model.fit(df1,df2)
    coef=model.coef_
    intercept=model.intercept_
    print(df1)
    print('========df1')
    print(df2)
    print('========df1')

    print(coef)
    print(intercept)
    return coef,intercept
#予測値の算出
def y_pred_df():
    coef,intercept=Linermodel()
    pred_x=pd.read_csv('csv1/pred_minmax.csv',index_col=0)
    y_pred=np.dot(np.array(coef),np.array(pred_x).T)+intercept
    df=pd.DataFrame()
    df['y']=y_pred
    df.to_csv('csv1/submit.csv')
if __name__ == '__main__':
    original='csv1/train.csv'
    result='csv1/train_minmax.csv'
    original1='csv1/pred.csv'
    result1='csv1/pred_minmax.csv'
    # min_max_normalization(original1,result1)
    y_pred_df()


#標準化10この特徴量
"""
coef:
[ -0.62153666   0.44049018 -11.96144655  10.03741561  -8.49943993
  -3.16539206  19.0395554   -3.39037192  89.77000656 -15.86780538
   9.20910563]
intercept:160.16364715830377
"""

#正規化10個の特徴量
"""
[-4.23753012e+13 -4.23753012e+13 -4.23753012e+13 -4.23753012e+13
 -4.23753012e+13 -4.23753012e+13 -4.55361328e+01  6.25414795e+02
 -2.53005371e+02  1.07310181e+02]
42375301181602.664
"""













