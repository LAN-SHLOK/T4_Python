
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
