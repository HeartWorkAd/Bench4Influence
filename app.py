import streamlit as st
import pandas as pd

st.set_page_config(page_title="Estymator Kampanii", layout="centered")

st.title("Estymator kampanii influencerskiej")

# Wczytywanie danych z Excela
@st.cache_data
def load_data():
    df = pd.read_excel("Benchmarki_influencerskie_2023_do_uzupełniania_IG_TT_FB.xlsx")
    return df.dropna(subset=["Platforma", "est. CPT", "ER (engagement rate)"])

df = load_data()

# Wybór platformy
platforms = df["Platforma"].unique()
platform = st.selectbox("Wybierz platformę:", platforms)

# Budżet
budget = st.number_input("Podaj budżet kampanii (PLN):", min_value=100.0, value=1000.0, step=100.0)

# Filtrujemy dane dla wybranej platformy
platform_data = df[df["Platforma"] == platform].iloc[0]

cpt = platform_data["est. CPT"]  # koszt 1000 odsłon
er = platform_data["ER (engagement rate)"] / 100   # procent na ułamek

# Obliczenia
reach = (budget / cpt) * 1000
interactions = reach * er

st.subheader("Estymowane wyniki kampanii:")
st.metric("Zasięg (reach)", f"{int(reach):,}".replace(",", " "))
st.metric("Interakcje (na podstawie ER)", f"{int(interactions):,}".replace(",", " "))

st.caption("Dane bazują na pliku benchmarków influ i mogą być orientacyjne.")
