import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import iirnotch
from scipy.signal import butter, filtfilt
import numpy as np

data = np.loadtxt("data/ecg_normal.csv")
data = data[0:400]
l = len(data)

t = np.arange(0, l) / 2000
plt.subplot(8, 1, 1)
plt.plot(t, data)
f = 500
data1 = 100 * np.sin(2 * np.pi * f * t)

plt.subplot(8, 1, 2)
plt.plot(t, data1)

noisy = data + data1
plt.subplot(8, 1, 3)
plt.plot(t, noisy)

b, a = signal.butter(4, 200, btype='low', analog=False, fs=2000)
y = signal.filtfilt(b, a, noisy)
plt.subplot(8, 1, 4)
plt.plot(t, y)

f = 15
data2 = 100 * np.sin(2 * np.pi * f * t)
plt.subplot(8, 1, 5)
plt.plot(t, data2)

noisy2 = data + data2
plt.subplot(8, 1, 6)
plt.plot(t, noisy2)

b, a = signal.butter(4, 20, btype='high', analog=False, fs=2000)
y = signal.filtfilt(b, a, noisy2)
plt.subplot(8, 1, 7)
plt.plot(t, y)

b, a = iirnotch(50, 30, 2000)
yy = signal.filtfilt(b, a, data)
plt.subplot(8, 1, 8)
plt.plot(t, yy)
