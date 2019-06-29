# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:29:53 2019

@author: lenovo
"""
#GIVE INPUT AS LOCATION OF DATA AND COLUMN NUMBERS FOR REQUIRED SUBDATA AND GIVES OUTPUT AS THE DATA AS A DATAFRAME, ITS STATISTICAL VALUES, CORRELATION(PEARSON) AND REQUIRED SUBDATA:

def statistical_values(datalocation,subdatascolumnnumbers):
    import numpy as np
    import pandas as pd
    from pandas import Series,DataFrame
    import scipy
    from scipy import stats
    from scipy.stats.stats import pearsonr
    data=pd.read_csv(datalocation)
    stat_values=data.describe()
    correlation=data.corr()  #pearsonR correlation values
    i=subdatascolumnnumbers
    subdata=data.iloc[:,1:i]
    return (data,stat_values,correlation,subdata)
(data,stat_values,correlation,subdata)=statistical_values(r'C:\Users\lenovo\Desktop\PYTHON\PYTHON LUCTURE\Ex_Files_Python_Data_Science_EssT\Exercise Files\Ch01\01_05\mtcars.csv',7)
import pandas as pd
import numpy as np
import sklearn
from sklearn.decomposition import FactorAnalysis,PCA
x1 = data
x1.columns=['a','b','c','d','e','f','g','h','i','j','k','l']    #NAMING COLUMNS
x=x1.drop(['a'],axis=1)   #DROPPING COLUMNS CONTAINING WORDS OR STRING
variable_name=x.columns


#Factor Analysis
factor=FactorAnalysis().fit(x)
table_FA=pd.DataFrame(factor.components_,columns=variable_name)


#principal component analysis:
pca=sklearn.decomposition.PCA()
table_PCA=pca.fit_transform(x)
variance_ratio=pca.explained_variance_ratio_
components=pd.DataFrame(pca.components_,columns=variable_name)
































