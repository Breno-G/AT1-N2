
import pandas as pd

df = pd.read_csv("UCI_Credit_Card.csv")
df.head()
df.info()

df[['SEX', 'EDUCATION', 'MARRIAGE']].describe()

for col in df.columns:
    print(f"Coluna: {col}")
    print(df[col].unique())
    print("-" * 30)


#GERADO POR IA

from sklearn.preprocessing import StandardScaler

# 1. Remover a coluna 'ID'
df.drop(columns=["ID"], inplace=True)

# 2. Corrigir valores incorretos em 'EDUCATION' (0, 5, 6 → 4: "outros")
df["EDUCATION"] = df["EDUCATION"].replace({0: 4, 5: 4, 6: 4})

# 3. Corrigir valores incorretos em 'MARRIAGE' (0 → 3: "outros")
df["MARRIAGE"] = df["MARRIAGE"].replace({0: 3})

# 4. Normalizar colunas de valores monetários (para evitar escalas desproporcionais)
scaler = StandardScaler()
bill_amt_cols = [f"BILL_AMT{i}" for i in range(1, 7)]
pay_amt_cols = [f"PAY_AMT{i}" for i in range(1, 7)]
df[bill_amt_cols + pay_amt_cols] = scaler.fit_transform(df[bill_amt_cols + pay_amt_cols])

# 5. Tratar colunas PAY_0 a PAY_6
# Valores negativos significam "pagamento antecipado ou no prazo"
# Vamos agrupar todos os < 0 em um único valor (ex: -1 → 0: "pagamento no prazo")
pay_status_cols = ["PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6"]
for col in pay_status_cols:
    df[col] = df[col].apply(lambda x: 0 if x < 0 else x)

# Resultado final limpo
df_cleaned = df.copy()

df_cleaned.info()

for col in df_cleaned.columns:
    print(f"Coluna: {col}")
    print(df_cleaned[col].unique())
    print("-" * 30)
