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
* jupyter lab

# Installation
```bash
pip install　pandas
pip install　numpy
pip install　sklearn
pip install streamlit
```
# 最適解の算出概要
### step1:データ抽出
selenium,bs４を用いて、https://www.airbnb.jpからデータを抽出と考えていたが、Exploratory Public(https://exploratory.io/download-public)からデータをダウンロードできたので、こちらのデータを使って分析を行う

### step2:特徴量抽出
step1で取得したデータから、価格を予測するための特徴量を抽出。
データの前処理などはjupyter labで行った。

```
 print(df.corr()['price'])
 sns.heatmap(df.corr(), square=True)
```

データセットには、場所がわかるデータもあったので、都京23区の地価を調べ、市地区から地下平均に変換したデータセットを作成。
以下のデータから予測モデルの作成を行った

- place
- amenities
- beds
- accommodates
- city_price

### step3:モデルの作成と訓練データとテストデータの比較『誤差の算出』
今回はsklearnのinearRegression()を使用した。

```
train_x,train_y=x[:n],y[:n]
test_x,test_y=x[n:],y[n:]

model=linear_model.LinearRegression()

model.fit(train_x,train_y)

coef=model.coef_
intercept=model.intercept_
y_pred=np.dot(np.array(coef),np.array(test_x).T)+intercept
coef

#評価関数
mean_absolute_error(test_y, y_pred)
```

### step4:UI
場所や宿泊人数を指定し、価格の予測を行う。

![UI](Minpaku/スクリーンショット 2021-09-21 18.47.35.png)
 
# Author
* 名前：谷本　守
* 所属：法政大学　人間支援ロボット研究室
* E-mail: mamoru.tanimoto.9g@stu.hosei.ac.jp
