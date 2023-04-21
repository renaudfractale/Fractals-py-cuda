import numpy as np
import quaternion
import Libs

nbPoint = 1000
xmin = -4.0
xmax = 4.0
ymin = -4.0
ymax = 4.0
zmin = -4.0
zmax = 4.0
iterMax = 250
qMaster = np.quaternion(0.5, 0.02, -0.2, 0.01)
Rmax = 4
RmaxPower = pow(Rmax, 2)
axeT_Name = "z"
axeT_Value = 0.5

Parameter = Libs.Parameters(nbPoint, xmin, xmax, ymin, ymax,
                       zmin, zmax, iterMax, qMaster,Rmax, RmaxPower,axeT_Name,axeT_Value)

tab = np.zeros(nbPoint* nbPoint* nbPoint, dtype=np.int16)
if Parameter.iterMax<=253:
    tab = np.zeros(nbPoint* nbPoint* nbPoint, dtype=np.int8)




iterRange = range(1, Parameter.iterMax)
qMaster = np.quaternion(Parameter.qMasterW,Parameter.qMasterX,Parameter.qMasterY,Parameter.qMasterZ)
for xInt in range(0, Parameter.nbPoint):
    xFloat = Libs.PosInt2PosFloat(xInt, Parameter.nbPoint, Parameter.pasX,Parameter.xmin)
    print("xInt = "+str(xInt)+" sur "+str(Parameter.nbPoint)+ " ==> xFloat = "+str(xFloat))
    for yInt in range(0, Parameter.nbPoint):
        yFloat = Libs.PosInt2PosFloat(yInt, Parameter.nbPoint, Parameter.pasY,Parameter.ymin)
        for zInt in range(0, Parameter.nbPoint):
            zFloat =Libs.PosInt2PosFloat(zInt, Parameter.nbPoint, Parameter.pasZ,Parameter.zmin)
            #position in Liste
            pLen = Libs.PoseXYZ2Poselen(xInt,yInt,zInt,Parameter.nbPoint)
            #print("pLen = "+ str(pLen))
            q = np.quaternion(0.0, 0.0, 0.0, 0.0)
            match str(Parameter.axeT_Name).lower():
                case 'w':
                    q = np.quaternion(
                        Parameter.axeT_Value, xFloat, yFloat, zFloat)
                case 'x':
                    q = np.quaternion(
                        xFloat, Parameter.axeT_Value, yFloat, zFloat)
                case 'y':
                    q = np.quaternion(
                        xFloat, yFloat, Parameter.axeT_Value, zFloat)
                case 'z':
                    q = np.quaternion(
                        xFloat, yFloat, zFloat, Parameter.axeT_Value)
                case _:
                    q = np.quaternion(
                        Parameter.axeT_Value, xFloat, yFloat, zFloat)
                    
            for iter in iterRange:
                q = q*q+qMaster
                tab[pLen] = iter
                norme = q.w*q.w+q.x*q.x+q.y*q.y+q.z*q.z
                if (norme > Parameter.RmaxPower):
                    break



strNow=Libs.Now2Str()
np.savez_compressed(strNow,data=tab,jsonText=Parameter.toJSON())

f = open(strNow+".json", "w")
f.write(Parameter.toJSON())
f.close()