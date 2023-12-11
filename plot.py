import matplotlib.pyplot as plt



f = open("output/out_2comp03.ctt", "r")

title = f.readline() + f.readline()

y = [int(line.strip()) for line in f.readlines()]

x = range(len(y))

fig, ax = plt.subplots()

ax.plot(x, y, label = "solution" )
ax.plot(x, len(y)*[64], label = "upper bound")
plt.xlabel("iterações")
plt.ylabel("f")
plt.axis((0, len(y), 0, 900))
plt.title(title)
plt.legend()

plt.show()
