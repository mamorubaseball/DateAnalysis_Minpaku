# Minpaku
Airbnbからデータを取得し、価格の予測をするファイル。
目的は、価格設定の基準を選定するため。（データ分析の練習も込み)

# Airbnbとは
![airbnb](png/airbnb.png)
アメリカのサンフランシスコで立ち上げられたサービス。

使っていない家や空いている部屋を貸したい「ホスト（家主）」から、空いている家や部屋を「ゲスト（旅行者）」として借りることができます。

# 価格決定問題
部屋を貸し出す『ホスト』自身で価格を設定する。

そのため、この価格設定を高く設定しすぎると貸し出すことができず、低く設定すると売上は立ちません。

そこで、価格の『最適解』を求めるのがこのプロジェクトです。

# 実行環境
* Python 3.8.3

# Installation
```bash
pip install　pandas
pip install　numpy
pip install　sklearn
```
# 最適解の算出概要
####step1:データ抽出
selenium,bs４を用いて、https://www.airbnb.jpからデータを抽出
####step2:特徴量抽出
step1で取得したデータから、価格を予測するための特徴量を抽出

- place
- amenities
- accommodates
- number_of_reviews
- review_scores_rating

####step3:訓練データとテストデータの比較『誤差の算出』
####step4:
####step5:

###ファイルの説明

 
# Author
* 名前：谷本　守
* 所属：法政大学　人間支援ロボット研究室
* E-mail: mamoru.tanimoto.9g@stu.hosei.ac.jp