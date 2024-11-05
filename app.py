import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.header('Dashboard de Anuncios de Venta de Coches')

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

car_data = load_data()

# Botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer", nbins=30, title='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price", title='Odómetro vs Precio')
    st.plotly_chart(fig, use_container_width=True)

# Opcional: Uso de casillas de verificación
st.sidebar.header('Opciones de Visualización')

build_histogram = st.sidebar.checkbox('Construir un histograma')
build_scatter = st.sidebar.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Construcción de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer", nbins=30, title='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construcción de un gráfico de dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price", title='Odómetro vs Precio')
    st.plotly_chart(fig, use_container_width=True)