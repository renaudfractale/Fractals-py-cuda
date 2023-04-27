import numpy as np
import quaternion
import Libs
import copy
import sys, getopt
import uuid

# get argument list using sys module
myopts, args = getopt.getopt(sys.argv[1:],"w:x:y:z:")
qw=None
qx=None
qy=None
qz=None

###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-w':
        qw=float(a)
    elif o == '-x':
        qx=float(a)
    elif o == '-y':
        qy=float(a)
    elif o == '-z':
        qz=float(a)
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])

print("qw="+str(qw))
print("qx="+str(qx))
print("qy="+str(qy))
print("qz="+str(qz))
print(str(str(uuid.uuid4())))
def Plot(qw,qx,qy,qz):
    nbPoint = 500
    xmin = -2.0
    xmax = 2.0
    ymin = -2.0
    ymax = 2.0
    zmin = -2.0
    zmax = 2.0
    iterMax = 250
    qMaster = np.quaternion(qw, qx, qy, qz)
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



    strNow=Libs.Now2Str()+"_"+str(uuid.uuid4())

    np.savez_compressed(strNow,data=tab,jsonText=Parameter.toJSON())

    f = open(strNow+".json", "w")
    f.write(Parameter.toJSON())
    f.close()
    tab_Filter = copy.copy(tab)
    #Filtrage 
    for xInt in range(1, Parameter['nbPoint']-1):
        print("xInt = "+str(xInt)+" sur "+str(Parameter['nbPoint']))
        for yInt in range(1, Parameter['nbPoint']-1):
            # z Int
            for zInt in range(1, Parameter['nbPoint']-1):
                # z Int
                #position in Liste
                pLen = Libs.PoseXYZ2Poselen(xInt,yInt,zInt,Parameter['nbPoint'])
                iter = tab[pLen]
                bool = False
                for x in range(-1,1):
                    for y in range(-1,1):
                        for z in range(-1,1):
                            pLenD = Libs.PoseXYZ2Poselen(xInt+x,yInt+y,zInt+z,Parameter['nbPoint'])
                            bool = iter != tab[pLenD]
                            if bool:
                                break
                        if bool:
                            break
                    if bool:
                        break
                if bool == False:
                    tab_Filter[pLen]=0


    strNow=strNow+"-Filter"
    np.savez_compressed(strNow,data=tab_Filter,jsonText=Parameter.toJSON())

Plot(qw,qx,qy,qz)

