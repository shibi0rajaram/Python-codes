# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:42:30 2019

@author: lenovo
"""

import pandas as pd
import numpy as np

def savingscaledandoriginaldata(address):
    
    data=pd.read_csv(address,delim_whitespace=True,skiprows=3)
    header=pd.read_csv(address,delim_whitespace=True,skiprows=2,nrows=1)
    
    timesteps = header.iloc[0][1].split(",")
    timesteps=int(timesteps[0])
    dt=float(header.iloc[0][3])
    totaltime=(timesteps)*(dt)
    Timesteps=np.arange(0,totaltime,dt,dtype=float)
    acceleration=data.stack().astype(float).values
    
    r1=acceleration.shape[0]
    acceleration=acceleration.reshape(r1,1)
    



    # FINDING VELOCITY BY INTEGRATION USING TRAPEZOIDAL RULE:
    velocity=np.zeros([r1,1])
    n1=1
    for n1 in range(1,r1):
       velocity[n1]=velocity[n1-1]+(acceleration[n1]+acceleration[n1-1])/2 * dt

    # FINDING DISPLACWMENT BY INEGRATION USING TRAPEZOIDAL RULE:
    displacement=np.zeros([r1,1])
    n1=1
    for n1 in range(1,r1):
        displacement[n1]=displacement[n1-1]+(velocity[n1]+velocity[n1-1])/2 * dt
    
    
    O=1/(dt)
    #FILTER
    from scipy.signal import butter,lfilter
    nyq=0.5*O
    lowcut=(1/nyq)*1.1
    highcut=(nyq*0.707)*0.9
    low=lowcut/nyq
    high=highcut/nyq
    b ,a = butter(4, [low, high], btype='bandpass')
    d=lfilter(b,a,displacement)

    
    
    
    
    

    #USING NUMERICAL DIFFERENTIATION TO GET ACCELERATION AND VELOCITY(CENTERED DIFFERENCE)
    #VELOCITY
    u=np.zeros((r1,1),float)
    u[0]=(d[1]-d[0])*O
    v1=1
    for v1 in range(1,r1-1):
        u[v1]=(d[v1-1]-d[v1+1])*0.5*(O)
        u[r1-1]=(d[r1-1]-d[r1-2])*(O)

    #ACCELERATION
    acc=np.zeros((r1,1),float)
    acc[0]=(u[1]-u[0])*(O)
    a1=1
    for a1 in range(1,r1-1):
        acc[a1]=(u[a1-1]-u[a1+1])*0.5*(O)
        acc[r1-1]=(u[r1-1]-u[r1-2])*(O)


    #saving datas into a matrix:
    Timesteps=pd.DataFrame(Timesteps)
    table=np.hstack((acceleration,velocity,displacement,acc,u,d))
    Table=pd.DataFrame(data=table)
    Table.columns=['Acc(orig)','Vel(orig)','Dis(orig)','Acc(psd)','Vel(psd)','Dis(psd)']
    return(Table,Timesteps)
    
    
    


    
    
    
