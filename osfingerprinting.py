
from tkinter.constants import ANCHOR, BOTH, END, LEFT, RIGHT, TOP, VERTICAL, X, Y
from tkinter import StringVar, messagebox,ttk
import nmap
from PIL import Image, ImageTk

import tkinter

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
lt1=StringVar()
print(lt1)
lt2 = tkinter.StringVar()
lt3 = tkinter.StringVar()
lt4 = tkinter.StringVar()
lt6 = tkinter.StringVar()
lt5 = tkinter.StringVar()
lt7 = tkinter.StringVar()
lt1.set("")
lt2.set("")
lt3.set("")
lt4.set("")
lt5.set("")
lt6.set("")
lt7.set("")
print(lt1)

class OS_Detection:
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
            # tkinter.Label(Lower_frame,text="Fourth field Is empty").grid(row=4,column=4)
            return 
        # if (ipadd1.get() == "" & ipadd2.get() == "" & ipadd3.get()=="" & ipadd4.get()==""):
        #     tkinter.Label(window,text="first field is empty").grid(row=4,column=4)
        #     return
        
        print(ip)
        scanner = nmap.PortScanner()
        result = scanner.scan(ip, arguments="-O")['scan'][ip]['osmatch'][0]
        if(len(result)==0):
            tkinter.Label(Frame_In_Canvas2, text="OS COULDN'T BE FOUND",font = ('helvetica',13,'bold')).grid(row=1)
        else:
            json_result = json.dumps(result, separators=(',', ':'))
            json_result1 = json.loads(json_result)
            json_result2 = json.dumps(json_result1["osclass"])
            json_result3 = json.loads(json_result2)
            print()
            print(json_result2)
            print(type(json_result2))
            print(type(json_result))
            print(type(json_result1))
            x0= json_result1["name"]
            x1= json_result3[0]["type"]
            x2= json_result3[0]["vendor"]
            x3= json_result3[0]["osfamily"]
            x4= json_result3[0]["osgen"]
            x5= json_result3[0]["accuracy"]
            x6= json_result3[0]["cpe"]
            lt1.set("Name Of OS: "+ x0)
            lt2.set("Type Of OS:  "+x1)
            lt3.set("Vendor Of OS:  "+x2)
            lt4.set("OSfamily Of OS:  "+x3)
            lt5.set("OSgen Of OS:  "+x4)
            lt6.set("Accuraccy Of Detection:  "+x5)
            lt7.set(("CPE Of OS:  ",x6))
            
    def reset():
        ipadd1.set("")
        ipadd2.set("")
        ipadd3.set("")
        ipadd4.set("")
        lt1.set("")
        lt2.set("")
        lt3.set("")
        lt4.set("")
        lt5.set("")
        lt6.set("")
        lt7.set("")
            
















canvas = tkinter.Canvas(window, width=500, height=170)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("ha.png").resize((500, 170), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tkinter.NW, image=img)


canvas.create_text(250, 35 , text ="This is a program developed to detect Remote OS",font = ('helvetica',15, 'bold'),fill='white')
canvas.create_text(130, 95 , text ="Enter IP Address:",font = ('helvetica',10, 'bold'),fill='white')
Entry1=tkinter.Entry(window,textvariable = ipadd1,width=3)
canvas.create_text(215, 95 , text =".",font = ('helvetica',15, 'bold'),fill='white')
Entry2=tkinter.Entry(window,textvariable = ipadd2,width=3)
canvas.create_text(245, 95 , text =".",font = ('helvetica',15, 'bold'),fill='white')
Entry3=tkinter.Entry(window,textvariable = ipadd3,width=3)
canvas.create_text(275, 95 , text =".",font = ('helvetica',15, 'bold'),fill='white')
Entry4=tkinter.Entry(window,textvariable = ipadd4,width=3)
Button1=tkinter.Button(window, text = "Detect OS", command = OS_Detection.Detect_OS)
Button2=tkinter.Button(window, text= "Reset", command = OS_Detection.reset)

Entry1_window = canvas.create_window(190,85, anchor="nw", window=Entry1)
Entry2_window = canvas.create_window(220,85, anchor="nw", window=Entry2)
Entry3_window = canvas.create_window(250,85, anchor="nw", window=Entry3)
Entry4_window = canvas.create_window(280,85, anchor="nw", window=Entry4)
Button1_window = canvas.create_window(210,125,anchor="nw",window=Button1)
Button2_window = canvas.create_window(455,140,anchor="nw",window=Button2)



Lower_frame = tkinter.Frame(window)
Lower_frame.pack(fill= X)
# canvas.create_window(500,200,anchor="nw",window=Lower_frame)

canvas2= tkinter.Canvas(Lower_frame)
canvas2.pack(side=LEFT, fill=BOTH)

Scrollbar = ttk.Scrollbar(Lower_frame, orient=VERTICAL, command= canvas2.yview)
Scrollbar.pack(side= RIGHT, fill = Y)

canvas2.configure(yscrollcommand=Scrollbar.set)
canvas2.bind('<Configure>', lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))

Frame_In_Canvas2 = tkinter.Frame(canvas2)
canvas2.create_window((0,0),window=Frame_In_Canvas2, anchor="nw") 


l1=tkinter.Label(Frame_In_Canvas2, textvariable=lt1,font = ('helvetica',9,'bold')).grid(row=1,sticky='nw')

l2=tkinter.Label(Frame_In_Canvas2, textvariable=lt2,font = ('helvetica',9,'bold')).grid(row=5,sticky='nw')
l3=tkinter.Label(Frame_In_Canvas2, textvariable=lt3,font = ('helvetica',9,'bold')).grid(row=2,sticky='nw')
l4=tkinter.Label(Frame_In_Canvas2, textvariable=lt4,font = ('helvetica',9,'bold')).grid(row=3,sticky='nw')
l5=tkinter.Label(Frame_In_Canvas2, textvariable=lt5,font = ('helvetica',9,'bold')).grid(row=4,sticky='nw')
l6=tkinter.Label(Frame_In_Canvas2, textvariable=lt6,font = ('helvetica',9,'bold')).grid(row=6,sticky='nw')
l7=tkinter.Label(Frame_In_Canvas2, textvariable=lt7,font = ('helvetica',9,'bold')).grid(row=7,sticky='nw')










# header_frame = tkinter.Frame(window,width=500,height=24)
# header_frame.pack()
# upper_frame = tkinter.Frame(window, width =500, height =150)
# upper_frame.pack()

# def Detect_OS():
#     ip = ipadd1.get() + "." + ipadd2.get() + "." + ipadd3.get() + "." + ipadd4.get()
#     if (ipadd1.get() == ""):
#         messagebox.showinfo("Alert Message", "First Field Is Empty")
#         # tkinter.Label(Lower_frame,text="First Field Is Empty").grid(row=4,column=4)
#         return(ipadd1.set(""))
#     if (ipadd2.get() == ""):
#         messagebox.showinfo("Alert Message", "Second Field Is Empty")
#         tkinter.Label(Lower_frame,text="Second Field Is Empty").grid(row=4,column=4)
#         return
#     if (ipadd3.get() == ""):
#         messagebox.showinfo("Alert Message", "Third Field Is Empty")
#         tkinter.Label(Lower_frame,text="Third Field Is Empty").grid(row=4,column=4)
#         return
#     if (ipadd4.get() == ""):
#         messagebox.showinfo("Alert Message", "Fourth Field Is Empty")
#         tkinter.Label(Lower_frame,text="Fourth field Is empty").grid(row=4,column=4)
#         return 
#     # if (ipadd1.get() == "" & ipadd2.get() == "" & ipadd3.get()=="" & ipadd4.get()==""):
#     #     tkinter.Label(window,text="first field is empty").grid(row=4,column=4)
#     #     return
    
#     print(ip)
#     scanner = nmap.PortScanner()
#     result = scanner.scan(ip, arguments="-O")['scan'][ip]['osmatch'][0]
#     json_result = json.dumps(result, separators=(',', ':'))
#     json_result1 = json.loads(json_result)
#     x= json_result1["name"]
#     tkinter.Label(Lower_frame, text=x).grid(row=7,column=4)
#     ipadd1.set("")
#     ipadd2.set("")
#     ipadd3.set("")
#     ipadd4.set("")
# tkinter.Label(canvas,text = "",height = 1).grid(row = 1,column = 3)
# tkinter.Label(canvas,text = "",width = 6).grid(row = 2,column = 1)
# tkinter.Label(canvas,text = "This is a program developed to detect OS",height = 2,font = ('helvetica',8, 'bold'),bg='grey').grid(row = 2,column = 2)
# tkinter.Label(canvas,text = "",height = 1).grid(row = 3,column = 1)
# tkinter.Label(canvas,text = "",width = 2 ).grid(row = 4,column = 1)
# tkinter.Label(canvas,text = "                       Enter Ip Address").grid(row = 4,column = 1)
# tkinter.Entry(canvas,textvariable = ipadd1,width=3).grid(row=4,column=2)
# tkinter.Label(canvas, text = '.').grid(row=4,column=3)
# tkinter.Entry(canvas,textvariable = ipadd2,width=3).grid(row=4,column=4)
# tkinter.Label(canvas, text = '.').grid(row=4,column=5)
# tkinter.Entry(canvas,textvariable = ipadd3,width=3).grid(row=4,column=6)
# tkinter.Label(canvas, text = '.').grid(row=4,column=7)
# tkinter.Entry(canvas,textvariable = ipadd4,width=3).grid(row=4,column=8)
# tkinter.Label(canvas,text = "",height = 1).grid(row = 5,column = 1)
# tkinter.Button(canvas, text = "Detect OS", command = Detect_OS).grid(row=6,column=4)

window.mainloop()

