import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data/ecg_normal.csv",delimiter=",")
fs=125
n = len(data)
dmax = max(data)
dt = dmax * 0.5

rr = []
rp = []
rin = []

for i in range(1, n - 1):
    if data[i] > dt:
        if data[i] - data[i - 1] > 0 and data[i] - data[i + 1] > 0:
            rr = np.append(rr, data[i])
            rp = np.append(rp, i)

print("R max =", rr)
print("R position =", rp)

rpl = len(rp)

for i in range(1, rpl):
    rin = np.append(rin, rp[i] - rp[i - 1])

f = 1 / rin
f1 = f * fs
fmean = np.mean(f1)

heart_rate = fmean * 60

print("Heart rate =", heart_rate, "bpm")

q = []
ps = []
s = []
ts = []
qa = []
sa = []
pp = []
tp = []
po = []
pof = []
to = []
tof = []
qo = []

for a in rp:
    l = int(a - 5)
    w = int(a)
    u = int(a + 5)

    for b in range(l, w):
        if data[b - 1] - data[b] > 0 and data[b + 1] - data[b] > 0:
            q = np.append(q, b)
            qa = np.append(qa, data[b])

    for c in range(w, u + 1):
        if data[c - 1] - data[c] > 0 and data[c + 1] - data[c] > 0:
            s = np.append(s, c)
            sa = np.append(sa, data[c])

print("Q position =", q)
print("S position =", s)

width = s - q
qrs_duration = width / fs

print("QRS width =", width)
print("Mean QRS width =", np.mean(width))
print("QRS duration =", qrs_duration)
print("Mean QRS duration =", np.mean(qrs_duration))

for i in q:
    l1 = int(i - 20)
    u1 = int(i)

    s1 = data[l1:u1]
    p = max(s1)
    ppos = np.argmax(s1)

    ps = np.append(ps, p)
    pp = np.append(pp, ppos + l1)

for i in s:
    l2 = int(i + 20)
    u2 = int(i)

    s2 = data[u2:l2]
    t = max(s2)
    tpos = np.argmax(s2)

    ts = np.append(ts, t)
    tp = np.append(tp, tpos + u2)

print("P max =", ps)
print("P position =", pp)

print("T max =", ts)
print("T position =", tp)

for i in pp:
    ru = int(i - 8)

    for k in range(int(i), ru + 1, -1):
        p_onset = max(0, data[k])

        if p_onset == 0:
            po = np.append(po, k)
            break

for i in pp:
    rk = int(i + 8)

    for k in range(int(i), rk + 1, 1):
        p_offset = max(0, data[k])

        if p_offset == 0:
            pof = np.append(pof, k)
            break

# print("P onset =", po)
# print("P offset =", pof)

p_duration = (pof - po) / fs

print("P wave duration =", p_duration)
print("Mean P wave duration =", np.mean(p_duration))

for i in tp:
    ru = int(i - 20)

    for k in range(int(i), ru + 1, -1):
        t_onset = max(0, data[k])

        if t_onset == 0:
            to = np.append(to, k)
            break

for i in tp:
    rk = int(i + 20)

    for k in range(int(i), rk + 1, 1):
        t_offset = max(0, data[k - 1])

        if t_offset == 0:
            tof = np.append(tof, k)
            break

# print("T onset =", to)
# print("T offset =", tof)

t_duration = (tof - to) / fs

print("T wave duration =", t_duration)
print("Mean T wave duration =", np.mean(t_duration))

for i in q:
    ru = int(i - 8)

    for k in range(int(i), ru + 1, -1):
        q_onset = max(0, data[k])

        if q_onset == 0:
            qo = np.append(qo, k)
            break

# print("Q onset =", qo)

pr = []
st = []
qt = []

for i in range(min(len(po), len(qo))):
    pr_interval = (qo[i] - po[i]) / fs
    pr = np.append(pr, pr_interval)

for i in range(min(len(s), len(to))):
    st_interval = (to[i] - s[i]) / fs
    st = np.append(st, st_interval)

for i in range(min(len(qo), len(tof))):
    qt_interval = (tof[i] - qo[i]) / fs
    qt = np.append(qt, qt_interval)

print("PR interval =", pr)
print("Mean PR interval =", np.mean(pr))

print("ST interval =", st)
print("Mean ST interval =", np.mean(st))

print("QT interval =", qt)
print("Mean QT interval =", np.mean(qt))

plt.figure(figsize=(12, 10))

plt.subplot(5, 1, 1)
plt.plot(data)
plt.plot(rp, rr, 'ro')
plt.title("R Peaks")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 2)
plt.plot(data)
plt.plot(q, qa, 'go')
plt.title("Q Peaks")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 3)
plt.plot(data)
plt.plot(s, sa, 'bo')
plt.title("S Peaks")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 4)
plt.plot(data)
plt.plot(pp, ps, 'mo')
plt.title("P Peaks")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 5)
plt.plot(data)
plt.plot(tp, ts, 'co')
plt.title("T Peaks")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)
