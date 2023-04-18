import numpy as np
import quaternion
from tempfile import TemporaryFile
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
with open('test-250.npy', 'rb') as f:
    tab_int = np.load(f)
    tab_pos = np.load(f)
    nbRange = np.load(f)

fig = plt.figure()
ax = fig.add_subplot()
ax.set_yscale('log')
lenHistoEnd = 20
lenHistostart = 0

histo= np.zeros((lenHistoEnd-lenHistostart)+1,np.int32)
for i in nbRange:
    if(tab_int[i]<=lenHistoEnd and tab_int[i]>=lenHistostart):
        histo[tab_int[i]-lenHistostart]+=1
ax.plot(histo)
plt.show()

"""


dim = 20
w = 0.75
dimw = w / dim

ax.hist(tab_int, bins=len(nbRange+1))


"""