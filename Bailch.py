import streamlit as st  # pip install streamlit
from deta import Deta


# -------------- SETTINGS --------------
vdouanes = ["id", "Name", "Last Name"]
currency = "FC"
page_title = "Bailch test"
page_icon = ":money_with_wings:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- INPUT & SAVE VALEURS DOUANE ---
with st.form("Identite", clear_on_submit=True):

        st.write ("Remplir")
        id = st.number_input("id")
        name = st.text_input("Name")
        last = st.text_input("Last name")
        submitted = st.form_submit_button("Enregistrer")

# --- DATABASE ---

deta = Deta(st.secrets["data_key"])
db = deta.Base("BSHT")

if submitted:
    db.put({"id":id, "name":name, "last":last})

def identity():
    """Returns a list"""
    res = db.fetch()
    return res.items
    
identity()
st.write ("Servir")
