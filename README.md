# Bank Churn Prediction - Classifcation Problem


[Clique aqui](https://bank-churn.streamlit.app) para testar o modelo de churn no Streamlit

## Business Problem:


Houve um aumento no número de clientes que abandonaram o serviço de cartão de crédito do banco. 

Como podemos mitigar o churn ? Vamos criar um modelo de classificação que nos ajude a decidir quais são os clientes com maior/menor propensão de virar churn.

## Objetivo:

Construir um modelo de churn para detectar os clientes com maior propensão de churn

Sabendo quais são os clientes com maior e menor risco, o banco pode adotar diferentes abordagens para cada tipo de cliente visando a diminuição do churn.


## Dados:

O banco de dados foi obtido no [Kaggle](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers)

Consiste no registro de 10.127 clientes contendo informações como idade, salario, limite do cartão de crédito, tipo de cartão de crédito,
o número de vezes que entrou em contato com o banco no último ano, número de meses que ficou inativo... entre outros. 

É possível consultar todas as variáveis no 'dicionário de variáveis'

16% dos registros - 1627 - são de clientes que fecharam suas contas. O restante 84% - 8500 são de clientes que permanecem utilizando os serviços de cartão de crédito.



## Metodologia:

Construção de um modelo de classificação para prever churn utilizando Random Forest,XGBoost, Decision Tree e Logistic Regression. 
O modelo final selecionado utiliza o Random Forest por ser o modelo mais promissor. Neste modelo utilizamos pre processing (OneHotEncoder), Feature Selection
(Teste Univariado F), tunagem de hiperparametros... 

Também fizemos o deploy do modelo utilizando o Streamlit.

Pode acessar e utilizar o modelo neste [link](https://bank-churn.streamlit.app)


## Resultados e métricas do modelo


#### Performance 

#### Qual a performance dos modelos preliminares ? 

Segue foto abaixo com os desempenhos. 







#### Qual a performance do Modelo Final utilizando Random Forest ? 


#### Como ficou a matriz de confusão 

#### E o Classification Report:



#### Curva ROC:


#### Mas afinal, quais foram as variáveis selecionadas pelo teste univariado F?

#### O quão calibrado estão as previsões do nosso modelo ?


