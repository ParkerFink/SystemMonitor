import psutil
import GPUtil
import tkinter
import threading
import time
import os


#thread functions
def getCPU():
    while True:
        time.sleep(3)
        cpu_percent = psutil.cpu_percent()
        label_cpu.config(text="CPU Useage: " + str(cpu_percent) + "%")

def getRAM():
    while True:
        time.sleep(3)
        ram_percent = psutil.virtual_memory()[2]
        label_ram.config(text="RAM Useage: " + str(ram_percent) + "%")

def getCPUTemp():
    while True:
        time.sleep(3)
        cpuTemp = psutil.sensors_temperatures()
        for a,b in cpuTemp.items():
            for x in b:
                label_cpu_temp.config(text= "CPU Temp: " + str(x.current) + 'c')

def getGPU():
    while True:
        time.sleep(3)
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            load = gpu.load * 100
            label_gpu.config(text="GPU Load: " + str(load) + "%")
            
                


#threads
cpuThread = threading.Thread(target=getCPU)
ramThead = threading.Thread(target=getRAM)
cpuTempThread = threading.Thread(target=getCPUTemp)
gpuThread = threading.Thread(target=getGPU)

#main window
window = tkinter.Tk()
window.geometry('275x200')
window.title("System Monitor")

global label_cpu
global label_ram
global label_cpu_temp
global label_gpu


cpuThread.start()
ramThead.start()
cpuTempThread.start()
gpuThread.start()



numOfCCores = tkinter.Label(text= "Number of cores: " + str(os.cpu_count()))
numOfCCores.pack()

label_cpu = tkinter.Label(text= "CPU N/A")
label_cpu.pack()

label_cpu_temp = tkinter.Label(text= "CPU Temp N/A")
label_cpu_temp.pack()

label_ram = tkinter.Label(text= "RAM N/A")
label_ram.pack()

label_gpu = tkinter.Label(text= "GPU N/A")
label_gpu.pack()


window.mainloop()
