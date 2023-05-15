import streamlit as st
import awswrangler as wr

def main():
    st.title("Streamlit com Argo e Kubernetes")
    
    query = '''
        select 
	        store, slug, platform, title
        from dw_bs.dm_client_application 
        limit 10;
    '''
    df = wr.athena.read_sql_query(sql=query,  database='dw_bs')
    st.write(df)
    
#     st.write("Nova linha!")
#     st.write("Olá Samyro!")
#     st.write("Olá Pessoas!")
    
if __name__ == '__main__':
    main()
