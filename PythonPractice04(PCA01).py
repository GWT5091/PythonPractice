from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('AirPlane.csv',index_col=0)
df = pd.concat([df,pd.get_dummies(df['Maker']),pd.get_dummies(df['Propulsion(Turbofan Engines)'])],axis=1).drop('Maker',axis=1)
df_1 = pd.concat([df.loc[:,'Passenger(MAX)'],df.loc[:,'EnginPower(kN)':'Height(m)']],axis=1)
pca = PCA()
x_pca = pca.fit_transform(df_1)
df_pca = pd.DataFrame(x_pca,index=df.index , columns = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th'])
#累積寄与率
plt.figure(figsize=(12,8))
plt.plot(np.hstack([0,pca.explained_variance_ratio_.cumsum()]))
plt.xlabel('n_commponents',fontsize=15)
plt.ylabel('explained_variance_ratio',fontsize=15)
plt.show()
#各説明変数と主成分の相関
plt.figure(figsize=(14,12))
sns.heatmap(pca.components_,
            cmap='Blues',
           annot=True,
           annot_kws={'size':20},
           fmt='1.1f',
           xticklabels=df_1.columns,
           yticklabels=['1st','2st','3st','4st','5st','6st','7st','8st','9st','10st','11st','12st','13st'])
#第1主成分と第2主成分
df_pca['result'] = df[4]
fig , ax = plt.subplots(figsize=(12,8))
df_pca.plot(kind='scatter', x='1st',y='2nd',s=100,c='result',cmap='summer',alpha=1.0,ax=ax)

#寄与率
print(pca.explained_variance_ratio_)
#因子
print(pca.components_)
