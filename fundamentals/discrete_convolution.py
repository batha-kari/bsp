import numpy as np
import matplotlib.pyplot as plt

x = [1, 2]
h = [1, 2, 3, 4]

d = np.convolve(x, h)
print(d)

l1 = len(x)
l2 = len(h)
l = l1 + l2 - 1

x1 = np.append(x, np.zeros(l - l1, dtype=int))
h1 = np.append(h, np.zeros(l - l2, dtype=int))

y = []

for n in range(l):
    s = 0
    for k in range(n + 1):
        if k < l1 and (n - k) < l2:
            s += x[k] * h[n - k]
    y.append(s)

y = np.array(y, dtype=int)
print("Convolution output:", y)

plt.subplot(3, 1, 1)
plt.stem(np.arange(len(x1)), x1)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Sequence x[n]")

plt.subplot(3, 1, 2)
plt.stem(np.arange(len(h1)), h1)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Sequence h[n]")

plt.subplot(3, 1, 3)
plt.stem(np.arange(len(y)), y)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Convoluted sequence y[n]")
