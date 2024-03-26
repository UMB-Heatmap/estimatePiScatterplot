from matplotlib import pyplot as plt
from matplotlib import patches as patches
import random
import math

ptsIn, ptsTotal = 0, 0
x = []
y = []

#Adjusting figure shape
fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect('equal', adjustable = 'box')

#Add square and circle to plot
ax.add_patch(patches.Rectangle((-1, -1), 2, 2, edgecolor='black', facecolor='none'))
ax.add_patch(patches.Circle((0,0), 1, edgecolor='black', facecolor='none'))

#Generate random floats in range -1 to 1
for i in range(1000):
    x.append(random.uniform(-1,1))
    y.append(random.uniform(-1,1))

#Plot points, red if in the circle, blue if outside the circle
for j in range(1000):
    if (math.sqrt((x[j]**2)+(y[j]**2)) < 1):
        plt.scatter(x[j], y[j], color='red')
        ptsIn = ptsIn + 1
    else:
        plt.scatter(x[j], y[j], color='blue')
    ptsTotal = ptsTotal + 1

#Calculate pi and show scatterplot
pi = 4 * (ptsIn/ptsTotal)
plt.title("Pi = "+str(pi))
plt.show()