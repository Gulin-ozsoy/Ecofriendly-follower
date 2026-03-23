import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Sayfa ayarları
st.set_page_config(page_title="Nature-Flow", layout="wide")

# Tema
st.markdown("""
    <style>
    .stApp { background-color: #F5F5DC; }
    div[data-testid="stMetric"] { background-color: #ffffff; border: 2px solid #87A96B; padding: 15px; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# Veri
food_data = {
    "Elma 🍎": 0.4,
    "Avokado 🥑": 2.5,
    "Sığır Eti 🥩": 27.0,
    "Mercimek 🍲": 0.9
}

# Arayüz
st.title("🍃 Nature-Flow")
food = st.sidebar.selectbox("Gıda seç:", list(food_data.keys()))
amount = st.sidebar.slider("Gram:", 50, 1000, 250)

# Hesaplama
total = round((food_data[food] * amount) / 1000, 2)

# Gösterge
st.metric("Karbon Ayak İzi", f"{total} kg CO2")

st.write("Doğa dostu seçimler dünyayı değiştirir.")
