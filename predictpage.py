# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:38:56 2022

@author: siddh
"""


import streamlit as st
import pickle
import numpy as np
import pandas as pd
import numpy as np

def load_model():
    with open('D://dsai//project//trainedmodel.sav', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

lr_model = data["model"]
oe_dependants = data["oe_dependants"]
oe_grad = data["oe_grad"]
oe_prop = data["oe_prop"]


    
st.title("Loan Prediction")

st.write("""### We need some information to predict Loan Status""")

depcat = ['3+','2', '1', '0']
grad = ['Not Graduate', 'Graduate']
prop = ['Rural', 'Semiurban', 'Urban']
gend = ['Male', 'Female']
mar = ['Yes', 'No']
credhis = ['1.0', '0.0']

dependants = st.selectbox('dependants', depcat)
education = st.selectbox('education', grad)
property_area = st.selectbox('Property_Area', prop)
credit_history = st.selectbox('Credit History', credhis)
  
gender = st.selectbox('Gender', gend)
married = st.selectbox('Married', mar)

appl_inc = st.slider('Applicant Income', 0, 100000, 0 )
co_appl_inc = st.slider('Coapplicant Income', 0, 100000, 0 )
loan_amt = st.slider('Loan Amount', 0, 1000, 0)
loan_amt_trm = st.slider('Loan Amount Term', 0, 500, 0)

cat_list = ['Male', 'Female', 'Married', 'Unmarried']         
for i in cat_list:
       exec("%s = %d" % (i,0))

if gender=='Male':
        Male = 1
elif gender=='Female':
        Female = 1
else:
    pass

if mar == 'Yes':
    Married = 1
elif mar == 'Female':
    Unmarried = 1
else:
    pass


prediction = st.button('Predict')

if prediction:
    st.write(dependants)
    
   
    
    lst = [str(dependants), education, appl_inc,
                  co_appl_inc, loan_amt, loan_amt_trm,
                  float(credit_history), property_area, Unmarried,
                  Married, Female, Male]
    X = pd.DataFrame(lst)
    X = X.T
    st.write(X)
        
    st.write(X[[0]])
    X[[0]] = oe_dependants.fit(X[[0]])
    st.write(X[[0]])
    
    '''loan_status = lr_model.predict(X)
    st.write('hello')'''

'''a='3+'
a = oe_dependants.fit_transform([[a]])
a

dependants

a=10
if a:
    b = oe_dependants.fit_transform([[dependants]])[0][0]
else:
    pass'''
