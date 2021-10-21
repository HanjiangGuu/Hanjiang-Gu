#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:23:58 2021

@author: guhanjiang
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Question 1

st.title("Hello Math 10")

# Question 2
st.markdown("Here is a link to Hanjinag Gu's Github page **github.com/HanjiangGuu**")

#Question 3
upload_file = st.file_uploader(label = "Please Upload CSV File",type=['csv'])

# Question 4 Convert file to a pandas df
if upload_file is not None:
    df = pd.read_csv(upload_file)
    
#Question 5
#if x is an empty strign make it numpy's not a number
#otherwise, leave x alone
    df= df.applymap(lambda x: np.nan if x==" " else x)
    
#Question 6: Let c be column name(week 3 Fri Lec)

    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
    # Then make a list of all the columns that can be made numeric
    
    good_cols = [c for c in df.columns if can_be_numeric(c)]
    
# Question 7:
# Replacecolumns in f that can be made numeric with their nueric values
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis = 0)

#Quesition 8:
    x_axis = st.selectbox("Choose an x-value",good_cols)
    y_axis = st.selectbox("Choose an y-value",good_cols)
    
#Question 9:
sd = st.slider("Numbers",0,len(df))

#Question 10:
st.write(f"The x_axis is {x_axis}, and the y_axis is {y_axis}")

#Question 11:
st.altair_chart(alt.Chart(df).mark_circle().encode(
    x = x_axis,
    y = y_axis,
    color = alt.Color(y_axis,scale=alt.Scale(scheme='turbo')),
    ), use_container_width = True)
#Question 12:
st.table(good_cols)
