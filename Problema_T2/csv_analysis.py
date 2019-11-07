import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data1 = pd.read_csv("data.csv")
data2 = pd.read_csv("data_seeded.csv")

sets = 20
trys = 10

x = np.array(range(1,sets))
random = [0] * sets
for index, row in data1.iterrows():
	if row['generator'] == "random":
		random[row['set']] += row['time']
		#algo
#	if row['generator'] == "numpy":
		#algo
#	if row['generator'] == "os":
		#algo

#for index, row in data2.iterrows():
#	if row['generator'] == "random":
		#algo
#	if row['generator'] == "numpy":
		#algo	
random /= 10
plt.bar(x, random, color="g", align="center")
plt.show()