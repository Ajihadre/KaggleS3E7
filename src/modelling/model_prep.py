# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:54:38 2023

@author: tcaron
"""

def SelfSplitTrain(df,test_size=0.2):
    X = df.drop(columns=["id","booking_status"])
    y = df[["booking_status"]].values
    X_train, X_val, y_train, y_val = train_test_split(X,y,test_size=test_size,random_state=42)
    return (X_train, X_val, y_train, y_val)