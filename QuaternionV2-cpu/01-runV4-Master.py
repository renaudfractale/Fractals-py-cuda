import numpy as np
import quaternion
import psutil
import os
import threading
import Libs
import time

# Getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()
 
cpu_usage = (load15/os.cpu_count()) * 100
 
print("The CPU usage is : ", psutil.cpu_percent())

if __name__ == "__main__":
    threads = (os.cpu_count()-1)*2   # Number of threads to create
    print("threads Max", threads)
    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list 
    """
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=list_append(size, i, out_list))
        jobs.append(thread)
    """
    start=-2.0
    end=2.0
    step=0.2

    jobs = []
    Countthreads =0
    nPRange= np.arange(start,end,step)
    for qw in  nPRange:
        for qx in  nPRange:
            for qy in  nPRange:
                for qz in  nPRange:
                    print("% CPU : ", psutil.cpu_percent())
                    if Countthreads<threads:
                        Countthreads+=1
                        run = ["Libs.MakeQ","-w",str(qw),"-x",str(qx),"-y",str(qy),"-z",str(qz)]
                        print(run)
                        thread = threading.Thread(target=Libs.MakeQ, 
                                          args=(qw, qx, qy, qz))
                        jobs.append(thread)
                    elif Countthreads==threads:
                        #Start
                        print("Start")
                        for j in jobs:
                            j.start()
                        #Join
                        print("Join")
                        for j in jobs:
                            j.join()
                        #Rests
                        print("Rests")
                        Countthreads =0
                        jobs = []


                        




"""
qw=0.1
qx=0.11
qy=0.111
qz=0.1111

run = ["python","01-runV4-Slave.py","-w",str(qw),"-x",str(qx),"-y",str(qy),"-z",str(qz)]
print(run)
result = subprocess.run(run, shell=True, capture_output=True, text=True)
print(result.stdout)

start=-2.0
end=2.0
step=0.2
for qw in np.arange(start,end,step):
    for qx in np.arange(start,end,step):
        for qy in np.arange(start,end,step):
            for qz in np.arange(start,end,step):
                 if psutil.cpu_percent()<85.0:
                    run = ["python","01-runV4-Slave.py","-w",str(qw),"-x",str(qx),"-y",str(qy),"-z",str(qz)]
                    print(run)
                    subprocess.run(run, shell=True, capture_output=True, text=True)
"""