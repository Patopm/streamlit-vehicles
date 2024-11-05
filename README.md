# Car Sales Dashboard

Este proyecto consiste en una aplicación web para visualizar datos de anuncios de venta de coches. La aplicación permite explorar los datos mediante histogramas y gráficos de dispersión interactivos.

## Funcionalidades

- **Encabezado:** Título de la aplicación.
- **Histograma:** Visualización de la distribución del odómetro.
- **Gráfico de Dispersión:** Relación entre el odómetro y el precio.
- **Interactividad:** Botones para generar las visualizaciones.

## Despliegue

La aplicación está desplegada en [Render](https://render.com/) y puede ser accedida a través de la siguiente URL: [https://<APP_NAME>.onrender.com/](https://render.com/).

## Tecnologías Utilizadas

- Python
- Streamlit
- Pandas
- Plotly Express
- Render

## Instrucciones

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/car-sales-dashboard.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd car-sales-dashboard
    ```
3. Crea un entorno virtual:
    ```bash
    python3 -m venv vehicles_env
    source vehicles_env/bin/activate
    ```
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
5. Ejecuta la aplicación:
    ```bash
    streamlit run app.py
    ```