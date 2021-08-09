import streamlit as st

header = st.container()
qualification = st.container()
designation = st.container()
publications = st.container()

with header:
    st.title('Welcome to Asif Ahmad WebPage')
    st.text('Hello, all! This is Asif Ahmad Master of Science in Mathematics')

with qualification:
    st.title('Qualification')
    st.text('Master of Science in Mathematics')

with designation:
    st.title('Designation')
    st.text('Lecturer in Mathematics')

with publications:
    st.title('Publications')
    st.text('One international journal article and one conference paper')

