import numpy as np
import quaternion
from tempfile import TemporaryFile
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import Libs


PathFile= "2023-04-19_18-41-34.0262410-Filter.npz"

Data = Libs.OpenFileNpz(PathFile)

tab_Source = Data["data"]
JsonString = Data["jsonText"]

Parameter = Libs.Json2Objet(JsonString)


lenPlotEnd = 50
lenPlotStart = 30



#print("i+lenHistostart =  "+str(type(i+lenHistostart)))
##
#filter_arr = tab_Source.any >  lenPlotStart-1 and tab_Source.any < lenPlotEnd+1
#print("filter_arr type " + str(type(filter_arr)))
Temp = tab_Source[(tab_Source  >  (lenPlotStart-1)) & (tab_Source < (lenPlotEnd+1))]
print(Temp.size)
X = np.zeros(Temp.size,np.float16)
Y = np.zeros(Temp.size,np.float16)
Z = np.zeros(Temp.size,np.float16)
C = np.zeros((Temp.size,4),np.float16)

tab_Index= np.arange(0,tab_Source.size)
#intX = np.trunc(tab_Index / (Parameter["nbPoint"]*Parameter["nbPoint"]))
#intY = np.trunc((tab_Index % (Parameter["nbPoint"]*Parameter["nbPoint"]))/Parameter["nbPoint"])
#intZ = tab_Index % Parameter["nbPoint"]
#print("*******************")
#print(max(intX))
#print(min(intX))
#print("*******************")
#print("*******************")
#print(max(intY))
#print(min(intY))
#print("*******************")
#print("*******************")
#print(max(intZ))
#print(min(intZ))
#print("*******************")
Arange = range(lenPlotStart,lenPlotEnd+1)
Plage = range(lenPlotStart,lenPlotEnd+1)
Plagemin=min(Plage)
Plagemax=max(Plage)
PlageEcart=max(Plage)-min(Plage)

R = np.linspace(0,255)
norm= plt.Normalize(0,255)
color=plt.cm.hsv(norm(R))
print(color.size)

index = -1
for i in Arange:
    filter_arr = tab_Source ==  i
    tab_IndexF = tab_Index[filter_arr]
    Xint = np.trunc(tab_IndexF / (Parameter["nbPoint"]*Parameter["nbPoint"]))
    Yint = np.trunc((tab_IndexF % (Parameter["nbPoint"]*Parameter["nbPoint"]))/Parameter["nbPoint"])
    Zint = tab_IndexF % Parameter["nbPoint"]
    print("i = "+str(i))
    print("size = "+str(tab_IndexF.size))    
    #print(Xint)
    #print(Yint)
    #print(Zint)
    XFloat = (np.float16(Xint)*Parameter["pasX"]/float(Parameter["nbPoint"]-1))+Parameter["xmin"]
    YFloat = (np.float16(Yint)*Parameter["pasY"]/float(Parameter["nbPoint"]-1))+Parameter["ymin"]
    ZFloat = (np.float16(Zint)*Parameter["pasZ"]/float(Parameter["nbPoint"]-1))+Parameter["zmin"]
    #print(XFloat)
    #print(YFloat)
    #print(ZFloat)
    #print(max(ZFloat))
    #print(min(ZFloat))    
    for k in np.arange(0,tab_IndexF.size):
        index+=1
        X[index] =  XFloat[k]
        Y[index] =  YFloat[k]
        Z[index] =  ZFloat[k]
        C[index] =  color[int(float(i-Plagemin)/float(PlageEcart)*((color.size/4)-1))]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(X, Y, Z,color=C)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
"""
i=-1
k=-1
for source in tab_Source:
    i+=1
    if(source>(lenPlotStart-1) and source < (lenPlotEnd+1)):
        k+=1
        Xint= int((i-(i % (Parameter["nbPoint"]*Parameter["nbPoint"])))/(Parameter["nbPoint"]*Parameter["nbPoint"]))
        print("i = "+str(i))
        print("Xint = "+str(Xint))
        print("-----------------")
        



tab_Index= np.arange(0,tab_Source.size)
tab_SourceF = tab_Source[filter_arr]
tab_IndexF = tab_Index[filter_arr]
print("tab_IndexF.size = " + str(tab_IndexF.size))
Xint = (tab_IndexF % (Parameter["nbPoint"]*Parameter["nbPoint"]))
Y = np.zeros(tab_IndexF.size,np.float16)
Z = np.zeros(tab_IndexF.size,np.float16)
C = np.zeros(tab_IndexF.size,np.int16)
print(max(Xint))
print(tab_IndexF)
print(tab_SourceF)
print(filter_arr)
print(tab_Source)
print(tab_Index[tab_Source.size-1])
print(tab_IndexF[tab_IndexF.size-1])
"""

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
"""