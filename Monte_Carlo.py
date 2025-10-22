import matplotlib.pyplot as plt
import numpy as np

import matplotlib.patches as patches

import matplotlib.pyplot as plt
import numpy as np
import math 


fig1, ax = plt.subplots()

ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_box_aspect(1)

square = patches.Rectangle((-0.5, -0.5), 1, 1, edgecolor='red', facecolor='none')
ax.add_patch(square)

circle = plt.Circle ((0, 0 ), 0.5, edgecolor='red', alpha=0.1)

#ændre antal af prikker i cirklen
n = 1000

x = np.random.uniform(-0.5, 0.5, n)
y = np.random.uniform(-0.5, 0.5, n)

circle_center = (0, 0)
radius = 0.5 
count = 0 
xi = 0
yi = 0

#The zip() function in Python is a neat tool that allows you to combine multiple lists or other iterables 
# (like tuples, sets, or even strings) into one iterable of tuples. 
# Think of it like a zipper on a jacket that brings two sides together
for xi, yi in zip(x, y):
    distance = math.sqrt(xi**2 + yi**2)
    if distance <= radius:
        count +=1

pi = (count*4)/n 

print (f"there are {count} dots in the circle")
print (f"pi = {pi}")

plt.scatter(x, y, alpha=0.2)
ax.add_patch(circle)
plt.show()