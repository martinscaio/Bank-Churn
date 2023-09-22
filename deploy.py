import pandas as pd
import numpy as np
import streamlit as st
import pickle



# Título
st.markdown("<h1 style='text-align: center; color: white;'>Bank Churn Prediction</h1>", unsafe_allow_html=True)



st.markdown(f"<small>Feito por [{'Caio Martins'}]({'https://github.com/martinscaio/'})</small>", unsafe_allow_html=True)



# Subtítulo

st.write("##### <div align='center'> Modelo de classificação para prever potenciais churns</div>", unsafe_allow_html=True)

st.write("###### <div align='center'> Com o score previsto pelo modelo segmentamos os clientes entre menos/mais propensos ao churn</div>", unsafe_allow_html=True)

# DF PARA MOSTRAR OS COMO ESTAMOS CRIANDO SCORES

data = {
    'Risco': ['Zero', 'Baixo', 'Médio', 'Alto', 'Altíssimo'],
    'Score': ["Abaixo de 0.10", "Entre 0.11 e 0.30", "Entre 0.31 e 0.50", "Entre 0.51 e 0.80", "Entre 0.81 e  1.00"]
}


df_faixa = pd.DataFrame(data)


colors = {

    "Zero":'White',
    "Baixo":'#A1ADAD',
    "Médio":"#EDCD2F",
    "Alto":"#ED9C2F",
    "Altíssimo":"#ED4F2F"
}



text_colors = {
    "Zero": 'Black',
    "Baixo": 'White',   # Por exemplo, o texto nas células cinzas será branco
    "Médio": "Black",
    "Alto": "White",
    "Altíssimo": "White"
}

def style_cells(val):
    background_color = colors.get(val, '')  # Obtém a cor de fundo com base no valor da célula
    text_color = text_colors.get(val, 'White')  # Obtém a cor do texto com base no valor da célula
    return f'background-color: {background_color}; color: {text_color};'



styled_df = df_faixa.style.applymap(style_cells, subset=['Risco', 'Score'])


styled_html = styled_df.render()


centered_html = f'<div style="display: flex; justify-content: center;">{styled_html}</div>'


st.write(centered_html, unsafe_allow_html=True)

st.write("\n")

st.write("As informações selecionadas ao lado serão passadas para o nosso modelo como é possível ver abaixo: ")




# SIDEBAR LATERAL

with st.sidebar:


    st.write("## Selecione os atributos abaixo: ")


# INPUTS PARA O USUARIO INFORMAR ATRIBUTOS DOS CLIENTES



    idade = st.number_input("Qual a idade ?", min_value=18, max_value=100)
    genero = st.selectbox("Qual o gênero ?",('M', 'F'))
    dependentes = st.number_input("Qual o número de dependentes ?", min_value=0, max_value=10)
    educacao = st.selectbox("Qual o nível educacional ?",('Graduate', 'High School', 'Unknown','Uneducated','College','Post-Graduate','Doctorate'))
    relacionamento = st.selectbox("Qual o relacionamento ?",('Married', 'Single', 'Unknown','Divorced'))
    renda = st.selectbox("Qual a renda do cliente ?",('Less than $40K','$40K - $60K','$80K - $120K','$60K - $80K','Unknown','$120K +'))
    cartao = st.selectbox("Qual o tipo de cartão de crédito ?",('Blue', 'Silver','Gold','Platinum'))
    duracao = st.slider("Quanto tempo é cliente do banco ?(Resposta em meses)",1,300, 8)
    credit_limit = st.number_input("Qual o Limite de Crédito ?", min_value=1000, max_value=40000)
    total_relationship_count = st.slider("Número de produtos mantidos pelo cliente:",1,6,2)
    months_inactive = st.slider("Número de meses inativo no último ano:",0,12,2)
    contacts_count = st.slider("Número de contatos com o banco no último ano:",0,6,3)
    total_revolving = st.number_input("Total de Saldo Rotativo no Cartão de Crédito:", min_value=0, max_value=2600)
    avg_open_buy = st.number_input("Linha de Crédito aberta no último ano(média):",min_value=1, max_value=36000)
    transaction_Q4_Q1 = st.slider("Change in Transaction Amount (Q4 over Q1):",0.0,4.5,1.3)
    transaction_total = st.number_input("Valor total de Transação no último ano:",min_value=500, max_value=20000)
    transaction_count = st.slider("Nº total de Transações no último ano:",5,150,57)
    transaction_count_Q4_Q1 = st.slider("Change in Transaction Count (Q4 over Q1):",0.0,4.8,2.2)
    avg = st.slider("Taxa Média de utilização do Cartão:",0.0,1.0,0.35)



# TRANSFORMANDO O OUTPUT EM DF

Customer_Age = [idade]
Gender = [genero]
Dependent_count = [dependentes]
Education_Level = [educacao]
Marital_Status = [relacionamento]
Income_Category = [renda]
Card_Category = [cartao]
Months_on_book = [duracao]
Total_Relationship_Count = [total_relationship_count]
Months_Inactive_12_mon = [months_inactive]
Contacts_Count_12_mon = [contacts_count]
Credit_Limit = [credit_limit]
Total_Revolving_Bal = [total_revolving]
Avg_Open_To_Buy = [avg_open_buy]
Total_Amt_Chng_Q4_Q1 = [transaction_Q4_Q1]
Total_Trans_Amt = [transaction_total]
Total_Trans_Ct = [transaction_count]
Total_Ct_Chng_Q4_Q1 = [transaction_count_Q4_Q1]
Avg_Utilization_Ratio = [avg]



data = {
    'Customer_Age': idade,
    'Gender': genero,
    'Dependent_count': dependentes,
    'Education_Level': educacao,
    'Marital_Status': relacionamento,
    'Income_Category': renda,
    'Card_Category': cartao,
    'Months_on_book': duracao,
    'Total_Relationship_Count': total_relationship_count,
    'Months_Inactive_12_mon': months_inactive,
    'Contacts_Count_12_mon': contacts_count,
    'Credit_Limit': credit_limit,
    'Total_Revolving_Bal': total_revolving,
    'Avg_Open_To_Buy': avg_open_buy,
    'Total_Amt_Chng_Q4_Q1': transaction_Q4_Q1,
    'Total_Trans_Amt': transaction_total,
    'Total_Trans_Ct': transaction_count,
    'Total_Ct_Chng_Q4_Q1': transaction_count_Q4_Q1,
    'Avg_Utilization_Ratio': avg
}


df = pd.DataFrame(data, index= [''])

# Fazer uma cópia do df para mostrar na interface do app com nome de colunas diferentes para o usuário


df_show = df.copy()


df_show = df_show.rename(columns = {"Customer_Age":"Idade",
                                    "Gender":"Genero",
                                    "Dependent_count":"Nº Dependentes",
                                    "Education_Level":"Educação",
                                    "Marital_Status":"Relacionamento",
                                    "Income_Category":"Renda",
                                    "Card_Category":"Tipo de Cartão",
                                    "Months_on_book":"Quanto tempo é cliente(meses) ?",
                                    "Total_Relationship_Count":"Nº de produtos do cliente",
                                    "Months_Inactive_12_mon":"Nº meses inativos",
                                    "Contacts_Count_12_mon":"Nº de Contatos com o banco último ano",
                                    "Credit_Limit":"Limite de Crédito",
                                    "Total_Revolving_Bal":"Total Saldo Rotativo",
                                    "Avg_Open_To_Buy":"Abertura de Linha de Crédito(Média)",
                                    "Total_Amt_Chng_Q4_Q1":"Change Amount Q4-Q1",
                                    "Total_Trans_Amt":"Valor Total de Transação no último ano",
                                    "Total_Trans_Ct":"Nº de Transação no último ano",
                                    "Total_Ct_Chng_Q4_Q1":"Change in Transaction Q4_Q1",
                                    "Avg_Utilization_Ratio":"Utilização do Cartão"})


st.write(df_show)


st.write("\n")


st.write("Após especificar todas as informações do cliente é só clicar no botão abaixo 'Churn Test' para gerar a predição")



# CARREGANDO O MODELO DE CLASSIFICAÇÃO

with open(r"C:\Users\Caio\Desktop\Credit Card Customers\model_churn.pkl", 'rb') as file:  
    model = pickle.load(file)





# FUNÇÃO DE PREDICT DO NOSSO MODELO - RETORNAR O PREDICT_PROBA PARA CRIAR OS SCORES

def predicao_churn(input_df):

    
    # Agora você pode usar input_df para prever o churn
    probs = model.predict_proba(input_df)[:,1]

    return probs







# BOTÃO PARA FAZER O PREDICT E OS POSSÍVEIS RESULTADOS
    
if st.button('Churn Test'):
    churn = predicao_churn(df)
    
    
    if churn <=0.10:
        st.write("##### <div align='center'> Resultado do Modelo</div>", unsafe_allow_html=True)
        st.write(f"Os clientes com esse perfil geralmente possuem <span style='color:White;'>Zero</span> risco de Churn. Score: {churn}", unsafe_allow_html=True)

        
    elif churn <=0.30:
        st.write("##### <div align='center'> Resultado do Modelo</div>", unsafe_allow_html=True)
        st.markdown(f"Os clientes com esse perfil geralmente possuem risco <span style='color:Grey;'>Baixo</span> de Churn. Score: {churn}", unsafe_allow_html=True)
    
    elif churn <= 0.50:
        st.write("##### <div align='center'> Resultado do Modelo</div>", unsafe_allow_html=True)
        st.markdown(f"Os clientes com esse perfil geralmente possuem <span style='color:Blue;'>Médio</span> risco de Churn. Score:{churn}", unsafe_allow_html=True)

    elif churn <= 0.80:
        st.write("##### <div align='center'> Resultado do Modelo</div>", unsafe_allow_html=True)
        st.markdown(f"Os clientes com esse perfil geralmente possuem <span style='color:Orange;'>Alto</span> risco de Churn. Score:{churn}", unsafe_allow_html=True)

    elif churn <= 1.000:
        st.write("##### <div align='center'> Resultado do Modelo</div>", unsafe_allow_html=True)
        st.markdown(f"Os clientes com esse perfil geralmente possuem <span style='color:Red;'>Altíssimo</span> risco de Churn. Score:{churn}", unsafe_allow_html=True)

    

