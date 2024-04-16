#///////////////////////
# budgets //////////////////////
#///////////////////////////////////////////
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import seaborn as sns
import os
import re
import unicodedata
from unidecode import unidecode
os.chdir('D:\Sylvain\GitHub\Model-Cinema')
df=pd.read_csv('Data/Archives/budgets2.csv', sep=";")


#////////////////////////////
#////////// STREAMLIT ///////


st.sidebar.title('Sommaire')
pages=["Contexte du projet","Collecte et Exploration des données","Analyse des données", "Modélisation"]
page=st.sidebar.radio ('allez vers la page', pages)
# st.dataframe(df.head())
if page ==pages[0]:
    st.write('### Contexte du projet')
    st.write ('bla bla bla bla bla')
    st.image("images.jpg")