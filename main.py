import streamlit as st
import pandas as pd
def ui():
    st.markdown("""

   <link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <link rel="icon" href="https://www.4th-ir.com/favicon.ico">
             <style>
            header {visibility: hidden;}
            .main {
                margin-top: -20px;
                padding-top: 10px;
            }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .navbar {
                padding: 1rem;
                margin-bottom: 2rem;
            }
            .card {
                padding: 1rem;
                margin-bottom: 1rem;
                transition: transform 0.2s;
                border-radius:5px;
            }
            .card:hover {
                transform: scale(1.02);
            }
            .navbar-brand img {
                margin-right: 10px;
                height: 30px;
            }
        </style>
            <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #4267B2;">
            <a class="navbar-brand" href="#" target="_blank">
                <img src="https://www.4th-ir.com/favicon.ico" alt="4th-ir logo">
                4th-ir Streamlit Tutorials
            </a>
        </nav>
""", unsafe_allow_html=True)
    
ui()

st.header("Streamlit App")
st.write("My name is Dela")
chat = st.chat_input("Hello")
date = st.date_input("Date here")
number = st.number_input("Enter number here")
audio = st.audio_input("Audio input")
text = st.text_input("hello")
file = st.file_uploader("upload herer",["csv"])

select = st.selectbox("select box",["hi"])

# try :
#     df = pd.read_csv(file)
# except :
#     st.markdown("<div class='alert alert-warning'>File not csv</div>")
# multi = st.multiselect("multiselect",df.columns)
# st.table(df[multi])
# st.write(df)