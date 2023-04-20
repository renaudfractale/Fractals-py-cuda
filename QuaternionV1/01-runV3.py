import numpy as np
import quaternion
import Libs






nbPoint = 500
xmin = -2.0
xmax = 0.0
ymin = -2.0
ymax = 0.0
zmin = -2.0
zmax = 0.0
iterMax = 250
qMaster = np.quaternion(0.5, 0.02, -0.2, 0.01)
Rmax = 8
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
            
            q = np.quaternion(0.0, 0.0, 0.0, 0.0)
            match str(Parameter.axeT_Name).lower():
                case 'w':
                    qInit = np.quaternion(
                        Parameter.axeT_Value, xFloat, yFloat, zFloat)
                case 'x':
                    qInit = np.quaternion(
                        xFloat, Parameter.axeT_Value, yFloat, zFloat)
                case 'y':
                    qInit = np.quaternion(
                        xFloat, yFloat, Parameter.axeT_Value, zFloat)
                case 'z':
                    qInit = np.quaternion(
                        xFloat, yFloat, zFloat, Parameter.axeT_Value)
                case _:
                    qInit = np.quaternion(
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