import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="wide")

# Cria um cabeçalho para o aplicativo
st.title("Análise de Estórias")

# Cria um componente de upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

if uploaded_file is not None:
    # Lê o arquivo Excel
    df = pd.read_excel(uploaded_file)

    # Mostra as primeiras 10 linhas do dataframe
    with st.expander("Mostrar dados da tabela"):
        st.write(df.head(10))
        
    # Divide o título em 'Epic' e 'Screen'
    df['Epic'] = df['Title'].apply(lambda x: x.split('|')[0].strip() if isinstance(x, str) and '|' in x else 'Other')
    df['Screen'] = df['Title'].apply(lambda x: x.split('|')[1].strip() if isinstance(x, str) and '|' in x and len(x.split('|')) > 1 else 'Other')
    
    # Contabiliza o número de bugs
    bug_count = df[df['Title'].str.contains(r'\[Bug\]', na=False)].shape[0]
    # Contabiliza o número de estórias entregues dentro da sprint ('Done')
    status_counts = df['State'].value_counts()
    delivered_count = status_counts.get('Done', 0)
    # Contabiliza o número de estórias não entregues dentro da sprint ('Done')
    non_delivered_statuses = status_counts.drop(labels='Done', errors='ignore')
    non_delivered_count = non_delivered_statuses.sum()
    
    with col1:
        #Mostra o card de estórias entregues
        st.subheader("Estórias entregues dentro da sprint")
        st.metric(label="Total de Entregues", value=delivered_count, border=True)
    
    with col2:
        #Mostra o card de estórias bugs
        st.subheader("Bugs criados")
        st.metric(label="Total de Bugs", value=bug_count, border=True)
    with col3:
        #Mostra o card de estórias bugs
        st.subheader("Estórias não entregues")
        st.metric(label="Total de não entregues", value=non_delivered_count, border=True)

    
    with col4:
        # Contabiliza o número de estórias em cada status
        st.subheader("Número de estórias em cada status como card")
        st.bar_chart(status_counts)

    with col5:
        # Contabiliza o número de estórias por Epic
        epic_counts = df['Epic'].value_counts().reset_index()
        epic_counts.columns = ['Epic', 'Contagem']
        # Exibe o gráfico de barras para a distribuição de Epics
        st.subheader("Distribuição de Estórias por Epic")
        st.bar_chart(epic_counts.set_index('Epic'))

    with col6:
        # Contabiliza o número de estórias por Tela (Screen)
        screen_counts = df['Screen'].value_counts()
        #screen_counts.columns = ['Screen', 'Contagem']

        # Exibe o gráfico de barras para a distribuição por Telas
        #st.subheader("Distribuição de Estórias por Tela")
        #st.bar_chart(screen_counts.set_index('Screen'))
        # Contabiliza o número de estórias por Tela (Screen)

        # Exibe o gráfico de pizza para a distribuição por Telas
        #st.subheader("Distribuição de Estórias por Tela")
        #fig, ax = plt.subplots(figsize=(8,8))
        #ax.pie(screen_counts.values, labels=screen_counts.index, autopct='%1.1f%%', startangle=140)
        #ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        #st.pyplot(fig)
    
        # Exibe o gráfico de pizza para a distribuição por Telas com plotly
        st.subheader("Distribuição de Estórias por Tela")
        fig = px.pie(screen_counts, values=screen_counts.values, names=screen_counts.index, title='Distribuição de Estórias por Tela')
        st.plotly_chart(fig)    