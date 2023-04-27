import json
import numpy as np

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


