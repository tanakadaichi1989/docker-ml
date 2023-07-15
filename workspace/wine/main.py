import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
import pickle

# CSV を読み込み
df = pd.read_csv('winequality-red.csv',sep=";")

# データフレームを出力
print(df)

# 列名を表示
print(list(df.columns.values))

# 説明変数
xcol = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
x = df[xcol]

# 目的変数
t = df['quality']

print(t.value_counts)

model = tree.DecisionTreeClassifier(max_depth=3,random_state=0)

# 学習を実行
model.fit(x,t)

# サンプルのデータ
sample = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 7.0, 0.0, 0.0],[7.9, 0.35, 0.46, 5, 0.078, 15, 37, 0.9973, 3.35, 0.86, 12.8]]

# サンプルデータの予測
print(model.predict(sample))

# モデルの評価
print(model.score(x,t))

# 決定木の表示
tree.plot_tree(model,feature_names=x.columns,filled=True)

# 散布図の表示
df.plot(kind='scatter', x = 'fixed acidity', y = 'pH')
plt.show()

# モデルの保存
with open('winequality-red.pkl','wb') as f:
    pickle.dump(model, f)
