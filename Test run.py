import matplotlib.pyplot as plt

A = {('Sep', 'Feed', 'Haematopus longirostris/Australian Pied Oystercatcher'): 1, ('Sep', 'Resting', 'Haematopus longirostris/Australian Pied Oystercatcher'): 1, ('May', 'Flying', 'Haematopus longirostris/Australian Pied Oystercatcher'): 2, ('Jan', 'Feed', 'Haematopus longirostris/Australian Pied Oystercatcher'): 1, ('Feb', 'Feed', 'Haematopus longirostris/Australian Pied Oystercatcher'): 1, ('Mar', 'Flying', 'Haematopus longirostris/Australian Pied Oystercatcher'): 2, ('Apr', 'Feed', 'Haematopus longirostris/Australian Pied Oystercatcher'): 3, ('Aug', 'Feed', 'Haematopus longirostris/Australian Pied Oystercatcher'): 2, ('Apr', 'Resting', 'Haematopus longirostris/Australian Pied Oystercatcher'): 3, ('May', 'Resting', 'Haematopus longirostris/Australian Pied Oystercatcher'): 6, ('Oct', 'Feed', 'Haematopus longirostris/Australian Pied Oystercatcher'): 1, ('May', 'Feed', 'Haematopus longirostris/Australian Pied Oystercatcher'): 16, ('Mar', 'Resting', 'Haematopus longirostris/Australian Pied Oystercatcher'): 20, ('Oct', 'Resting', 'Haematopus longirostris/Australian Pied Oystercatcher'): 5, ('Mar', 'Feed', 'Haematopus longirostris/Australian Pied Oystercatcher'): 7, ('Apr', 'Flying', 'Haematopus longirostris/Australian Pied Oystercatcher'): 1}

A = list(A.items())

B = []

for item in A:
    if item[0][1] == "Feed":
        B.append((item[0][0],item[1]))

months = {'Sep': '09', 'Nov': '11', 'Feb': '02', 'Oct': '10', 'Jul': '07', 'Aug': '08', 'Mar': '03', 'May': '05', 'Jan': '01', 'Jun': '06', 'Dec': '12', 'Apr': '04'}

C = []

for item in B:
    C.append((months[item[0]],item[0],item[1]))

C.sort()

print(C)

'''
plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), list(D.keys()))

plt.show()

'''