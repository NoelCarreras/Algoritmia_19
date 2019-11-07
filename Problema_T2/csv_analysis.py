import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data1 = pd.read_csv("data.csv")
data2 = pd.read_csv("data_seeded.csv")

sets = 20
trys = 10

names = [ "Set1", "Set2", "Set3", "Set4", "Set5", "Set6", "Set7", "Set8", "Set9", "Set10", "Set11", "Set12", "Set13", "Set14", "Set15", "Set16", "Set17", "Set18", "Set19", "Set20" ]

x1 = [0] * sets
x2 = [0] * sets
x3 = [0] * sets
x4 = [0] * sets
x5 = [0] * sets


i = 0
j = 0
while i < sets*5:
	x1[j] = i+1
	x2[j] = i+2
	x3[j] = i+3
	x4[j] = i+4
	x5[j] = i+5
	j += 1
	i += 5

random = [0] * sets
numpy = [0] * sets
os = [0] * sets
ns_random = [0] * sets
ns_numpy = [0] * sets

for index, row in data1.iterrows():
	if row['generator'] == "random":
		ns_random[row['set']-1] += row['time']
	if row['generator'] == "numpy":
		ns_numpy[row['set']-1] += row['time']

for index, row in data2.iterrows():
	if row['generator'] == "random":
		random[row['set']-1] += row['time']
	if row['generator'] == "numpy":
		numpy[row['set']-1] += row['time']	
	if row['generator'] == "os":
		os[row['set']-1] += row['time']

new1 = np.array([x*1000 / trys for x in random])
new2 = np.array([x*1000 / trys for x in numpy])
new3 = np.array([x*1000 / trys for x in os])
new4 = np.array([x*1000 / trys for x in ns_random])
new5 = np.array([x*1000 / trys for x in ns_numpy])

'''
plt.bar(x1, new1, color="g", align="center")
plt.bar(x2, new2, color="r", align="center")
plt.bar(x3, new3, color="b", align="center")
plt.bar(x4, new4, color="m", align="center")
plt.bar(x5, new5, color="k", align="center")

plt.show()

t = linspace(0, 2*math.pi, 400)
'''

plt.plot(names, new1, color="g")
plt.plot(names, new2, color="r")
plt.plot(names, new3, color="b")
plt.plot(names, new4, color="m")
plt.plot(names, new5, color="k")

plt.ylabel("Tiempo en milisegundos")
plt.xlabel("SET de datos")
plt.legend(["random con semilla", "numpy con semilla", "os", "random sin semilla", "numpy sin semilla"])
plt.show()
