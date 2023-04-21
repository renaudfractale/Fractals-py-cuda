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


lenPlotEnd = 35
lenPlotStart = 30
#print("i+lenHistostart =  "+str(type(i+lenHistostart)))
filter_arr = tab_Source[(tab_Source  >  (lenPlotStart-1)) & (tab_Source < (lenPlotEnd+1))]
#filter_arr = tab_Source.any >  lenPlotStart-1 and tab_Source.any < lenPlotEnd+1
print("filter_arr type " + str(type(filter_arr)))

tab_Index= np.arange(0,tab_Source.size)

tab_SourceF = tab_Source[filter_arr]
tab_IndexF = tab_Index[filter_arr]
print("tab_IndexF.size = " + str(tab_IndexF.size))
X = np.zeros(tab_IndexF.size,np.float16)
Y = np.zeros(tab_IndexF.size,np.float16)
Z = np.zeros(tab_IndexF.size,np.float16)
C = np.zeros(tab_IndexF.size,np.int16)



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
