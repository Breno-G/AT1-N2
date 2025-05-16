# 💳 Previsão de Inadimplência com Aprendizado de Máquina

Projeto da disciplina de Novas Tecnologias (AT1 - N2) — Universidade Católica de Brasília  
Professor: William Malvezzi

## 📌 Descrição

Este projeto tem como objetivo construir um modelo preditivo capaz de identificar clientes com maior risco de inadimplência em pagamentos de cartão de crédito, com base em dados históricos e demográficos.

O dataset utilizado é o [Default of Credit Card Clients Dataset](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset), extraído do Kaggle.

---

## 📁 Estrutura do Projeto

- `Previsao_Inadinplencia.ipynb` — Notebook principal com toda a análise, modelagem, validação e visualizações.
- `UCI_Credit_Card.csv` — Base de dados original.
- `Desafio AT1 - N2.docx` — Enunciado oficial do desafio.
- `requirements.txt` — Lista de bibliotecas utilizadas.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.8+
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## ✅ Etapas do Projeto

### 1. Leitura e Limpeza dos Dados
- Importação do dataset
- Renomeação de colunas (`PAY_0` → `PAY_1`, `default.payment.next.month` → `DEF_NEXT_MONTH`)
- Remoção da coluna `ID`
- Correção de categorias inválidas em `EDUCATION` (valores 0, 5, 6 → 4)
- Correção de `MARRIAGE` com valor 0 substituído por 3
- Substituição de valores negativos em `PAY_*` por 0

### 2. Análise Exploratória (EDA)
- Estatísticas descritivas com `.describe()` e `.info()`
- Visualização de distribuições com histogramas e boxplots
- Mapa de correlação entre faturas e pagamentos

### 3. Pré-processamento
Pré-processamento com Pipelines
- Uso de `Pipeline` e `ColumnTransformer` para tratamento automático de dados
- **Colunas numéricas**:
  - Imputação de média (`SimpleImputer`)
  - Escalonamento com `MinMaxScaler`
- **Colunas categóricas**:
  - Codificação com `OneHotEncoder` (com `handle_unknown='ignore'`)
- Junção dos dados transformados em um `DataFrame` processado
- Separação clara entre `X` (features) e `y` (alvo)

### 4. Modelagem
- Divisão dos dados em treino/teste (70%/30%) com estratificação
- Modelos treinados:
  - DummyClassifier (baseline)
  - DecisionTreeClassifier
  - RandomForestClassifier com ajuste de hiperparâmetros (`GridSearchCV`)

### 5. Avaliação dos Modelos
- Métricas utilizadas:
  - Acurácia
  - Precisão
  - Recall
  - F1 Score
  - ROC AUC
  - Matriz de Confusão
- Comparação entre modelos: Random Forest apresentou o melhor desempenho geral.

---

## 📊 Resultados do Melhor Modelo (Random Forest)

- **Acurácia**: 82.07%
- **Precisão**: 69.99%
- **Recall**: 33.15%
- **F1 Score**: 44.99%
- **ROC AUC**: 64.56%
- Matriz de confusão: 
 [[6726  283]
 [1331  660]]

---

## 🧠 Conclusões

- O Random Forest superou outros modelos, com desempenho equilibrado entre precisão e recall, porém foi o modelo que mais demorou para executar.
- O projeto tem margem para evolução. 
- O uso de métricas como F1 e AUC foi essencial devido ao desbalanceamento das classes.

---

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/previsao-inadimplencia.git
cd previsao-inadimplencia
```

2. Instale os pacotes:
```bash
pip install -r requirements.txt
```

3. Execute o notebook:
```bash
jupyter notebook Previsao_Inadinplencia1_2.ipynb
```

---

## 📚 Referências

- https://www.kaggle.com/code/lucabasa/credit-card-default-a-very-pedagogical-notebook
