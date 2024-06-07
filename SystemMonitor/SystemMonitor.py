import psutil
import tkinter
import threading
import time

from gpiozero import CPUTemperature

#thread functions
def getCPU():
    while True:
        time.sleep(1)
        cpu_percent = psutil.cpu_percent()
        label_cpu.config(text="CPU Useage: " + str(cpu_percent) + "%")

def getRAM():
    while True:
        time.sleep(1)
        ram_percent = psutil.virtual_memory()[2]
        label_ram.config(text="RAM Useage: " + str(ram_percent) + "%")

def getCPUTemp():
    while True:
        time.sleep(1)
        cpuTemp = psutil.sensors_temperatures()
        for a,b in cpuTemp.items():
            for x in b:
                #print(x.current)
                label_cpu_temp.config(text= "CPU Temp: " + str(x.current) + 'c')

    

#threads
cpuThread = threading.Thread(target=getCPU)
ramThead = threading.Thread(target=getRAM)
cpuTempThread = threading.Thread(target=getCPUTemp)


#main window
window = tkinter.Tk()
window.geometry('275x200')
window.title("System Monitor")

global label_cpu
global label_ram

cpuThread.start()
ramThead.start()
cpuTempThread.start()

label_cpu = tkinter.Label(text="CPU N/A")
label_cpu.pack()

label_cpu_temp = tkinter.Label(text="CPU Temp N/A")
label_cpu_temp.pack()

label_ram = tkinter.Label(text="RAM N/A")
label_ram.pack()




window.mainloop()
