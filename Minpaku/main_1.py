import pandas as pd
import numpy as np
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
def zscore(x, axis = None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd  = np.std(x, axis=axis, keepdims=True)
    zscore = (x-xmean)/xstd
    return zscore


#文字列データを数値データとして、分析する
def make_train_data():
    df=pd.read_csv('csv/train.csv')
    df=df[['accommodates','amenities','city','number_of_reviews','review_score_rating','property_type','y']]

#質的変数（説明変数が文字列であるデータの処理）
def category_int():
    df=pd.read_csv('csv/train.csv')
    train_df=pd.read_csv('csv1/train.csv')
    # ac=df['amenities']
    # for i in range(len(ac)):
    #     n=len(ac[i])
    #     df['amenities_num']=n
    # cc=df['city'].unique()
    # pc=df['property_type'].unique().tolist()
    # print(cc,pc)
    #カテゴリー種類
    #city:['LA' 'DC' 'NYC' 'SF' 'Chicago' 'Boston']
    # property_type:['Apartment', 'House', 'Townhouse', 'Loft', 'Cabin', 'Condominium', 'Guest suite', 'Guesthouse', 'Other', 'Bungalow', 'Villa', 'Bed & Breakfast', 'Dorm', 'Timeshare', 'Camper/RV', 'Cave', 'Hostel', 'Earth House', 'In-law', 'Serviced apartment', 'Boat', 'Tent', 'Castle', 'Boutique hotel', 'Vacation home', 'Hut', 'Treehouse', 'Yurt', 'Chalet', 'Island', 'Tipi', 'Train', 'Parking Space', 'Casa particular']
    #
    # df_int=pd.DataFrame(['accommodates','amenities','city','number_of_reviews','review_score_rating','property_type',
    #                       'Condominium', 'Guest suite', 'Guesthouse', 'Other',
    #                       'Bungalow', 'Villa', 'Bed & Breakfast', 'Dorm', 'Timeshare',
    #                       'Camper/RV', 'Cave', 'Hostel', 'Earth House', 'In-law',
    #                       'Serviced apartment', 'Boat', 'Tent', 'Castle', 'Boutique hotel',
    #                       'Vacation home', 'Hut', 'Treehouse', 'Yurt', 'Chalet', 'Island',
    #                       'Tipi', 'Train', 'Parking Space', 'Casa particular','y'])

    #数値計算
    # train_df=pd.DataFrame()
    # amenities=[]
    # for i in df['amenities']:
    #     print(len(i))
    #     amenities.append(len(i))
    # train_df['number_of_reviews']=np.array(df['number_of_reviews'])
    # train_df['review_scores_rating'].fillna(train_df['review_scores_rating'].mean())

    #city
    city_lst=['LA' 'DC' 'NYC' 'SF' 'Chicago' 'Boston']
    for j,i in enumerate(df['city']):
        if i=='LA':
            train_df['LA'][j]=1
        elif i=='DC':
            train_df['DC']=1
        elif i=='NYC':
            train_df['NYC']=1
        elif i=='CF':
            train_df['CF']=1
        elif i=='Chicago':
            train_df['Chicago']=1
        elif i=='Boston':
            train_df['Boston']=1
    #property_type
    # train_df.fillna(0)
    # train_df.to_csv('csv1/train.csv')



if __name__ == '__main__':
    category_int()










