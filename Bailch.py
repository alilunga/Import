import streamlit as st  # pip install streamlit
from deta import Deta
import os


# -------------- SETTINGS --------------
vdouanes = ["Numero bulletin de liquidation", "Numero quittance", "Date de paiement", "Position tarifaire", "Unite statique", "Quantite", "Nom du declarant", "Valeur en douane"]
currency = "FC"
page_title = "Bailch Import"
page_icon = ":money_with_wings:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- INPUT & SAVE VALEURS DOUANE ---
st.header(f"Data Entry in {currency}")
cwd = os.getcwd()
st.write("curren working directory:", cwd)
with st.form("Valeurs_Douane", clear_on_submit=True):

        st.write ("Remplir les valeurs douanieres")
        nbl = st.number_input("Entrer Numero bulletin de liquidation")
        nqc = st.number_input("Numero quittance")
        dtp = st.number_input("Date de paiement")
        ptf = st.number_input("Position tarifaire")
        ust = st.number_input("Unite statique")
        qte = st.number_input("Quantite")
        ndc = st.text_input("Nom du declarant")
        vld = st.number_input("Valeur en douane")
        submitted = st.form_submit_button("Enregistrer")

# --- DATABASE ---

deta = Deta(st.secrets["data_key"])
db = deta.Base("BSHT")

if submitted:
   db.put({"Numero bulletin de liquidation":nbl, "Numero quittance":nqc, "Date de paiement":dtp, "Position tarifaire":ptf, "Unite statique":ust, "Quantite":qte, "Nom du declarant":ndc, "Valeur en douane":vld})
    
