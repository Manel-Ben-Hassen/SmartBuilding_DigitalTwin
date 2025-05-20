import streamlit as st
import requests

st.title("🏢 Smart Building Digital Twin")
st.write("Visualisation des données de la salle 001")

try:
    response = requests.get("http://orion:1026/v2/entities/urn:ngsi-ld:Room:001")
    data = response.json()

    st.metric("🌡️ Température", f"{data['temperature']['value']} °C")
    st.metric("💧 Humidité", f"{data['humidity']['value']} %")
    st.metric("👥 Occupation", f"{data['occupancy']['value']} personnes")

except Exception as e:
    st.error("Erreur lors de la récupération des données depuis Orion.")
