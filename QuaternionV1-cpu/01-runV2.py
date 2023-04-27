import numpy as np
import quaternion
import matplotlib.pyplot as plt
from tempfile import TemporaryFile
import json
from datetime import datetime


class Parameters(object):
    def __init__(self, nbPoint=1000, xmin=-1, xmax=0, ymin=-1, ymax=0, zmin=-1, zmax=0, iterMax=200, qMaster=np.quaternion(0.0, 0.0, 0.0, 0.0), Rmax=8, RmaxPower=pow(8, 2), axeT_Name="w", axeT_Value=0.5):
        self.nbPoint = nbPoint
        self.xmin = xmin
        self.xmax = xmax
        self.pasX = xmax-xmin
        self.ymin = ymin
        self.ymax = ymax
        self.pasY = ymax-ymin
        self.zmin = zmin
        self.zmax = zmax
        self.pasZ = zmax-zmin
        self.iterMax = iterMax
        self.qMasterW = qMaster.w
        self.qMasterX = qMaster.x
        self.qMasterY = qMaster.y
        self.qMasterZ = qMaster.z
        self.Rmax = Rmax
        self.RmaxPower = RmaxPower
        self.axeT_Name = axeT_Name
        self.axeT_Value = axeT_Value

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


nbPoint = 1000
xmin = -1.5
xmax = 0
ymin = -1.5
ymax = 0
zmin = -1.5
zmax = 0
iterMax = 250
qMaster = np.quaternion(0.5, 0.02, -0.2, 0.01)
Rmax = 8
RmaxPower = pow(Rmax, 2)
axeT_Name = "z"
axeT_Value = 0.5

Parameter = Parameters(nbPoint, xmin, xmax, ymin, ymax,
                       zmin, zmax, iterMax, qMaster,Rmax, RmaxPower,axeT_Name,axeT_Value)

tab = np.zeros((nbPoint, nbPoint, nbPoint), dtype=np.int16)


def PosInt2PosFloat(pInt, nbPoint, pas,pmin):
    pFloat = float(pInt)/float(nbPoint-1)*pas+pmin
    return pFloat

iterRange = range(1, Parameter.iterMax)
qMaster = np.quaternion(Parameter.qMasterW,Parameter.qMasterX,Parameter.qMasterY,Parameter.qMasterZ)
for xInt in range(0, Parameter.nbPoint):
    print("xInt = "+str(xInt)+" sur "+str(Parameter.nbPoint))
    xFloat = PosInt2PosFloat(xInt, Parameter.nbPoint, Parameter.pasX,Parameter.xmin)
    print("xFloat = "+str(xFloat))
    for yInt in range(0, Parameter.nbPoint):
        yFloat = PosInt2PosFloat(yInt, Parameter.nbPoint, Parameter.pasY,Parameter.ymin)
        for zInt in range(0, Parameter.nbPoint):
            zFloat = PosInt2PosFloat(zInt, Parameter.nbPoint, Parameter.pasZ,Parameter.zmin)
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
                tab[xInt][yInt][zInt] = iter
                norme = q.w*q.w+q.x*q.x+q.y*q.y+q.z*q.z
                if (norme > Parameter.RmaxPower):
                    break


def Now2Str():
    # current date and time
    now = datetime.now()
    #Date
    year = str(now.year)
    month = ("00"+str(now.month))[-2:]
    day = ("00"+str(now.day))[-2:]
    #time
    hour = ("00"+str(now.hour))[-2:]
    minute = ("00"+str(now.minute))[-2:]
    second = ("00"+str(now.second))[-2:]
    microsecond= ("0000000"+str(now.microsecond))[-7:]
    return year+"-"+month+"-"+day+"_"+hour+"-"+minute+"-"+second+"."+microsecond


strNow=Now2Str()
with open(strNow+'.npy', 'wb') as f:
    np.save(f, tab)

f = open(strNow+".json", "w")
f.write(Parameter.toJSON())
f.close()