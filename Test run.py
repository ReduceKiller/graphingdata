import matplotlib.pyplot as plt
import random

D = {'Feed': 1,  'Resting': 1, 'Flying': 2}

title2 = input("Title of the graph?: ")


bar_graph = plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), list(D.keys()))

plt.title(title2)
plt.ylabel("Frequency")
plt.xlabel("Behaviours")


#c = random.choice(color)

#bar_graph[0:range(len(D))].set_color(c)
plt.show()



