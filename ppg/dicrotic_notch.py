import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt

data = np.loadtxt("data/ppg.csv"  , delimiter=',')

d1 = data[0:2000]

plt.figure(figsize=(12,10))

b, a = butter(4, 0.2, btype='high', analog=False, fs=500)

y = filtfilt(b, a, d1)

d1 = y

b, a = butter(4, 200, btype='low', analog=False, fs=500)

yy = filtfilt(b, a, y)

print(yy)

plt.subplot(5,1,1)
plt.title('filtereddata')
plt.plot(d1)

length = len(yy)

p = []
d = []

for i in range(2, length-2):
    d = (2*yy[i-2]) - yy[i-1] - (2*yy[i]) - yy[i+1] + (2*yy[i+2])
    p = np.append(p, d)

print(p)

plt.subplot(5,1,2)
plt.xlabel("position")
plt.ylabel("amp")
plt.title("ppg data")
plt.plot(p)

smoth = []
len1 = len(p)

m1 = 32

smt = []

for i in range(m1, len1):
    i = int(i)
    s = 0

    for k in range(1, m1):
        k = int(k)
        b = (p[i-k+1])**2
        s = s + (m1-k+1)*b

    smoth = np.append(smoth, s)

plt.subplot(5,1,3)
plt.xlabel("position")
plt.ylabel("amp")
plt.title('smooth')
plt.plot(smoth)

sm1 = len(smoth)

th = (0.15) * max(smoth)

smt = []

for i in range(sm1):
    i = int(i)
    v = smoth[i]

    if (v > th):
        smt = np.append(smt, smoth[i])
    else:
        smt = np.append(smt, 0)

plt.subplot(5,1,4)
plt.xlabel("position")
plt.ylabel("amp")
plt.title("threshold")
plt.plot(smt)

len1 = len(smt)

ppos = []
peak = []

for i in range(0, len1-1):
    if smt[i] > smt[i+1] and smt[i] > smt[i-1]:
        ppos = np.append(ppos, i)
        peak = np.append(peak, smt[i])

lenn = len(ppos)

p = []

for i in range(0, lenn-1):
    difference = ppos[i+1] - ppos[i]

    if (difference > 100):
        p = np.append(p, ppos[i])

print(p)

lennn = len(p)

dpos = []
dic = []

for i in range(lennn):
    u = int(p[i] + 50)
    l = int(p[i] - 50)

    M = d1[l:u]

    dic = np.argmin(M)

    dic = dic + l

    dpos = np.append(dpos, dic)

print("dicrotic position", dpos)

plt.subplot(5,1,5)
plt.xlabel("position")
plt.ylabel("amp")
plt.title("dicrotic notch")

plt.plot(d1)

plt.plot(
    dpos.astype(int),
    d1[dpos.astype(int)],
    'r*',
    markersize=6
)
