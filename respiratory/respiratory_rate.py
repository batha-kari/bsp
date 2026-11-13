import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

data = np.loadtxt("data/respiratory.csv")

plt.figure(figsize=(15, 10))


plt.subplot(2, 2, 1)
plt.plot(data)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Respiratory Signal")


f = 500
b, a = butter(2, 0.005, btype='high', analog=False, fs=f)
y = filtfilt(b, a, data)
data = y
plt.subplot(2, 2, 2)
plt.plot(data)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered Respiratory Signal")


m = max(data)
th = m * 0.5
th_data = []
pos = []
l1 = len(data)
for i in range(l1):
    if data[i] > th:
        th_data = np.append(th_data, data[i])
    else:
        th_data = np.append(th_data, 0)
plt.subplot(2, 2, 3)
plt.plot(th_data)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Thresholded Respiratory Signal")


l2 = len(th_data)
for i in range(1, l2 - 1):
    if (th_data[i] > th_data[i + 1] and
            th_data[i] > th_data[i - 1] and
            th_data[i] > 0):
        pos = np.append(pos, i)


l3 = len(pos)
interval = []
for i in range(l3 - 1):
    diff = pos[i + 1] - pos[i]
    if diff > 5:
        interval = np.append(interval, diff)
m_int = np.mean(interval)
rr = (60 * f) / m_int
print("Respiratory rate using time domain:", rr, "breaths/min")





N = len(data)
fft_vals = np.fft.rfft(data, N)
fft_vals = abs(fft_vals)
fft_freqs = np.fft.rfftfreq(N, d=1/f)



fft_vals[0] = 0
max_pos = np.argmax(fft_vals)
max_freq = fft_freqs[max_pos]


rr_fft = max_freq * 60
print("Respiratory rate using frequency domain:", rr_fft, "breaths/min")


plt.subplot(2, 2, 4)
plt.plot(fft_freqs, fft_vals)
plt.xlim(0, 1)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency Domain (FFT)")
