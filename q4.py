import numpy as np

# Ping response time readings (in milliseconds)
rtt = [40, 48, 42, 65, 50, 72]

# Calculate average, minimum and maximum RTT
average_rtt = np.mean(rtt)
minimum_rtt = np.min(rtt)
maximum_rtt = np.max(rtt)

# Display results
print("Ping Response Time Analysis")
print("Average RTT:", round(average_rtt, 2), "ms")
print("Minimum RTT:", minimum_rtt, "ms")
print("Maximum RTT:", maximum_rtt, "ms")
