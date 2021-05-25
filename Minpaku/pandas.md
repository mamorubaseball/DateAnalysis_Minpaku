#意外と理解していなかったpandasの総復讐Part1
###pandas as pd とは
データ分析する際に『csvファイル』を操作する必要があります.
このcsvファイルの操作を楽に行うためにpandasというライブラリーがよく使われています。

pythonでcsvファイルを操作する際に使われるライブラリとして、pandasの他にものcsvモジュールが存在します。
簡単な書き込みや読み込み程度であればcsvモジュールでも十分ですが、より細かい編集を行う場合はpandasがオススメ

#pandasの基本操作
###csvファイルの読み込み
import pandas as pdでpandasをインポートを忘れずに。
pandasで扱うデータのことをデータフレーム(pd)と呼びます
```
import pandas as pd
df=pd.read_csv('file_name.csv')
df.head(n) #最初のn行を表示
```
###df(データフレームの作成)
```
df=pd.Dataframe('file.csv')

```

###作成したdf(データフレーム)をcsvファイルへ保存する
```
df.to_csv('file_name.csv')
```
###列の指定
例えば,[beds,roooms,number]この三つの名前が列となったdfが存在します。このdfのnumberだけ取得したい。
```
df=df['number']
#複数指定する場合
df=df[['number','rooms']]
```
###行の指定『配列に似ている』
```
#100行目から200行目
df=df[100:200]
#200行目以降全てのデータ
df=df[200:]
```
###上の二つを組み合わせて、n1~n2列m1~m2行を取得することも可能
```
df=df[[n1:n2]]
df=df[m1:m2]

#df.columsとdf.indexでも指定可能
df.colums=['n1,n2]
df.index=[m1,m2]
```
###列の追加
```
df['A']=a
df['B']=b
df['C']=[a,b,c]

A B C
a b a
    b
    c
```
#データ分析でよく使う手法
##欠損値に対する考え
基本的にデータ分析をする際、欠損値が存在するデータは削除する。

###欠損値の確認
```
df.isnull().sum()
```
###全ての値が欠損値である行、列を削除⇨all
```
#行、列どちらも指定
df.dropna(how='all')
#列を指定して削除(全ての行がNanである列を削除）
df.dropna(how='all',axis=1)
#行を指定して削除(全ての列がNanである行を削除）
df.dropna(how='all',axis=0)
```
###一つでも欠損値がある行、列を削除⇨any
```
#行、列どちらも指定
df.dropna(how='any')
#列を削除(Nanである列を削除）
df.dropna(how='any',axis=1)
#行を削除(列Nanである行を削除）
df.dropna(how='any',axis=0)
```

###特定の行・列に欠損値がある場合、列・行を削除⇨subset
```
列名：ageを指定して特定の行を削除する
df.dropna(subset=['age'])

行名：0,1を指定して特定の列を削除
df.dropna(subset=[0,1],axis=1)
```


##numpyのnp.array()で配列変換

