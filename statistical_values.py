# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:03:16 2019

@author: lenovo
"""

def statistical_values(datalocation,subdatascolumnnumbers):
    import pandas as pd
    data=pd.read_csv(datalocation)
    stat_values=data.describe()
    correlation=data.corr()  #pearsonR correlation values
    i=subdatascolumnnumbers
    subdata=data.iloc[:,1:i]
    return (data,stat_values,correlation,subdata)
(data,stat_values,correlation,subdata)=statistical_values(r'C:\Users\lenovo\Desktop\PROGRAMS\PYTHON\PYTHON CODES\statistical_values\mtcars.csv',7)