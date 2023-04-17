import numpy as np
import quaternion
from tempfile import TemporaryFile
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
with open('test-2000.npy', 'rb') as f:
    tab_int = np.load(f)
    tab_pos = np.load(f)
    nbRange = np.load(f)

""""
histo= np.zeros(len(nbRange+2),np.int32)
for i in nbRange:
    histo[tab_int[i]]+=1
"""

fig = plt.figure()
ax = fig.add_subplot()

dim = 20
w = 0.75
dimw = w / dim

ax.hist(tab_int, bins=len(nbRange+1))

plt.show()