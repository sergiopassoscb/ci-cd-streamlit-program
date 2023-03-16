import streamlit as st


page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

def main():
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title("Minha Aplicação Streamlit Alterado")
    st.write("A aplicação foi atualizada")
    
    
if __name__ == '__main__':
    main()

# Define a cor de fundo da página como amarelo

