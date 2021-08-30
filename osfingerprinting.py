
import nmap
 

import tkinter
from tkinter import messagebox
import json
window = tkinter.Tk()
window.geometry("500x324")
window.resizable(0, 0)
window.title("OSFingerPrinting")
bg = tkinter.PhotoImage(file="ha.png")
ipadd1=tkinter.StringVar()
ipadd2=tkinter.StringVar()
ipadd3=tkinter.StringVar()
ipadd4=tkinter.StringVar()
header_frame = tkinter.Frame(window,width=500,height=24)

header_frame.pack()
upper_frame = tkinter.Frame(window, width =500, height =150)
upper_frame.pack()
Lower_frame = tkinter.Frame(window, width = 500, height = 150)
Lower_frame.pack()
def Detect_OS():
    ip = ipadd1.get() + "." + ipadd2.get() + "." + ipadd3.get() + "." + ipadd4.get()
    if (ipadd1.get() == ""):
        messagebox.showinfo("Alert Message", "First Field Is Empty")
        # tkinter.Label(Lower_frame,text="First Field Is Empty").grid(row=4,column=4)
        return(ipadd1.set(""))
    if (ipadd2.get() == ""):
        messagebox.showinfo("Alert Message", "Second Field Is Empty")
        tkinter.Label(Lower_frame,text="Second Field Is Empty").grid(row=4,column=4)
        return
    if (ipadd3.get() == ""):
        messagebox.showinfo("Alert Message", "Third Field Is Empty")
        tkinter.Label(Lower_frame,text="Third Field Is Empty").grid(row=4,column=4)
        return
    if (ipadd4.get() == ""):
        messagebox.showinfo("Alert Message", "Fourth Field Is Empty")
        tkinter.Label(Lower_frame,text="Fourth field Is empty").grid(row=4,column=4)
        return 
    # if (ipadd1.get() == "" & ipadd2.get() == "" & ipadd3.get()=="" & ipadd4.get()==""):
    #     tkinter.Label(window,text="first field is empty").grid(row=4,column=4)
    #     return
    
    print(ip)
    scanner = nmap.PortScanner()
    result = scanner.scan(ip, arguments="-O")['scan'][ip]['osmatch'][0]
    json_result = json.dumps(result, separators=(',', ':'))
    json_result1 = json.loads(json_result)
    x= json_result1["name"]
    tkinter.Label(Lower_frame, text=x).grid(row=7,column=4)
    # ipadd1.set("")
    # ipadd2.set("")
    # ipadd3.set("")
    # ipadd4.set("")
tkinter.Label(header_frame,text = "",height = 1).grid(row = 1,column = 3)
tkinter.Label(header_frame,text = "",width = 6).grid(row = 2,column = 1)
tkinter.Label(header_frame,text = "This is a program developed to detect OS",height = 2,font = ('helvetica',8, 'bold')).grid(row = 2,column = 2)
tkinter.Label(upper_frame,text = "",height = 1).grid(row = 3,column = 1)
tkinter.Label(upper_frame,text = "",width = 2 ).grid(row = 4,column = 1)
tkinter.Label(upper_frame,text = "                       Enter Ip Address").grid(row = 4,column = 1)
tkinter.Entry(upper_frame,textvariable = ipadd1,width=3).grid(row=4,column=2)
tkinter.Label(upper_frame, text = '.').grid(row=4,column=3)
tkinter.Entry(upper_frame,textvariable = ipadd2,width=3).grid(row=4,column=4)
tkinter.Label(upper_frame, text = '.').grid(row=4,column=5)
tkinter.Entry(upper_frame,textvariable = ipadd3,width=3).grid(row=4,column=6)
tkinter.Label(upper_frame, text = '.').grid(row=4,column=7)
tkinter.Entry(upper_frame,textvariable = ipadd4,width=3).grid(row=4,column=8)
tkinter.Label(upper_frame,text = "",height = 1).grid(row = 5,column = 1)
tkinter.Button(upper_frame, text = "Detect OS", command = Detect_OS).grid(row=6,column=4)

window.mainloop()

