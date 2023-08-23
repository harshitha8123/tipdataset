import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-12/Downloads/tips.csv")
plt.hist(data['total_bill'])
plt.xlabel('day')
plt.ylabel('tip')
plt.show()
