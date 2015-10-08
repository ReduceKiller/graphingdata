import matplotlib.pyplot as plt
import random

D = {'Feed': 1,  'Resting': 1, 'Flying': 2}

C = {'Feed': 1,  'Resting': 1, 'Flying': 2}

#title2 = input("Title of the graph?: ")
#xlabel = input("")


for a in range(0,2):
    stored_color = False
    color_letter = ['r','b','c','g']
    color_picked = random.choice(color_letter)

    while color_picked == stored_color:
        color_picked = random.choice(color_letter)


    plt.figure()
    bar_graph = plt.bar(range(len(D)), D.values(), align='center',color = color_picked)
    plt.xticks(range(len(D)), list(D.keys()))

    stored_color = color_picked


plt.show()

'''

bar_graph2 = plt.bar(range(len(C)), C.values(), align='center')
plt.figure()
plt.xticks(range(len(C)), list(C.keys()))

#c = random.choice(color)

#bar_graph[0:range(len(D))].set_color(c)

'''


'''
plt.title(title2)
plt.ylabel("Frequency")
plt.xlabel("Behaviours")
'''

