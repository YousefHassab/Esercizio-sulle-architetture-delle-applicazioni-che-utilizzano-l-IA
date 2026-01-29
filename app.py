import streamlit as st
from core.planner import Planner
import os

# Configurazione Pagina
st.set_page_config(page_title="AI HR Manager", page_icon="🤖")

st.title("🤖 AI Corporate Human Capital")
st.markdown("Interroga il database aziendale delle competenze in tempo reale.")

# Inizializzazione del Planner (Cervello dell'app)
@st.cache_resource
def get_planner():
    return Planner()

planner = get_planner()

# Inizializzazione della cronologia della chat (Memoria di Stato UI)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Visualizza i messaggi precedenti
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dell'utente
if prompt := st.chat_input("Chiedi qualcosa (es: Chi sa usare Python a Milano?)"):
    # Aggiungi messaggio utente alla cronologia
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generazione risposta dell'AI
    with st.chat_message("assistant"):
        with st.spinner("L'AI sta consultando il database..."):
            try:
                # Chiamata al tuo Planner (lo stesso del terminale!)
                response = planner.process_request(prompt)
                st.markdown(response)
                # Aggiungi risposta alla cronologia
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Errore: {e}")
