import streamlit as st
import pandas as pd
st.write("""
# Maximum of 3 numbers
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    number1 = st.number_input("Enter_first_number", min_value=None, max_value=None)
    number2 = st.number_input("Enter_second_number",min_value=None, max_value=None)
    number3 = st.number_input("Enter_third_number",min_value=None, max_value=None)
    data1=max(number1,number2,number3)
          
          
    

    data = {         
            'Enter_first_number': number1,
            'Enter_second_number': number2,
            'Enter_third_number': number3
            }
    features = pd.DataFrame(data, index=[0])
    return features
df = user_input_features()


st.subheader('User Input parameters')
st.write(df.to_dict())
st.write("The maximum value is",df.max(axis=1))
