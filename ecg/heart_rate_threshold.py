import numpy as np
import matplotlib.pyplot as plt

# Load the ECG data
data=np.loadtxt("data/ecg_normal.csv",delimiter=',')

# Plot original ECG signal
plt.subplot(2, 2, 1)
plt.plot(data)
plt.title('ECG')

# Calculate threshold
dlen = len(data)
dmax = max(data)
dthr = 0.5 * dmax
print("Threshold =", dthr)

# Apply thresholding filter
s = []
for i in range(dlen):
    if data[i] < dthr:
        s = np.append(s, 0)
    else:
        s = np.append(s, data[i])

# Plot filtered signal
plt.subplot(2, 2, 2)
plt.plot(s)
plt.title('R peaks')
Rpeak = []
Rpos = []

# Loop through the signal to find local maxima (R-peaks)
for i in range(1, dlen - 1):
    if s[i] > s[i - 1] and s[i] >= s[i + 1]:
        Rpeak = np.append(Rpeak, s[i])
        Rpos = np.append(Rpos, i)

print("Rpeak amplitude is", Rpeak)
print("R position is", Rpos)

# Plot the detected peaks on top of the original ECG signal
plt.subplot(2, 2, 3)
plt.plot(data)
plt.plot(Rpos, Rpeak, "m*")
plt.title('Peak Detected')

# Calculate peak intervals and Heart Rate (HR)
d = []
d = np.diff(Rpos)
print("Difference of R peak interval =", d)

m = np.mean(d)
print("Mean of R peak interval in sample =", m)

Fs = 125
HR = round((60 / m) * Fs, 1)
print("Heart Rate =", HR)
