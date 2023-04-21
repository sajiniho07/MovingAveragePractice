import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('res/project_data.csv')
df['<DTYYYYMMDD>'] = pd.to_datetime(df['<DTYYYYMMDD>'], format='%Y%m%d')
day_values = np.array(df['<DTYYYYMMDD>'].tolist())
close_values = np.array(df['<CLOSE>'].tolist())

kernel_size = 100
moving_avg = np.convolve(close_values, np.ones(kernel_size) / kernel_size, mode='valid')
moving_avg = np.concatenate((close_values[:kernel_size - 1], moving_avg))

fig, ax = plt.subplots()
ax.plot(day_values, close_values, label="Main schema")
ax.plot(day_values, moving_avg, label=f"Moving avg kernel_size={kernel_size}")
ax.set_xlabel("DAYS")
ax.set_ylabel("CLOSE")
ax.legend()
plt.show()