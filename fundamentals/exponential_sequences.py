import matplotlib.pyplot as plt
import numpy as np

a = 0.5
time = np.arange(0,15)
x = []

for i in time:
    x.append(a**i)

plt.subplot(4,2,1)
plt.stem(time,x)
plt.title("exponential seq")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)

a = 1.5
time = np.arange(0,15)
x = []

for i in time:
    x.append(a**i)

plt.subplot(4,2,2)
plt.stem(time,x)
plt.title("exponential seq")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)

a = -0.5
time = np.arange(0,15)
x = []

for i in time:
    x.append(a**i)

plt.subplot(4,2,3)
plt.stem(time,x)
plt.title("exponential seq")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)

a = -2
time = np.arange(0,15)
x = []

for i in time:
    x.append(a**i)

plt.subplot(4,2,4)
plt.stem(time,x)
plt.title("exponential seq")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)
