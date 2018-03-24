import matplotlib.pyplot as plt

numWorkers = [1,10,20,30,40]

speedup = []
totTime = []

file = "epinions-sig"

plt.figure(figsize = (6.5,9))

for i in range(5):
	ifn = "/Users/ZMY/ASY/" + file + "/w" + str(numWorkers[i]) + ".txt"
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

	plt.subplot(212)
	plt.plot(epoch, acc, label = "$M =$" + str(numWorkers[i]))
	plt.xlabel("Epoch", fontsize = 14)
	plt.ylabel("Accuracy", fontsize = 14)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.xlim(0,100)
	# plt.ylim(0.82,0.90)
	plt.ylim(0.90,0.96)
	# plt.title("Slashdot with Square Loss")
	plt.legend(loc = 4, fontsize = 14)
	plt.grid(True)

	infile.close()

for i in range(5):
	ifn = "./" + file + "/w"  + str(numWorkers[i]) + ".txt"
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
	plt.subplot(211)
	plt.plot(epoch, acc, label = "$M =$" + str(numWorkers[i]))
	plt.xlabel("Epoch", fontsize = 14)
	plt.ylabel("Accuracy", fontsize = 14)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.xlim(0,100)
	# plt.ylim(0.82,0.90)
	plt.ylim(0.90,0.96)
	# plt.title("Slashdot with Square Loss")
	plt.legend(loc = 4, fontsize = 14)
	plt.grid(True)

	infile.close()

plt.show()
# plt.savefig("/Users/ZMY/Documents/figs/" + file + ".eps")
