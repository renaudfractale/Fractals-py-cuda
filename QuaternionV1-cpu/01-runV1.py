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
print(q1)
print(q1.w)
"""
pas = 0.005

xmin = -1.5
xmax = 0
xpas = pas
xrange = np.arange(xmin, xmax, xpas)

ymin = -1.5
ymax = 0
ypas = pas
yrange = np.arange(ymin, ymax, ypas)

zmin = -1.5
zmax = 0
zpas = pas
zrange = np.arange(zmin, zmax, zpas)

nbIter = 250
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

qMaster = np.quaternion(0.5, 0.02, -0.2, 0.01)
Rmax = 8.0
Rmax2 = Rmax*Rmax
for i in nbRange:
    print(str(i)+" sur "+str(nbrange))
    for iter in iterRange:
        tab_q[i] = tab_q[i]*tab_q[i]+qMaster
        tab_int[i] = iter
        if (tab_q[i].x*tab_q[i].x+tab_q[i].w*tab_q[i].w+tab_q[i].y*tab_q[i].y+tab_q[i].z*tab_q[i].z > Rmax2):
            break
               

print(tab_int)

with open('test-'+str(nbIter)+'.npy', 'wb') as f:
    np.save(f, tab_int)
    np.save(f, tab_pos)
    np.save(f,nbRange)
    np.save(f,nbIter)
"""