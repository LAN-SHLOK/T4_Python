
import streamlit as st
st.set_page_config(page_title="Hello streamlit",layout='centered')

st.title("Welcome to streamlit !!")
st.header("This is Header")
##################IMAGE DISPLAY########################
st.header("Local Image Display")
st.image(
"Screenshot (27).png"
,caption="Random Image",
use_container_width=True)
##################AUDIO FILES##########################
st.header("Audio files")
st.audio("sampleaudio.mp3")
##################VIDEO FILES##########################
st.header("Video files")
st.video("samplevideo.mp4")
##################DATA DISPLAY##########################
import pandas as pd
st.header("Display Data")
data = {
    "student":['A','B','C','D'],
    "Marks":[85,92,76,24],
    "Passed":[True,True,True,False]
}
df=pd.DataFrame(data)
st.subheader("st.dataframe")
st.dataframe(df)

st.subheader("st.table")
st.table(df)
##################STATUS ELEMENTS##########################
import time
st.info("Useful Information")
if st.button("Start Long Run"):
    progress=st.progress(0)
    with st.spinner("progressing"):
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i+1)
    st.success("Task Completed")
    st.balloons()
##################MATPLOTLIB CHARTS##########################
import matplotlib.pyplot as plt
import numpy as np

st.subheader("Line Chart")
x = np.arange(1,11)
y = np.random.randint(50,100,size=10)

plt.figure(figsize=(6,4))
plt.plot(x,y,"o")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Matplotlib based linearchart")

st.pyplot(plt)
##################MATPLOTLIB CHARTS##########################
st.subheader("Streamlit based chart")
df1 = pd.DataFrame({
    "Student":x,
    "Marks":y
})
st.line_chart(df1)
