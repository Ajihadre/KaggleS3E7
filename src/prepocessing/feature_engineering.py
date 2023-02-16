# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:55:48 2023

@author: tcaron
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler

def SelfScaleData(df):
    features = []
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    df[features] = scaler.transform(df[features])
    