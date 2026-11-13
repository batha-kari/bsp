import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt

data = np.loadtxt("data/ppg.csv" , delimiter=',')
plt.figure(figsize=(12,10))

plt.subplot(5,1,1)
plt.xlabel("position")
plt.ylabel("amp")
plt.title("ppg data")
plt.plot(data)

b, a = butter(1, 0.005, btype='high', analog=False)
y = filtfilt(b, a, data)
data = y
plt.subplot(5,1,2)
plt.xlabel("position")
plt.ylabel("amp")
plt.title("filtered data")
plt.plot(data)

l=len(data)
d=[]
dp=[]
for i in range(0,l,5):
   d=np.append(d,data[i])
   dp=np.append(d,i)
plt.subplot(5,1,3)
plt.xlabel("position")
plt.ylabel("amp")
plt.title("downsampled data")
plt.plot(d)

m=max(data)
threshold=m*0.5
mdata=[]
for i in range(l):
    if(data[i]>threshold):
        mdata.append(data[i])
    else:
        mdata.append(0)
plt.subplot(5,1,4)
plt.xlabel("position")
plt.ylabel("amp")
plt.title("threshold data")
plt.plot(mdata)

P=[]
PPos=[]
l1=len(d)
for i in range(0,l1):
  if (d[i]>threshold):
      if (d[i]-d[i-1]>=0 and d[i]-d[i+1]>=0):
          P=np.append(P,d[i])
          PPos=np.append(PPos,i)
print("Peak=",P)
print("PeakPos=",PPos)

interval=[]
l2=len(PPos)
for n in range(l2):
    diff=PPos[n]-PPos[n-1]
    if (diff>5):
        interval=np.append(interval,diff)
print('interval',interval)

#pk_pk
pkpk=[]
pkpk=np.mean(interval)
fs=100
duration=pkpk/fs
print("Pulse duration=",duration,"seconds")

i=1/pkpk
pulserate=i*fs*60
print("pulse rate=",pulserate)

onset=[]
for i in PPos:
    di=int(i-20)
    q=int(i)
    for j in range(q,di,-1):
        j=int(j)
        if(d[j-1]>d[j]and d[j+1]>d[j]):
            onset=np.append(onset,j)
            break
print(onset)
mininumonset=0
mininumonset=min(d)
d=d+abs(mininumonset)
t=[]
array=[]
u=len(onset)
meanvalue=0
for i in range(u-1):
    i=int(i)
    l1=int(onset[i])
    l2=int(onset[i+1])
    t=d[l1:l2]
    sumofarray=sum(t)
    array=np.append(array,sumofarray)
meanvalue=np.mean(array)
print('pulsearea',meanvalue)
