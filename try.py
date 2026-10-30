
import pandas as pd
import streamlit as st

info=pd.read_excel("courses_database.xlsx",)
file_dep=pd.read_excel("courses_database.xlsx",1)
file_req=pd.read_excel("courses_database.xlsx",2)




department = st.selectbox(
    "Choose Department",
    ["DS", "CY", "IS", "MI"]
)



course = st.selectbox(
    "Choose Course",
    
   [ "",*file_dep["Course Name (EN)"].dropna().unique()]
)

code = st.selectbox(
    "or Choose Course code",
   ["", *file_dep["Code"].dropna().unique()]
)

course_info=info[(info["Code"]==code) | (info["Course Name (EN)"]==course )]
st.dataframe((course_info[["Code","Course Name (EN)","اسم المقرر (AR)","Credits","Category"]]),hide_index=True, use_container_width=True)



subject_open=file_req[(file_req["Prerequisite"]==code) | (file_req["Prerequisite Name (EN)"]==course )]
merged=pd.merge(file_dep, subject_open, left_on="Code", right_on="Course").drop(["Prerequisite Name (EN)","Prerequisite","Course Name (EN)_y","Course"],axis=1)
data=merged[merged["Department"]==department]

st.write("course ", course,"open on ",department,"department")
st.write( data.shape[0])
st.dataframe(data[["Course Name (EN)_x","Mandatory","Year","Semester","Credits"]], hide_index=True, use_container_width=True)
