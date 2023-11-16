import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
        page_title="Bailch Smart Visibility",
)

import accueil

with st.sidebar:
        app = option_menu(
            menu_title='Smart Visibility',
            options=['accueil','requisitions','stocks','services','commandes','declarations','contact'],
            icons=['house','person-square','graph-up','tools','cart','share','send'],
            menu_icon="bricks", default_index=0,
            styles={
                    "container": {"padding": "5!important", "background-color": "#ffffe0"},
            "icon": {"color": "red", "font-size": "16px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#ddd"},
            "nav-link-selected": {"background-color": "#add8ff"},}

        )

if app == 'accueil':
    st.write(app)
if app == 'requisitions':
    st.write(app)
if app == 'stocks':
    st.write(app)
if app == 'services':
    st.write(app)
if app == 'commandes':
    st.write(app)
if app == 'declarations':
    st.write(app)
if app == 'contact':
    st.write(app)
