import matplotlib.pyplot as plt
import math
import random


N = 50
step = 4 / 100
listOft = [1 + step * i for i in range(100)]
n = 1
a = random.uniform(0.7, 1) 
b = random.uniform(1, 1.5) / a  
var = 0
maxY = 0
minY = 0
listOfy = []

for t in listOft:
    for k in range(N):
        var += pow(a, n) * math.cos(math.pi * pow(b, n) * t)
        n += 1
    if maxY < var:
        maxY = var
        tOfmaxY = t
    if minY > var:
        minY = var
        tOfminY = t
    listOfy.append(var)
    n=1

maxY = round(maxY, 2)
minY = round(minY, 2)
# print(maxY)
# print(minY)

plt.plot(listOft, listOfy)
plt.ylim([minY, maxY])
plt.xlabel('t-axis')
plt.ylabel('y-axis')
plt.text(tOfmaxY, maxY, str(maxY), fontsize=12, ha='left', va='bottom')
plt.text(tOfminY, minY, str(minY), fontsize=12, ha='left', va='bottom')
plt.grid(True)
plt.show()