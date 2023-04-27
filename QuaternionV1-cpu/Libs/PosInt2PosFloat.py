def PosInt2PosFloat(pInt, nbPoint, pas,pmin):
    pFloat = float(pInt)/float(nbPoint-1)*pas+pmin
    return pFloat