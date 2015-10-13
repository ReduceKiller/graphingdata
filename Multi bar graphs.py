__author__ = 'David Pham'
import matplotlib.pyplot as plt
import random

D = {'Feed': 1,  'Resting': 1, 'Flying': 2}

C = {'Feed': 4,  'Resting': 6, 'Flying': 7}

#title2 = input("Title of the graph?: ")
#xlabel = input("")


for a in range(0,2):
    stored_color = False
    color_letter = ['r','b','c','g']
    color_picked = random.choice(color_letter)

    while color_picked == stored_color:
        color_picked = random.choice(color_letter)


    bar_graph1 = plt.bar(range(len(D)), D.values(), align='center',color = color_picked, width = 0.4)
    plt.xticks(range(len(D)), list(D.keys()))

    stored_color = color_picked


plt.show()
