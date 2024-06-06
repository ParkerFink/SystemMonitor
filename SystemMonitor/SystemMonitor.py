import psutil
import tkinter
import threading
import time


#thread functions
def getCPU():
    while True:
        time.sleep(1)
        percent = psutil.cpu_percent()
        label_cpu.config(text=percent)
        
        
#threads
cpuThread = threading.Thread(target=getCPU)




#main window
window = tkinter.Tk()
window.geometry('800x500')
window.title("System Monitor")

global label_cpu

cpuThread.start()



label_cpu = tkinter.Label(text="CPU N/A")
label_cpu.pack()

label_cpu_temp = tkinter.Label(text="CPU Temp N/A")

label_ram = tkinter.Label(text="RAM N/A")
label_ram.pack()




window.mainloop()
