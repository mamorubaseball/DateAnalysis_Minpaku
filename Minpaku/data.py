import csv
import pandas as pd

#データ数が多すぎるので半分で処理する
def data_half():
    df=pd.read_csv('Data/train.csv')
    half_df=df[:20000]
    half_df.to_csv('Data/half_train.csv')
    #19999このデータ数

#データの抜けや漏れがあると基本的にそのデータは使えない
def make_nommising_data(filename):
    df=pd.read_csv('Data/{}'.format(filename))
    missing_df=df.dropna(how='any')
    missing_df=missing_df[:]
    #19999このデータ数
    missing_df.to_csv('Data/no_missing_data_{}'.format(filename))

#全ての行が埋まっている列だけを作成
def row_make_nomissing_data(filename):
    df=pd.read_csv('Data/{}'.format(filename))
    missing_df=df.dropna(how='any',axis=1)
    missing_df=missing_df[:]
    #19999このデータ数
    missing_df.to_csv('Data/row_no_missing_data_{}'.format(filename))

#fileが多すぎるので、拡張子ごとにdirに移動
import os
import glob
import shutil
def file_clean():
    csv_file=glob.glob('Data/*.csv')
    png_file=glob.glob('Data/*.png')
    for i in csv_file:
        shutil.move(i,'csv/')
    for j in png_file:
        shutil.move(j,'png/')

if __name__ == '__main__':
    # make_nommising_data('pred.csv')
    # row_make_nomissing_data('pred.csv')
    pass