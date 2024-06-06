import psutil
import tkinter
import threading
import time


#thread functions
def getCPU():
    while True:
        time.sleep(1)
        cpu_percent = psutil.cpu_percent()
        label_cpu.config(text=cpu_percent)

def getRAM():
    while True:
        time.sleep(1)
        ram_percent = psutil.virtual_memory()[2]
        label_ram.config(text=ram_percent)

        
#threads
cpuThread = threading.Thread(target=getCPU)
ramThead = threading.Thread(target=getRAM)



#main window
window = tkinter.Tk()
window.geometry('800x500')
window.title("System Monitor")

global label_cpu
global label_ram

cpuThread.start()
ramThead.start()


label_cpu = tkinter.Label(text="CPU N/A")
label_cpu.pack()

label_cpu_temp = tkinter.Label(text="CPU Temp N/A")
label_cpu_temp.pack()

label_ram = tkinter.Label(text="RAM N/A")
label_ram.pack()




window.mainloop()
