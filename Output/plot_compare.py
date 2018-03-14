import matplotlib.pyplot as plt

lambda1 = [0.001, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1]
epinions1 = [0.9127, 0.9259, 0.9420, 0.9467, 0.9494, 0.9466, 0.9458, 0.9457, 0.9458, 0.9386]
slashdot1 = [0.8137, 0.8260, 0.8518, 0.8642, 0.8763, 0.8775, 0.8800, 0.8776, 0.8754, 0.8464]

rank = [5, 10, 20, 30, 40, 50, 100, 200]
epinions = [0.9395, 0.9443, 0.9463, 0.9475, 0.9471, 0.9449, 0.9399, 0.9244]
slashdot = [0.8599, 0.8611, 0.8655, 0.8678, 0.8590, 0.8587, 0.8536, 0.8225]

plt.plot(rank, epinions, label = "Epinions", marker = 'v', linestyle = '--')
plt.plot(rank, slashdot, label = "Slashdot", marker = 'o', linestyle = '--')

plt.xlabel("$\lambda$", fontsize = 14)
plt.ylabel("Accuracy", fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.ylim(0.75, 1)

# plt.title("Slashdot with Square Loss")
plt.legend(loc = 0, fontsize = 14)
plt.grid(True)

plt.show()
