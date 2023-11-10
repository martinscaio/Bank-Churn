# Bank Churn Prediction - Classifcation Problem


[Clique aqui](https://bank-churn.streamlit.app) para testar o modelo de churn no Streamlit


Abaixo uma foto da interface do aplicativo

![interface_app](https://github.com/martinscaio/Bank-Churn/blob/main/Interface_App.png)

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
O modelo final selecionado utiliza o Random Forest por ser o modelo mais promissor. Neste modelo utilizamos pre processing, Feature Selection
(Mutual Information), tunagem de hiperparametros... tudo isso utilizando o Pipeline do Sklearn. 

Também fizemos o deploy do modelo utilizando o Streamlit.

Pode acessar e utilizar o modelo neste [link](https://bank-churn.streamlit.app)


## Resultados e métricas

Neste projeto testei vários modelos(sem usar dados de teste, obviamente) para verificar qual apresentava ser o mais promissor. Não irei mostrar as métricas preliminares aqui. Caso queira ver é só acessar o arquivo 'modelagem' que possui o trabalho completo.

O algoritmo escolhido foi o Random Forest. 

Como estamos lidando com dados desbalanceados, optei por utilizar o método do Class Weight para atribuir pesos diferentes às classes, de modo que o modelo leve em consideração a desigualdade na distribuição das classes durante o treinamento.

Caso queira verificar o Pipeline do modelo, a tunagem dos hiperparametros basta verificar no arquivo 'modelagem'.

#### Qual a performance/métrica do modelo final ?

Abaixo as médias de algumas métricas do Cross Validation(K = 5):

![metricas_modelofinal](https://github.com/martinscaio/Bank-Churn/blob/main/modelofinal_crossvalidation.png)


#### Mas qual a performance utilizando os dados de teste ?

![metricas](https://github.com/martinscaio/Bank-Churn/blob/main/metricas_modelofinal.png)

#### E o Classification Report ?

![classification_report](https://github.com/martinscaio/Bank-Churn/blob/main/ClassificationReport_ModeloFinal.png)

#### Curva ROC

![curva roc](https://github.com/martinscaio/Bank-Churn/blob/main/CurvaROC_ModeloFinal.png)

#### O quão calibrado estão as previsões do nosso modelo ?

![teste](https://github.com/martinscaio/Bank-Churn/blob/main/CalibrationCurve_ModeloFinal.png)


#### Curva Precisão-Recall vs Threshold

![precisao_recall](https://github.com/martinscaio/Bank-Churn/blob/main/CurvaPrecisaoRecall_ModeloFinal.png)


Este é um projeto que visa identificar os potenciais Churn com o intuito de mitigá-los. Para este problema é fundamental que consigamos um modelo que reduza os falsos negativos. Por isso priorizamos o Recall ao invés da Precisão! Em outras palavras, queremos identificar ao máximo os clientes que estão em risco de Churn, mesmo que isso signifique na prática ter alguns casos de falsos positivos. É fundamental maximizar o Recall nesses cenários! O recall é uma métrica que mede a capacidade do modelo de identificar a maioria dos casos positivos reais. Ou seja, de todas as instâncias positivas, qual o percentual é identificado corretamente pelo modelo ? No nosso caso seria: de todos os clientes que são Churns, qual percentual o nosso modelo consegue identificar corretamente ? 

Como vimos acima o nosso modelo consegue captar 84% usando threshold de 0.5

Porém, como vimos no gráfico acima, podemos obter uma melhor métrica de recall se utilizarmos um threshold de 0.4. Por padrão o modelo tende a utilizar o Threshold de 0.5, ou seja, caso o output seja >= 0.5 é considerado 'Churn' e abaixo de 0.5 considerado 'Não Churn'. A depender da aplicação do modelo podemos utilizar um Threshold diferente de 0.5! Neste caso iremos adotar um Threshold de 0.4 para maximizar o recall.




#### Performance do modelo utilizando threshold de 0.4


#### Como fica o Classification Report ? 

![class_report04](https://github.com/martinscaio/Bank-Churn/blob/main/ClassificationReport_Threshold04.png)


Podemos verificar um aumento do Recall de 0.84 para 0.88 e um declínio da Precisão de 0.86 para 0.82. Isso faz sentido neste problema que estamos tentando resolver!



#### Faixas de Riscos

Nosso modelo para prever Churn utilizando Random Forest já está pronto! Mas vamos torná-lo mais útil para os tomadores de decisão!
Como faremos isso ? Dificilmente um banco irá utilizar um modelo como saída binária 0 e 1. Faz sentido criarmos uma faixa "Risco de Churn" com base nos scores preditos pelo modelo. Isso permitirá o banco adotar diferentes planos de ação com base no risco de cada cliente.

Um cliente com alto risco de churn necessitará de uma abordagem cirúrgica e comercialmente agressiva, diferentemente de um cliente que possui risco baixo de churn. Essa segmentação facilitará e tornará mais efetiva a atuação do banco na mitigação de churn. O plano de atuação para um cliente considerado risco médio de virar churn é diferente de um cliente prestes a abandonar o serviço, assim como é diferente do plano de ação para um cliente com baixo risco de virar churn.

#### Como fica as nossas previsões utilizando uma faixa de Risco ? 

Vamos cruzar os scores criados pelo modelo com o target real dos dados 

![riscos](https://github.com/martinscaio/Bank-Churn/blob/main/Riscos_ModeloFinal.png)



#### Abrindo a caixa preta: quais são as variáveis mais importantes para o nosso modelo ?

![variaveis mais importantes](https://github.com/martinscaio/Bank-Churn/blob/main/VariaveisMaisImportantes_ModeloFinal.png)


