import numpy as np
import quaternion
import Libs
import copy 
PathFile= "2023-04-19_18-41-34.0262410.npz"

Data = Libs.OpenFileNpz(PathFile)

tab_Source = Data["data"]
tab_Filter = copy.copy(tab_Source)
JsonString = Data["jsonText"]

Parameter = Libs.Json2Objet(JsonString)

for xInt in range(1, Parameter['nbPoint']-1):
    print("xInt = "+str(xInt)+" sur "+str(Parameter['nbPoint']))
    for yInt in range(1, Parameter['nbPoint']-1):
        # z Int
        for zInt in range(1, Parameter['nbPoint']-1):
             # z Int
            #position in Liste
            pLen = Libs.PoseXYZ2Poselen(xInt,yInt,zInt,Parameter['nbPoint'])
            iter = tab_Source[pLen]
            bool = False
            for x in range(-1,1):
                for y in range(-1,1):
                    for z in range(-1,1):
                        pLenD = Libs.PoseXYZ2Poselen(xInt+x,yInt+y,zInt+z,Parameter['nbPoint'])
                        bool = iter != tab_Source[pLenD]
                        if bool:
                             break
                    if bool:
                         break
                if bool:
                     break
            if bool == False:
                tab_Filter[pLen]=0


strNow=PathFile.replace(".npz", "-Filter")
np.savez_compressed(strNow,data=tab_Filter,jsonText=JsonString)
