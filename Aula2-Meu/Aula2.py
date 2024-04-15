import pandas as pd
import plotly.express as px

# Lê o arquivo CSV
df = pd.read_csv(r"Aula2-Meu\telecom_users.csv")
df=df.drop("Unnamed: 0",axis=1)
df["TotalGasto"]=pd.to_numeric(df["TotalGasto"],errors="coerce")
df=df.dropna(how='all',axis=1)
df=df.dropna(how='any',axis=0)

# Exibe o DataFrame
# print(df.info())
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

for coluna in df.columns:
    if coluna != "IDCliente" or "Churn":
        fig = px.histogram(df, x=coluna, color="Churn")

        fig.show()
        #mostra no terminal as informações do gráfico
        print(df.pivot_table(index="Churn", columns=coluna, aggfunc='count'))
