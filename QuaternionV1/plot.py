import numpy as np
import quaternion
from tempfile import TemporaryFile
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
with open('test.npy', 'rb') as f:
    tab_int = np.load(f)
    tab_pos = np.load(f)
    nbRange = np.load(f)

"""
histo= np.zeros(21,np.int32)
for i in nbRange:
    histo[tab_int[i]]+=1


fig = plt.figure()
ax = fig.add_subplot()

dim = 20
w = 0.75
dimw = w / dim

ax.hist(tab_int, bins=20)

plt.show()
"""
j=0
for i in nbRange:
    if(tab_int[i]>10 and tab_int[i]<17 ):
        j+=1
x= np.zeros(j,np.float16)
y= np.zeros(j,np.float16)
z= np.zeros(j,np.float16)
c= np.zeros(j,np.int16)
j=-1
for i in nbRange:
    if(tab_int[i]>10 and tab_int[i]<17 ):
        j+=1
        x[j] = tab_pos[i][0]
        y[j] = tab_pos[i][1]
        z[j] = tab_pos[i][2]
        c[j] = tab_int[i]



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, c)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
