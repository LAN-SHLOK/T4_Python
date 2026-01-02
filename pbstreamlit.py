
#################### PB 711 ########################
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title="streamlit example of pb",layout='wide')

st.title("Streamlit Examples of PB")
st.header(("user profile app"))

name=st.text_input("Enter name")
age = st.slider("Select age",10,100)
gender = st.radio("Choose Gender",['male','female','other 107'])
hoobies = st.multiselect("Select hobbies",['Reading','Sports','Sketching'])
photo = st.file_uploader("Upload Profile Pic",type=['.jpg','.png','.jpeg'])

if st.button("Submit Profile"):
    st.subheader("profile details")
    st.write("Name - ",name)
    st.write("Age - ",age)
    st.write("Gender - ",gender)
    st.write("Hoobies - ",hoobies)
    if photo:
        st.image(photo,caption='profile pic',width=200)
        
#################### PB 712 ########################
st.header("PB 712 VACCINATION APP")
with st.sidebar:
    country = st.selectbox("Select Country",['India','USA','UK','CANADA'])
    totalpopulation = st.number_input("Total population",min_value=1)
    vaccinatedpeople = st.number_input("Vaccinated people",min_value=0)
    
if st.button("Calculate Vaccinated %"):
    percentage = (vaccinatedpeople/totalpopulation)*100
    st.write(f"Vaccination rate in {country} : {percentage :.2f}%")
    
    st.progress(min(int(percentage),100))
    if percentage>=70:
        st.success("Good coverage of vaccination")
    else:
        st.warning("Vaccination cover is poor")
