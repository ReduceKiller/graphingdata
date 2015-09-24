import matplotlib.pyplot as plt

no_breeding = int(input("Number of breeding: "))
no_feeding = int(input("Number of feeding: "))
no_mating = int(input("Number of mating: "))

a = 'Feeding'
b = 'Mating'
c = 'Breeding'

D = {c: no_breeding,  a: no_feeding, b: no_mating}


plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), list(D.keys()))

plt.show()