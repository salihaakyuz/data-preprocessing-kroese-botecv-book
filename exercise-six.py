import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

urlprefix = "https://vincentarelbundock.github.io/Rdatasets/csv/"
dataname = "datasets/EuStockMarkets.csv"
EuStockMarkets = pd.read_csv(urlprefix + dataname)
start_time = 1991.495
end_time = 1998.646
time_vector = np.arange(start_time, end_time, 1 / 260)
# print(len(time_vector), len(EuStockMarkets["DAX"]))
color_map = {"DAX": "blue", "SMI": "green", "CAC": "red", "FTSE": "turquoise"}

plt.figure(figsize=(12, 6))

for column in EuStockMarkets.iloc[:, 1:]:
    print(column)
    plt.scatter(
        time_vector,
        EuStockMarkets[column],
        label=column,
        color=color_map[column],
        linewidths=2,
        s=10,
    )
plt.title("EuStockMarkets indices")
plt.xlabel("Time in years")
plt.ylabel("Stock Index Value")
plt.legend(title="Stock indices")
plt.grid(True)
plt.show()
