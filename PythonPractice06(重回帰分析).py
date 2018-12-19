import numpy as np
import pandas as pd

path = ''
df = pd.read_csv(path)

from sklearn import linear_model
#インスタンス生成
clf = linear_model.LinearRegression()

target = ''
#説明変数
X = df.drop(target,axis=1).as_matrix()
#目的変数
Y = df[target].as_matrix()

#予測モデル
clf.fit(X, Y)

# #回帰係数
# print(clf.coef_)

# 偏回帰係数
print(pd.DataFrame({"Name":df.drop(target,axis=1).columns,
                    "Coefficients":clf.coef_}).sort_values(by='Coefficients') )

#切片(誤差)
print(clf.intercept_)

#決定係数
print(clf.score(X, Y))

# 偏回帰係数2
df_test = pd.DataFrame({"Name":df.drop(target,axis=1).columns,"Coefficients":np.abs(clf.coef_)}).sort_values(by='Coefficients')
df_test.sort_values('Coefficients',ascending=False).head()

#図示
import matplotlib.pyplot as plt

x1 = 8
y1 = 67
#説明変数
X = df.loc[:,[list_col[x1]]].as_matrix()
#目的変数
Y = df[list_col[y1]].as_matrix()

#散布図
clf.fit(X, Y)
plt.scatter(X , Y)

#回帰直線
plt.plot(X, clf.predict(X))
print('X:'+ list_col[x1])
print('Y:'+ list_col[y1])
