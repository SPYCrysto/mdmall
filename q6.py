import numpy as np
import matplotlib.pyplot as plt

# Generate time values
np.random.seed(42)
t = np.linspace(0, 1, 500)

# 1. Generate a clean sine wave
clean_signal = np.sin(2 * np.pi * 5 * t)

# 2. Add low-level random noise
low_noise = np.random.normal(0, 0.2, len(t))
low_noise_signal = clean_signal + low_noise

# 3. Add high-level random noise
high_noise = np.random.normal(0, 0.8, len(t))
high_noise_signal = clean_signal + high_noise

# 4. Plot all three signals in subplots
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, clean_signal)
plt.title("Clean Signal")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, low_noise_signal)
plt.title("Signal with Low Noise")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, high_noise_signal)
plt.title("Signal with High Noise")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
