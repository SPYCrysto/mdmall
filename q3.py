import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Network': ['Network A', 'Network B', 'Network C',
                'Network D', 'Network E'],
    'Frequency': ['2.4 GHz', '2.4 GHz', '5 GHz',
                  '2.4 GHz', '5 GHz'],
    'Channel': [6, 11, 36, 1, 40],
    'RSSI': [-45, -68, -52, -80, -38]
}

df = pd.DataFrame(data)

# Display dataset
print("Wi-Fi Network Dataset:")
print(df.to_string(index=False))

# Identify strongest and weakest signals
strongest = df.loc[df['RSSI'].idxmax()]
weakest = df.loc[df['RSSI'].idxmin()]

print("\nStrongest Signal:")
print(strongest.to_string())

print("\nWeakest Signal:")
print(weakest.to_string())

# Plot bar chart
plt.bar(df['Network'], df['RSSI'])

plt.title('Wi-Fi Network Signal Strength')
plt.xlabel('Network (SSID)')
plt.ylabel('RSSI (dBm)')
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
