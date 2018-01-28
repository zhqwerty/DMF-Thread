import matplotlib.pyplot as plt

numWorkers = [1,10,20,30,40]

speedup = []
totTime = []

# plt.figure(1)

for i in range(5):
	ifn = "./epinions-sh/w" + str(numWorkers[i]) + ".txt"
	time = []
	acc = []
	epoch = []
	rmse = []

	infile = open(ifn,'rb')
	for eachline in infile.readlines():
		lines = eachline.split(' ')
		# print lines
		epoch.append(int(lines[0]))
		acc.append(float(lines[1]))
		rmse.append(float(lines[2]))
		time.append(float(lines[3]))
	# print time
	totTime.append(time[-1])
	speedup.append(totTime[0] / totTime[-1])

	plt.plot(time, acc, label = "w = " + str(numWorkers[i]))
	plt.xlabel("Time")
	#plt.xlabel("Epoch")
	plt.ylabel("Accuracy")
	plt.title("Epinions with Square-Hinge Loss")
	plt.legend(loc = 0)
	plt.grid(True)

	infile.close()

print speedup
print totTime
plt.show()

