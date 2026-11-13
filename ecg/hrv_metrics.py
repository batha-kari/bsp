import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
data = np.loadtxt("data/hr.csv", delimiter=",")


fs = 500

b, a = butter(4, [0.2, 100], btype='bandpass', fs=500)
y = filtfilt(b, a, data)

plt.subplot(1,1,1)
plt.plot(data)
threshold = 0.5 * max(data)

mod_data = []
for i in data:
    if i > threshold:
        mod_data.append(i)
    else:
        mod_data.append(0)

rvalue = []
rpos = []

for i in range(1, len(mod_data)-1):
    if mod_data[i] > mod_data[i-1] and mod_data[i] > mod_data[i+1]:
        rvalue.append(mod_data[i])
        rpos.append(i)

d = []
rr_int = []
rr_interval = []
nn=rr_interval


for i in range(len(rpos)-1):
    d = rpos[i+1] - rpos[i]
    rr = d/fs
    rr_int = np.append(rr_int, rr)

print("RR interval is:", rr_int)
rr_mean = np.mean(rr_int)
print("AV-NN =", rr_mean)
SDNN = np.std(rr_int)
print("SDNN=", SDNN)



diff = np.diff(rr_int)
p = diff**2
m = np.mean(p)
RMSSD = np.sqrt(m)
print("RMSSD =", RMSSD)

SDSD = np.std(diff)
print("SDSD = ", SDSD)

threshold = 0.75
count = 0

for i in rr_int:
    if i > threshold:
        count = count + 1

print("NN50 = ", count)

pNN50 = (count / len(rr_int)) * 100
print("pNN50 = ", pNN50, "%")

hrmin = (60 / max(rr_int))
print("Min HR = ", hrmin)

hrmax = (60 / min(rr_int))
print("Max HR =", hrmax)

hr = (60) / rr_mean
print("Mean heart rate = ", hr)
