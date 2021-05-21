import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

head='id,accommodates,amenities,bathrooms,bed_type,bedrooms,' \
     'beds,cancellation_policy,city,cleaning_fee,description,' \
     'first_review,host_has_profile_pic,host_identity_verified,' \
     'host_response_rate,host_since,instant_bookable,last_review,' \
     'latitude,longitude,name,neighbourhood,number_of_reviews,' \
     'property_type,review_scores_rating,room_type,thumbnail_url,zipcode,y'
head_lst = head.split(',')

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

if __name__ == '__main__':
    for i in range(1,27):
        if i==10 or i==11 or i==18 or i==19 or i==20 or i==26 or i==27:
            continue
        else:
            try:
                is_correlation(i)
            except:
                print(i)

    # make_rellation()







