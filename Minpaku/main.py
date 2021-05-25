import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
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
"""
１amaenitiesはamenitieの数で調査
２amenitiesの種類で調査
"""

"""
columns=1~27
row=50000
データ数があまりにも多すぎるので、50000ある中からランダムで10000件取得
"""

def is_correlation(n):
    head_lst = head.split(',')
    df=pd.read_csv('Data/train.csv')
    df.sample(n=10000)
    x=np.array(df[head_lst[n]])
    y=np.array(df[head_lst[28]])

    # plt.scatter(eval_x, eval_y)
    plt.xlabel(head_lst[n],fontname="MS Gothic")
    plt.ylabel('price')
    plt.scatter(x,y)
    # save as png
    plt.savefig('Data/{}.png'.format(head_lst[n]))
    plt.show()
    plt.close()
    #グラフを作成する
def make_rellation(n):
    df = pd.read_csv('Data/train.csv')
    df=df.sample(n=10000)
    a = df[head_lst[n]]
    lst=[]
    for i in a:
        lst.append(len(i.split(',')))
    x=np.array(lst)
    y = np.array(df['y'])

    # plt.scatter(eval_x, eval_y)
    plt.xlabel('amenities',fontname="MS Gothic")
    plt.ylabel('price')
    plt.scatter(x,y)
    # save as png
    plt.savefig('{}.png'.format(head_lst[n]))

def zscore(x, axis = None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd  = np.std(x, axis=axis, keepdims=True)
    zscore = (x-xmean)/xstd
    return zscore
#次元圧縮なしで重回帰分析
# n=len(y_pred_std)
# y_h,y_s=zscore()
def LR_no_stand():
    model=linear_model.LinearRegression()
    df=pd.read_csv('Data/x_std.csv')
    # 説明変数と目的変数の作成
    # axis=1で列の削除,axis=0で行の削除。default:axis=0
    y_train=df['y']
    x_train=df.drop(['y','s'],axis=1)
    model.fit(x_train,y_train)
    coef=model.coef_
    intercept=model.intercept_

    #予測するためのデータx（欠損値なし）を標準化しないでyを求める
    df_coef=pd.DataFrame(coef,columns=['回帰係数'],index=standscaler_ok_lst[:6])
    df_pred=pd.read_csv('Data/no_missing_data_pred.csv')
    x_pred=df_pred[['accommodates','bathrooms','bedrooms','beds','number_of_reviews','review_scores_rating']]
    x_pred=np.array(x_pred)
    coef = np.array(coef)
    y_pred=np.dot(coef,x_pred.T)+intercept

#x標準化したデータとyのmodelを作成
def LR_stand():
    #modelの作成
    model=linear_model.LinearRegression()
    df_train_x=pd.read_csv('Data/x_std.csv')
    train_x=df_train_x[['accommodates','bathrooms','bedrooms','beds','number_of_reviews','review_scores_rating']]
    df_train_y=pd.read_csv('Data/no_missing_data.csv')
    train_y=df_train_y['y']
    model.fit(train_x,train_y)
    coef=model.coef_
    intercepr=model.intercept_

    df_pred=pd.read_csv('Data/missing_pred_x_std.csv')
    x_pred=df_pred[['accommodates','bathrooms','bedrooms','beds','number_of_reviews','review_scores_rating']]
    x_pred_np=np.array(x_pred)

    y_pred=np.dot(np.array(coef),x_pred_np.T)+intercepr
    df=pd.DataFrame()
    df['y_pred']=y_pred
    df.to_csv('Data/all_y_pred.csv')
def x_data_add():
    df=pd.read_csv('Data/all_y_pred.csv')
    df_x=pd.read_csv('Data/missing_pred_x_std.csv')
    df_x=df_x[['accommodates','bathrooms','bedrooms','beds','number_of_reviews','review_scores_rating']]
    y_pred=df_x.join(df)
    y_pred.to_csv('Data/all_y_pred_x.csv')

if __name__ == '__main__':
    # LR_stand()
    # x_data_add()
    df=pd.read_csv('csv/row_no_missing_data_pred.csv')
    usefule_data=df.head(0)
    print(usefule_data)

















