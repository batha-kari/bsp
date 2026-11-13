import matplotlib.pyplot as plt
import numpy as np

n = np.arange(-10,11)
u = np.where(n>=0,1,0)

plt.subplot(3,1,1)
plt.stem(n,u)
plt.title("unit step signal")
plt.xlabel("n")
plt.ylabel("u(n)")
plt.grid(True)

n2 = np.arange(-10,11)
impulse = np.where(n2==0,1,0)

plt.subplot(3,1,2)
plt.stem(n2,impulse)
plt.title("unit impulse signal")
plt.xlabel("n")
plt.ylabel("u(n)")
plt.grid(True)


n3 = np.arange(-10,11)
u3 = np.where(n3>=0,n3,0)

plt.subplot(3,1,3)
plt.stem(n3,u3)
plt.title("unit ramp signal")
plt.xlabel("n")
plt.ylabel("u(n)")
plt.grid(True)
