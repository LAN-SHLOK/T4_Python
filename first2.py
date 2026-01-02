
import streamlit as st
st.set_page_config(page_title="Hello streamlit",layout='centered')

st.title("Welcome to streamlit !!")
st.header("This is Header")
st.subheader("This is a st.text")
st.markdown("This is **st.markdown**")

code="""
def add(a,b):
    return a+b
print(add(3,5))
"""
st.code(code,language='python')

#### SIDEBAR COLUMNS AND EXPANDERS

st.sidebar.header("Profile settings")
name=st.sidebar.text_input("FacultyName")
dept=st.sidebar.selectbox("Dept",["CE","CSE","IT"])

col1,col2=st.columns([1,2])
with col1:
    st.write("Basic info")
    st.write(name,dept)
with col2:
    st.subheader("About")
with st.expander("Subjects taught"):
    st.write("Python","CN","SA")
    
#### FORMS AND INPUT

name=st.text_input("Enter name")
age =st.number_input("Age - ",0,80,18)
rating=st.slider("Rating",1,10,5)
if name:
    st.write(f"Hello {name}")

#### Selection Widget
course =st.selectbox("Courses",['python','fsd','de'])
days=st.multiselect("Perferres days",['mon','tue','thur'])
lec=st.radio("lec no",[1,2,3])

#### Date time and file upload

from datetime import date,time

examdate=st.date_input("Exam Date",date.today())
starttime=st.time_input("Start time",time(14,0))
file=st.file_uploader("Upload CSV",type=['CSV'])

## DISPLAY JSON
st.text("json data")
data={1:"python",2:"java",3:"c++"}
st.json(data)
