import numpy as np
import matplotlib.pyplot as plt

def fnc(t):
    y = np.ones_like(t)
    nonzero = t != 0
    y[nonzero] = np.sin(2 * np.pi * t[nonzero]) / (2 * np.pi * t[nonzero])
    return y

n = np.linspace(-500, 500, 1001)
t = n * (100/500)
x_n = fnc(t)

plt.plot(n, x_n)
plt.title('x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()

x_k = np.fft.fft(x_n) 
x_k_shifted = np.fft.fftshift(x_k) # 將低頻移到中心
omega = np.linspace(-np.pi, np.pi, len(x_k_shifted))  #DFT 每2*pi都是一個週期

plt.plot(omega, np.abs(x_k_shifted))
plt.title('DFT of x[n] (Magnitude Spectrum)')
plt.xlabel('Frequency ω (radians/sample)')
plt.ylabel('|X(e^(jω))|')
plt.grid(True)
plt.show()


N = len(x_n)
X_manual = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        X_manual[k] += x_n[n] * np.exp(-1j * 2 * np.pi * k * n / N)
X_manual_shifted = np.fft.fftshift(X_manual)  # 將低頻移到中心

plt.plot(omega, np.abs(X_manual_shifted))
plt.title('DFT of x[n] (Magnitude Spectrum)')
plt.xlabel('Frequency ω (radians/sample)')
plt.ylabel('|X(e^(jω))|')
plt.grid(True)
plt.show()




def hanning_window(t, T0):
    w = np.zeros_like(t)
    inside = np.abs(t) <= (T0 / 2)  # Hanning window is non-zero only in this range
    w[inside] = 0.5 * (1 + np.cos(2 * np.pi * t[inside] / T0))
    return w

n = np.linspace(-500, 500, 1001)
t = n * (100/500)
T0 = 50

w_n = hanning_window(t, T0)

plt.plot(n, w_n)
plt.title('Hanning window w[n]')
plt.xlabel('n')
plt.ylabel('w[n]')
plt.grid(True)
plt.show()

y_n = x_n * w_n

plt.plot(n, y_n)
plt.title('y[n]')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid(True)
plt.show()


y_k = np.fft.fft(y_n) 
y_k_shifted = np.fft.fftshift(y_k)
omega = np.linspace(-np.pi, np.pi, len(y_k_shifted))

plt.plot(omega, np.abs(y_k_shifted))
plt.title('DFT of y[n] (Magnitude Spectrum)')
plt.xlabel('Frequency ω (radians/sample)')
plt.ylabel('|Y(e^(jω))|')
plt.grid(True)
plt.show()