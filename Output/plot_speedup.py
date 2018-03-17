import matplotlib.pyplot as plt

algos = ["Slashdot-Sigmoid", "Slashdot-Square", "Slashdot-Squared Hinge", "Epinions-Sigmoid", "Epinions-Square", "Epinions-Squared Hinge"]
marker = ['o', '*', 'v', 's','h','+']
numWorkers = [1,10,20,30,40]
time = [[0 for j in range(5)] for i in range(6)]
asy_time = [[0 for j in range(5)] for i in range(6)]
speedup = [[0 for j in range(5)] for i in range(6)]

# Slashdot-Sigmoid
time[0] = [72.66, 15.43, 11.14, 8.10, 7.42] # 
asy_time[0] = [70.97, 12.40, 8.72, 7.43, 6.85] #

# Slashdot-Square
time[1] = [68.44, 14.35, 10.56, 7.83, 7.47] #
asy_time[1] = [68.38, 12.33, 8.48, 7.23, 6.99] #

# Slashdot-Sauare-Hinge
time[2] = [63.80, 13.71, 10.40, 7.60, 6.69] #
asy_time[2] = [64.59, 11.18, 7.63, 6.77, 6.56] #

# Epinions-Sigmoid
time[3] = [118.61, 23.30, 17.20, 15.26, 12.20] #
asy_time[3] = [112.40, 19.98, 14.54, 12.21, 11.65]  #

# Epinions-Square
time[4] = [108.68, 22.41, 16.60, 14.47, 11.69] #
asy_time[4] = [108.65, 18.79, 13.92, 11.97, 11.29] #

# Epinions-Square-Hinge
time[5] = [104.60, 20.44, 15.13, 12.74, 11.27]  #
asy_time[5] = [103.60, 18.05, 12.99, 11.18, 10.97] #

for i in range(6):
	for j in range(5):
		speedup[i][j] = asy_time[i][0] / asy_time[i][j] 

plt.figure(1)
for i in range(6):
	plt.plot(numWorkers, speedup[i], label = algos[i], marker = marker[i])
	plt.xlabel("$M$", fontsize = 14)
	plt.ylabel("Speedup", fontsize = 14)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.grid(True)
	plt.ylim(0,12)
	plt.xlim(0,40)
	plt.legend(loc = 0, fontsize = 12)

plt.show()
