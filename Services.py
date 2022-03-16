#Get all the running process on the machine, test on win 10
import psutil,os,signal
listproc=[]
for process in psutil.process_iter():
    listproc.append(process.name())
    for name in listproc:
        print(name)
        
