import psutil
import GPUtil
import tkinter
import threading
import time
import os


#thread functions

def getSysInfo():
    while True:
        time.sleep(3)

        cpu_percent = psutil.cpu_percent()
        label_cpu.config(text="CPU Useage: " + str(cpu_percent) + "%")

        ram_percent = psutil.virtual_memory()[2]
        label_ram.config(text="RAM Useage: " + str(ram_percent) + "%")

        cpuTemp = psutil.sensors_temperatures()
        for a,b in cpuTemp.items():
            for x in b:
                label_cpu_temp.config(text= "CPU Temp: " + str(x.current) + 'c')

        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            load = gpu.load * 100
            label_gpu.config(text="GPU Load: " + str(load) + "%")

            
                


#threads
secondaryThread = threading.Thread(target=getSysInfo)

#main window
window = tkinter.Tk()
window.geometry('275x200')
window.title("System Monitor")

global label_cpu
global label_ram
global label_cpu_temp
global label_gpu


secondaryThread.start()



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
