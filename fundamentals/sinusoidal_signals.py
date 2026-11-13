import numpy as np

time = np.arange(1,10,0.1)

f = 0.25
a = np.sin(2*np.pi*f*time)

plt.subplot(2,2,1)
plt.plot(time,a)
plt.title("sine wave 1")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)

f1 = 2
b = np.sin(2*np.pi*f1*time)

plt.subplot(2,2,2)
plt.plot(time,b)
plt.title("sine wave 2")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)

c = a+b

plt.subplot(2,2,3)
plt.plot(time,c)
plt.title("sine wave 3")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)
