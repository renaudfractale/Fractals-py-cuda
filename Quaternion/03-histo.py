import numpy as np
import quaternion
from tempfile import TemporaryFile
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import Libs
import copy 
PathFile= "2023-04-18_23-36-53.0476124.npz"

Data = Libs.OpenFileNpz(PathFile)

tab_Source = Data["data"]
JsonString = Data["jsonText"]

Parameter = Libs.Json2Objet(JsonString)
fig = plt.figure()
ax = fig.add_subplot()
ax.set_yscale('log')
lenHistoEnd = 30
lenHistostart = 1

histo= np.zeros((lenHistoEnd-lenHistostart)+1,np.int32)
for value in tab_Source:
    if(value<=lenHistoEnd and value>=lenHistostart):
        histo[value-lenHistostart]+=1
ax.plot(histo)
plt.show()