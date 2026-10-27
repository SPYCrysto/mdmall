import matplotlib.pyplot as plt

# Indoor Wi-Fi measurement data
position = [1, 2, 3, 4, 5, 6]
rssi = [-40, -48, -42, -65, -50, -72]

# Plot Position versus RSSI
plt.figure(figsize=(8, 5))
plt.plot(position, rssi, marker='o', linestyle='-',
         label='RSSI')

# Highlight deep signal fluctuation points
plt.scatter([4, 6], [-65, -72],
            label='Fade nulls')

plt.title('Indoor Wi-Fi Signal Fluctuation')
plt.xlabel('Position (m)')
plt.ylabel('RSSI (dBm)')
plt.xticks(position)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# Identify weakest signal
weakest_index = rssi.index(min(rssi))
print("Deepest fade point:")
print("Position:", position[weakest_index], "m")
print("RSSI:", rssi[weakest_index], "dBm")
