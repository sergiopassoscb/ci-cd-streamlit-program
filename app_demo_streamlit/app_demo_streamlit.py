import streamlit as st
import pandas as pd

def main():
    st.title("Minha Aplicação Streamlit Alterado")
    st.write("A aplicação foi atualizada")
    
    # Cria um botão para carregar os dados
    if st.button("Carregar Dados"):
        # Cria um dataframe com dados de teste
        data = {
            'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
            'Idade': [25, 30, 27, 22],
            'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']
        }
        df = pd.DataFrame(data)
        # Mostra o dataframe na página
        st.write(df)
    
    # Cria uma caixa de seleção para filtrar os dados
    cidade_selecionada = st.selectbox("Selecione uma cidade", df['Cidade'].unique())
    # Filtra o dataframe de acordo com a cidade selecionada
    df_filtrado = df[df['Cidade'] == cidade_selecionada]
    # Mostra o dataframe filtrado na página
    st.write(df_filtrado)
    
if __name__ == '__main__':
    main()
