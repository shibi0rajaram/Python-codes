 
import numpy as np
import csv
#ACCELERATION INPUT:
#address of earquake data as dat.txt file to be stored in same folder
with open ("elcentro_EW.dat.txt") as data1:
    D1=list(csv.reader(data1,delimiter=' '))  # delimiter to be given in csv reader
    r1 = len(D1)
    n1 = 0
    Acc_EWt = np.zeros([r1,1])
    for n1 in range(0,r1):
        Acc_EWt[n1,0] = D1[n1][1]
Acc_EWup=list(Acc_EWt[:,0])
#PADDING ACCELERATION VALUES: 100 zeros before and 1000 zeros after
izp=list(np.zeros([100,1]))
izp.extend(Acc_EWup)
fzp=list(np.zeros([1000,1]))
izp.extend(fzp)
Acc_EW=list(map(float,izp))

#TIME:
t1i=np.zeros([r1,1])
for n1 in range(0,r1):
    t1i[n1,0]=D1[n1][0]
dt=t1i[1]-t1i[0]
r1=len(Acc_EW)
T=r1*dt
t1=np.arange(0,T,dt)


# FINDING VELOCITY BY INTEGRATION USING TRAPEZOIDAL RULE:
Vel_EWt=np.zeros([r1,1])
n1=1
for n1 in range(1,r1):
    Vel_EWt[n1]=Vel_EWt[n1-1]+(Acc_EW[n1]+Acc_EW[n1-1])/2 * dt
Vel_EW=Vel_EWt[:,0]
# FINDING DISPLACWMENT BY INEGRATION USING TRAPEZOIDAL RULE:
Dis_EWt=np.zeros([r1,1])
n1=1
for n1 in range(1,r1):
    Dis_EWt[n1]=Dis_EWt[n1-1]+(Vel_EW[n1]+Vel_EW[n1-1])/2 * dt
Dis_EW=Dis_EWt[:,0]




import matplotlib.pyplot as plt  #Plotting
#Acceleration Vs Time:
y=Acc_EW
x=t1
plt.ylabel('Acceleration')
plt.xlabel('Time')
plt.title('Acceleration Vs Time (unfiltered)')
plt.plot(x,y)
plt.show()
#Velocity Vs Time:
y=Vel_EW
x=t1
plt.ylabel('Velocity')
plt.xlabel('Time')
plt.title('Velocity Vs Time (unfiltered)')
plt.plot(x,y)
plt.show()
#Displacement Vs Time:
y=Dis_EW
x=t1
plt.ylabel('Displacement')
plt.xlabel('Time')
plt.title('Displacemment Vs Time (unfiltered)')
plt.plot(x,y)
plt.show()


#above inputs in frequency domain
O=1/dt
dO=1/t1[r1-1]
Os=np.arange(0,O,dO)
#finding frequencies:
Af_EW=np.fft.fft(Acc_EW)
Vf_EW=np.fft.fft(Vel_EW)
Df_EW=np.fft.fft(Dis_EW)

Af_EWabsolute=np.abs(Af_EW)
Af_EWangle=np.angle(Af_EW)
Vf_EWangle=np.angle(Vf_EW)
Vf_EWabsolute=np.abs(Vf_EW)
Df_EWangle=np.angle(Df_EW)
Df_EWabsolute=np.abs(Df_EW)



#PLOTTING ALL SPECTRUMS:
#plt.plot(Os,Af_EWangle)
#plt.show()
#plt.draw()
#plt.figure()
#plt.plot(Os,Af_EWabsolute)
#plt.draw()
#plt.show()

#plt.plot(Os,Vf_EWangle)   SPECTRUM VALUES TO BE UNCOMMENTED IF USEFUL
#plt.draw()
#plt.figure()
#plt.plot(Os,Vf_EWabsolute)
#plt.draw()
#plt.show()

#plt.plot(Os,Df_EWangle)
#plt.draw()
#plt.figure()
#plt.plot(Os,Df_EWabsolute)
#plt.draw()
#plt.show()



#FILTER  (applying butter filter) with given lowcut and high cut values
from scipy.signal import butter,lfilter
lowcut=0.1
highcut=22
nyq=0.5*O
low=lowcut/nyq
high=highcut/nyq
b ,a = butter(4, [low, high], btype='bandpass')
d=list(lfilter(b,a,Dis_EW))


#USING NUMERICAL DIFFERENTIATION TO GET ACCELERATION AND VELOCITY(CENTERED DIFFERENCE)
#VELOCITY
u=list(np.zeros((r1,1),float))
u[0]=(d[1]-d[0])*O
v1=1
for v1 in range(1,r1-1):
    u[v1]=(d[v1-1]-d[v1+1])*0.5*O
u[r1-1]=(d[r1-1]-d[r1-2])*O

#ACCELERATION
acc=list(np.zeros((r1,1),float))
acc[0]=(u[1]-u[0])*O
a1=1
for a1 in range(1,r1-1):
    acc[a1]=(u[a1-1]-u[a1+1])*0.5*O
acc[r1-1]=(u[r1-1]-u[r1-2])*O
#PLOTTINGS using non zero padded values
t1=np.array(t1)
d=np.array(d)
plt.ylabel('Displacement')
plt.xlabel('Time')
plt.title('Displacemment Vs Time (filtered)')
plt.plot(t1[100:2774],d[100:2774])
plt.show()
plt.ylabel('Velocity')
plt.xlabel('Time')
plt.title('Velocity Vs Time (filtered)')
plt.plot(t1[100:2774],u[100:2774])
plt.show()
plt.ylabel('Acceleration')
plt.xlabel('Time')
plt.title('Acceleration Vs Time (filtered)')
plt.plot(t1[100:2774],acc[100:2774])
plt.show()

      
      