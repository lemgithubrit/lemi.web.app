import streamlit as st 
import streamlit.components as stc
import pandas as pd
import numpy as np
#header
st.set_page_config(page_title="Wabepage", page_icon=":tada:", layout="wide")
st.title("Engineering Properties of Ethiopian Grains Crops")
st.write("Five major cereals (Teff, Wheat, Maize, Sorghum, and Barley)"
         )

#subheader
with st.container():
    st.write("---") 
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("Available Data")       
st.subheader("""Basic Engineering Properties of Grain""")  
#input table
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'Grains': ["Teff", "Wheat", "Maize","Sorghum","Barly"],
  'Bulk Density': [1, 20, 30, 40, 50],
  'Solid Density': [30, 20, 40, 40, 90],
  'Angle of Repose': [3, 2, 40, 10,9]

})
df





#sidenotes 
st.sidebar.title("Option")
text=st.sidebar.text_area("Paste Text Here")
st.write(text)
button1=st.sidebar.button("Add Text")
date = st.sidebar.date_input("Pick a date")
#add file

#gap
st.write("##")
st.write("##")

#authenticator 
st.subheader("Registration")
frist,second,last=st.columns(3)
frist.text_input("Frist Name")
second.text_input("Middle Name")
last.text_input("Last Name")
email,mob=st.columns([3,1])
email.text_input("Email")
mob.text_input("Mob Number")
user,pw,pw2=st.columns(3)
user.text_input("Username")
pw.text_input("password",type="password")
pw2.text_input("Retype your password",type="password")
button1=st.button("Submit")





st.write("##")
st.write("##")
st.write("##")
st.write("##")


#footer 
st.caption('streamlit turns data scripts into shareable web appin minutes All in pure python No front end experience required')
st.write("Developer(Lemi Demissie PhD student @ASTU")











