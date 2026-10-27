import numpy as np
import matplotlib.pyplot as plt

# 1. Generate binary data (Transmitter)
np.random.seed(42)
N = 20

transmitted_bits = np.random.randint(0, 2, N)

# 2. Introduce noise into the channel
noise_probability = 0.20

noise = np.random.rand(N) < noise_probability

received_bits = np.bitwise_xor(
    transmitted_bits, noise.astype(int)
)

# 3. Compare transmitted and received data (Receiver)
bit_errors = np.sum(transmitted_bits != received_bits)
ber = bit_errors / N

# Display results
print("Transmitted Bits:", transmitted_bits)
print("Received Bits:   ", received_bits)
print("Number of Bit Errors:", bit_errors)
print("Bit Error Rate (BER):", round(ber, 2))

# 4. Plot transmitted and received signals
plt.figure(figsize=(10, 5))

plt.step(range(N), transmitted_bits,
         where='mid', label='Transmitted Bits')

plt.step(range(N), received_bits,
         where='mid', label='Received Bits')

plt.xlabel("Bit Index")
plt.ylabel("Binary Value")
plt.title("Digital Communication System with Noise")
plt.yticks([0, 1])
plt.ylim(-0.2, 1.2)
plt.grid(True)
plt.legend()
plt.show()
