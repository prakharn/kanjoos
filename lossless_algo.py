import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url = "https://stooq.com/q/d/l/?s=nvda.us&i=d"
data = pd.read_csv(url)
date = data.tail(30)["Date"]
op = data.tail(30)["Open"]


fdate = [
    datetime.strptime(d, "%Y-%m-%d").strftime("%m-%d")
    for d in date
]

# prange = max(op)-min(op)

x = np.arange(0.00, max(op), 0.01)

# for i in line:
#     print(i)

val = np.zeros_like(x)
y = np.zeros_like(x)

k = op.iloc[0]

for i in op:
    if k>i:
        mask = (x<k) & (x>i)
        val[mask] += 1
    elif k==i:
        mask = (x==k)
        val[mask] += 1
    else:
        mask = (x>k) & (x<i)
        val[mask] += 1
    k=i

for i in op:
    mask = (x==i)
    y[mask] = i

# plt.plot(val, op)
plt.plot(x, y)
plt.plot(x, val, color="green")
plt.show()
