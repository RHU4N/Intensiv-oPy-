import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import numpy as np

df = pd.read_csv(r'Aula4-meu/advertising.csv')

sns.heatmap(df.corr(), cmap='Wistia', annot=True)
# sns.pairplot(df)
plt.show()

x=df.drop('Vendas',axis=1)

y=df['Vendas']
x_treino,x_teste,y_treino,y_teste=train_test_split(x,y,test_size=0.3)

#treino ia
regresão_linear = LinearRegression()
regresão_linear.fit(x_treino,y_treino)

arvore_ale=RandomForestRegressor()
arvore_ale.fit(x_treino,y_treino)

resultado_lin = regresão_linear.predict(x_teste)
resultado_arvore=arvore_ale.predict(x_teste)

r2_lin = metrics.r2_score(y_teste, resultado_lin)
rmse_lin = np.sqrt(metrics.mean_squared_error(y_teste,resultado_lin))
print(f'R² da Regressão Linear:{r2_lin:.1%}')
print(f'RSME da Regressão Linear:{rmse_lin:.1%}')

r2_arvore = metrics.r2_score(y_teste, resultado_arvore)
rmse_arvore = np.sqrt(metrics.mean_squared_error(y_teste,resultado_arvore))
print(f'R² da Random Forest:{r2_arvore:.1%}')
print(f'RSME da Random Forest:{rmse_arvore:.1%}')

df_resul = pd.DataFrame()

df_resul['y_teste']=y_teste
df_resul['resultado_arvore']=resultado_arvore
df_resul['resultado_lin']=resultado_lin
df_resul=df_resul.reset_index(drop=True)
fig =plt.figure(figsize=(15, 5))
sns.lineplot(data=df_resul)
plt.show()
print(df_resul)

importancia_features = pd.DataFrame(arvore_ale.feature_importances_,x_treino.columns)
plt.figure(figsize=(5,5))
sns.barplot(x=importancia_features.index,y=importancia_features[0])
plt.show()

nova_tabela = pd.read_csv("Aula4-meu/novos.csv")
print(nova_tabela)
previsao = arvore_ale.predict(nova_tabela)
sns.lineplot(data=previsao)
plt.show()
print(previsao)