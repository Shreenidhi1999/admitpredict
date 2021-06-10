# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:37:49 2021

@author: Hipparagi
"""

import numpy as np
import pandas as pd
import pickle 
import streamlit as st

pickle_a=open("linear.pkl","rb")
regressor=pickle.load(pickle_a) # our model

def predict_chance(GREScore,TOEFLScore,UniversityRating,CGPA):
    prediction=regressor.predict([[GREScore,TOEFLScore,UniversityRating,CGPA]])
    return prediction


def main():
    st.title("Admission prediction APP using ML") 
    html_temp="""
        <div style="background-color:tomato;padding:10px">
        <h2 style ="color:black;text-align:center;">Admission Prediction ML app</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)
    GREScore=st.text_input("GRE Score(0-340)","Type here")
    TOEFLScore=st.text_input("TOEFL Score(0-120)","Type here")
    UniversityRating=st.text_input("University Rating(1-5)","Type here")
    CGPA=st.text_input("CGPA(1-10)","Type here")
    result=""
    if st.button("Predict"):
        result=predict_chance(GREScore, TOEFLScore, UniversityRating, CGPA)
    st.success("The chance of admission in that university is{}".format(result))
        
if __name__=='__main__':
    main()
