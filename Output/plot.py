import matplotlib.pyplot as plt

numWorkers = [1,10,20,30,40]

speedup = []
totTime = []

# plt.figure(1)

for i in range(5):
	ifn = "./epinions-sq/w" + str(numWorkers[i]) + ".txt"
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

	plt.plot(epoch, acc, label = "$M=$" + str(numWorkers[i]))
	plt.xlabel("Epoch", fontsize = 14)
	plt.ylabel("Accuracy", fontsize = 14)
	# plt.title("Slashdot with Square Loss")
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.xlim(0,100)
	# plt.ylim(0.82,0.885)
	plt.ylim(0.9,0.951)
	plt.grid(True)
	plt.legend(loc = 4, fontsize = 14)


	infile.close()

print speedup
print totTime
plt.show()

