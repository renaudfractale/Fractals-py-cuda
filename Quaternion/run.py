import numpy as np
import quaternion
import matplotlib.pyplot as plt
from tempfile import TemporaryFile

outfile = TemporaryFile()

q0 = np.quaternion(1, 0, 0, 0)
q1 = np.quaternion(1, 2, 3, 5)
q2 = np.quaternion(5, 6, 7, 8)
a = q1 * q2
b = np.array([q1, q2])
c = np.exp(b)

print(a)
print(b)
print(c)

pas = 0.01

xmin = -0.7
xmax = 0.7
xpas = pas
xrange = np.arange(xmin, xmax, xpas)

ymin = -0.7
ymax = 0.7
ypas = pas
yrange = np.arange(ymin, ymax, ypas)

zmin = -0.7
zmax = 0.7
zpas = pas
zrange = np.arange(zmin, zmax, zpas)

nbIter = 2000
iterRange = range(0, nbIter)

nbrange = xrange.size * yrange.size * zrange.size

nbRange = range(0, nbrange)


print(nbrange)
print(zrange.size)
tab_int = np.zeros(nbrange, dtype=np.int16)
tab_pos = np.zeros((nbrange, 3), dtype=np.float16)
tab_q = np.zeros(nbrange, dtype=np.quaternion)
i = -1
for x in xrange:
    for y in yrange:
        for z in zrange:
            i += 1
            tab_q[i] = np.quaternion(0, x, y, z)
            tab_int[i] = -1
            tab_pos[i] = [x, y, z]

qMaster = np.quaternion(0, 0.02, -0.02, 0.01)
Rmax = 8.0
Rmax2 = Rmax*Rmax
for iter in iterRange:
    print(str(iter)+" sur "+str(nbIter))
    for i in nbRange:
        """print(tab_int[i])
        print(tab_int[i]+1)
        print(iter)
        tab_q[i] = tab_q[i]*tab_q[i]+qMaster
        print(tab_q[i].x*tab_q[i].x+tab_q[i].w*tab_q[i].w+tab_q[i].y*tab_q[i].y+tab_q[i].z*tab_q[i].z)
        print(tab_q[i].x*tab_q[i].x+tab_q[i].w*tab_q[i].w+tab_q[i].y*tab_q[i].y+tab_q[i].z*tab_q[i].z<Rmax2)
        break"""
        if (tab_int[i]+1 == iter):
            tab_q[i] = tab_q[i]*tab_q[i]+qMaster
            if (tab_q[i].x*tab_q[i].x+tab_q[i].w*tab_q[i].w+tab_q[i].y*tab_q[i].y+tab_q[i].z*tab_q[i].z < Rmax2):
                tab_int[i] = iter

print(tab_int)

with open('test-'+str(nbIter)+'.npy', 'wb') as f:
    np.save(f, tab_int)
    np.save(f, tab_pos)
    np.save(f,nbRange)
