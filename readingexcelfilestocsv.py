
import pandas as pd
from groundmotionanalysis import savingscaledandoriginaldata

flist=pd.read_csv("D:/EQASoft/pyproject/PEERNGAR_SCALED/flist.csv")
sn=flist.shape[0]
location='D:/EQASoft/pyproject/PEERNGAR_Unscaled/'
for i in range(sn):
    if len(flist.iloc[i][0])!=5:
         filename1=location+str(flist.iloc[i][0]).strip()
         Table1,Time=savingscaledandoriginaldata(filename1)
         
    if len(flist.iloc[i][1])!=5:
        filename2=location+str(flist.iloc[i][1]).strip()
        Table2,Time=savingscaledandoriginaldata(filename2)
        
    if len(flist.iloc[i][2])!=5:
        filename3=location+str(flist.iloc[i][2]).strip()
        Table3,Time=savingscaledandoriginaldata(filename3)
    
    Table=pd.concat([Time,Table1,Table2,Table3], axis=1)
    Table.to_csv('csv'+str(i),sep=',')