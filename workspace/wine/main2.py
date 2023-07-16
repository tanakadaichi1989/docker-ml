# このコードに関する記事
# https://qiita.com/tanakadaichi_1989/items/c655d93a1fae56f2be07

#モジュールの読み込み
from __future__ import print_function

import pandas as pd
from pandas import Series,DataFrame

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np
import matplotlib.pyplot as plt

import keras
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras.optimizers import Adam


#CSVファイルの読み込み
wine_data_set = pd.read_csv("winequality-red.csv",sep=";",header=0)

#説明変数(ワインに含まれる成分)
x = DataFrame(wine_data_set.drop("quality",axis=1))

#目的変数(各ワインの品質を10段階評価したもの)
y = DataFrame(wine_data_set["quality"])

#説明変数・目的変数をそれぞれ訓練データ・テストデータに分割
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.05)


#データの整形
x_train = x_train.astype(float)
x_test = x_test.astype(float)

y_train = keras.utils.to_categorical(y_train,10)
y_test = keras.utils.to_categorical(y_test,10)


#ニューラルネットワークの実装①
model = Sequential()

model.add(Dense(50, activation='relu', input_shape=(11,)))
model.add(Dropout(0.2))

model.add(Dense(50, activation='relu', input_shape=(11,)))
model.add(Dropout(0.2))

model.add(Dense(50, activation='relu', input_shape=(11,)))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))

model.summary()
print("\n")

#ニューラルネットワークの実装②
model.compile(loss='mean_squared_error',optimizer=RMSprop(),metrics=['accuracy'])
#勾配法には、Adam(lr=1e-3)という方法もある（らしい）。

#ニューラルネットワークの学習
history = model.fit(x_train, y_train,batch_size=200,epochs=1000,verbose=1,validation_data=(x_test, y_test))

#ニューラルネットワークの推論
score = model.evaluate(x_test,y_test,verbose=1)
print("\n")
print("Test loss:",score[0])
print("Test accuracy:",score[1])

#10段階評価したいワインの成分を設定
sample = [7.9, 0.35, 0.46, 5, 0.078, 15, 37, 0.9973, 3.35, 0.86, 12.8]
print("\n")
print("--サンプルワインのデータ--")
print(sample)

#ポイント：ワインの成分をNumpyのArrayにしないとエラーが出る
sample = np.array(sample)
predict = model.predict(sample.reshape(1,-1),batch_size=1,verbose=0)

print("\n")
print("--予測値--")
print(predict)
print("\n")


#学習履歴のグラフ化に関する参考資料
#http://aidiary.hatenablog.com/entry/20161109/1478696865

def plot_history(history):  
    # 精度の履歴をプロット
    # print(history.history)
    plt.plot(['acc'])
    plt.plot(['val_acc'])
    plt.title('model accuracy')
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend(['acc', 'val_acc'], loc='lower right')
    plt.show()
    
    # 損失の履歴をプロット
    plt.plot(history.history['loss'])
    plt.plot(['val_loss'])
    plt.title('model loss')
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend(['loss', 'val_loss'], loc='lower right')
    plt.show()

# 学習履歴をプロット
plot_history(history)
