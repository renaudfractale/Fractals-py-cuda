def PoseXYZ2Poselen(xInt,yInt,zInt,nbPoints):
    return xInt+yInt*nbPoints+zInt*pow(nbPoints,2)

