import numpy as np
import quaternion
from tempfile import TemporaryFile
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import Libs
import copy 
PathFile= "2023-04-19_18-41-34.0262410-Filter.npz"

Data = Libs.OpenFileNpz(PathFile)

tab_Source = Data["data"]
JsonString = Data["jsonText"]

Parameter = Libs.Json2Objet(JsonString)
fig = plt.figure()
ax = fig.add_subplot()
ax.set_yscale('log')
lenHistoEnd = 70
lenHistostart = 1

histo= np.zeros((lenHistoEnd-lenHistostart)+1,np.int32)
#print(str(type(tab_Source)))
for i in range(0,(lenHistoEnd-lenHistostart)+1):
    #print("i+lenHistostart =  "+str(type(i+lenHistostart)))
    filter_arr = tab_Source ==  i+lenHistostart
    newarr = tab_Source[filter_arr]
    #print("newarr=  "+str(type(newarr))+"==> "+str(newarr.size))
    histo[i] = newarr.size
"""
for value in tab_Source:
    if(value<=lenHistoEnd and value>=lenHistostart):
        histo[value-lenHistostart]+=1
"""
ax.plot(histo)
plt.show()