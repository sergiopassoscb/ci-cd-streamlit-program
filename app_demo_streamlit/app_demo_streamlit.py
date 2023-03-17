import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Gráfico de Linha")
    
    x = np.linspace(0, 20, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    st.pyplot(fig)

if __name__ == "__main__":
    main()