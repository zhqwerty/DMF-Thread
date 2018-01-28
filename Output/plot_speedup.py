import matplotlib.pyplot as plt

algos = ["Slashdot-Sigmoid", "Slashdot-Square", "Slashdot-Sauare-Hinge", "Epinions-Sigmoid", "Epinions-Square", "Epinions-Square-Hinge"]

numWorkers = [1,10,20,30,40]
s = [[], [], [], [], [], []]

s[0] = [1.0, 4.296753749033111, 6.281899515727457, 7.390569139188242, 8.47231139745586]
t0 = [68.8804, 16.0308, 10.9649, 9.32004, 8.13006]

s[1] = [1.0, 4.124579473783148, 6.025083089509416, 7.071526211089007, 7.523330728221402]
t1 = [63.6303, 15.4271, 10.5609, 8.9981, 8.45773]

s[2] = [1.0, 3.7494084940257895, 5.827195109338911, 6.364917768174407, 6.427204400562745]
t2 = [50.71, 13.5248, 8.7023, 7.96711, 7.8899] 

s[3] = [1.0, 5.187944805637246, 7.084951704016762, 8.222830706631552, 8.981043916322323]
t3 = [118.019, 22.7487, 16.6577, 14.3526, 13.1409]

s[4] = [1.0, 4.976024411508282, 7.009383455183928, 7.9882200288667615, 8.587616666797276]
t4 = [109.584, 22.0224, 15.6339, 13.7182, 12.7607]

s[5] = [1.0, 4.878158844765343, 6.305745753531201, 7.147051184170136, 8.494134815064264]
t5 = [90.804, 18.6144, 14.4002, 12.7051, 10.6902]

plt.figure(1)
for i in range(6):
	plt.plot(numWorkers, s[i], label = algos[i], marker = 'o')
	plt.xlabel("Number of workers")
	plt.ylabel("Speedup")
	plt.grid(True)
	plt.legend(loc = 0)

plt.show()







