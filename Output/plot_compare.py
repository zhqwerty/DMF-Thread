import matplotlib.pyplot as plt

lambda1 = [0.001, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1]
epinions_p1 = [0.9127, 0.9259, 0.9420, 0.9467, 0.9494, 0.9466, 0.9458, 0.9457, 0.9458, 0.9386]
slashdot_p1 = [0.8137, 0.8260, 0.8518, 0.8642, 0.8763, 0.8775, 0.8800, 0.8776, 0.8754, 0.8464]

epinions_f1 = [0.9137, 0.9250, 0.9419, 0.9484, 0.9498, 0.9490, 0.9462, 0.9439, 0.9448, 0.9387]
slashdot_f1 = [0.8133, 0.8267, 0.8514, 0.8680, 0.8785, 0.8784, 0.8772, 0.8765, 0.8748, 0.8450]

rank = [5, 10, 20, 30, 40, 50, 100, 200]
epinions_p2 = [0.9395, 0.9443, 0.9463, 0.9475, 0.9471, 0.9449, 0.9399, 0.9244]
slashdot_p2 = [0.8663, 0.8693, 0.8762, 0.8746, 0.8782, 0.8750, 0.8581, 0.8325]

epinions_f2 = [0.9400, 0.9471, 0.9487, 0.9479, 0.9485, 0.9467, 0.9416, 0.9289]
slashdot_f2 = [0.8672, 0.8719, 0.8749, 0.8762, 0.8763, 0.8719, 0.8618, 0.8420]

plt.plot(rank, epinions_p2, label = "Epinions Partially", marker = 'v', linestyle = '--')
plt.plot(rank, epinions_f2, label = "Epinions Fully", marker = '*', linestyle = '--')

plt.plot(rank, slashdot_p2, label = "Slashdot Partially", marker = 'o', linestyle = '--')
plt.plot(rank, slashdot_f2, label = "Slashdot Fully", marker = 's', linestyle = '--')

plt.xlabel("$r$", fontsize = 14)
# plt.xlabel("$r$", fontsize = 14)
plt.ylabel("Accuracy", fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.ylim(0.75, 1)
plt.xlim(0, 200)
# plt.title("Slashdot with Square Loss")
plt.legend(loc = 0, fontsize = 14)
plt.grid(True)

plt.show()
