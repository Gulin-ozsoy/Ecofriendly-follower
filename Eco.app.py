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

# Gıda Verileri
food_data = {
    "Elma 🍎": 0.4,
    "Avokado 🥑": 2.5,
    "Dana Eti 🥩": 27.0,
    "Mercimek 🍲": 0.9,
    "Çilek 🍓": 0.5,
    "Domates 🍅": 0.2,
    "Salatalık 🥒": 0.15,
    "Yumurta 🥚": 4.8,
    "Süt (1L) 🥛": 3.2,
    "Çay (Bardak) ☕": 0.05,
    "Şeker (kg) 🍬": 0.6,
    "Un (kg) 🌾": 0.7,
    "Zeytinyağı (1L) 🫒": 4.5,
    "Ekmek 🥖": 0.6
}

# Sol Panel Düzenleme
food = st.sidebar.selectbox("Gıdalar", list(food_data.keys()))


# Arayüz
st.title("🍃 Nature-Flow")
food = st.sidebar.selectbox("Gıda seç:", list(food_data.keys()))
amount = st.sidebar.slider("Gram:", 50, 1000, 250)

# Hesaplama
total = round((food_data[food] * amount) / 1000, 2)

# Gösterge
st.metric("Karbon Ayak İzi", f"{total} kg CO2")

st.write("Doğa dostu seçimler dünyayı değiştirir.")
