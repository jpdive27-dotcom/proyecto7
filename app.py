import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Cuadro de mandos - Vehículos", layout="wide")


st.header("Cuadro de mandos: Anuncios de venta de coches (USA)")


car_data = pd.read_csv("vehicles_us.csv")

st.write("Vista rápida del dataset:")
st.dataframe(car_data)


hist_button = st.button("Construir histograma (odometer)")

if hist_button:
    st.write("Creación de un histograma para la columna **odometer**.")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button("Construir gráfico de dispersión (odometer vs price)")

if scatter_button:
    st.write("Creación de un gráfico de dispersión: **odometer** vs **price**.")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
