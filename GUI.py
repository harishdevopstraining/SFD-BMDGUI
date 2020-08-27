import tkinter as tk
from tkinter import messagebox, END


loads_temp = []
load_at_dist_temp = []


Shear_Force = []
Bending_Moment = []

def Add():
    loads_temp.append(float(E1.get()))
    load_at_dist_temp.append(float(E2.get()))
    x_dist = float(E2.get())
    if a1 >= 0 and a1 <= 7:
        x_dist = (float(E2.get()) * 100) + 50
    elif a1 > 7 and a1 <= 14:
        x_dist = (float(E2.get()) * 50) + 50
    elif a1 > 14 and a1 <= 23:
        x_dist = (float(E2.get()) * 30) + 50
    elif a1 > 23 and a1 <= 35:
        x_dist = (float(E2.get()) * 20) + 50
    elif a1 > 35 and a1 <= 70:
        x_dist = (float(E2.get()) * 10) + 50
    elif a1 > 70 and a1 <= 140:
        x_dist = (float(E2.get()) * 5) + 50
    elif a1 > 140 and a1 <= 350:
        x_dist = (float(E2.get()) * 2) + 50
    else:
        x_dist = (float(E2.get()) * 1) + 50
    Ref_line = canvas.create_line(x_dist, 160, x_dist, 650, width=2, fill="grey70", dash = (5,1))
    load_line = canvas.create_line(x_dist,20,x_dist,100, width=5,arrow = "last")
    define_load = canvas.create_text(x_dist+20, 40, text=float(E1.get()), font=30)
    if float(E2.get()) != 0:
        if float(E2.get()) != a1:
            define_dimen = canvas.create_text(x_dist - 20, 140, text=float(E2.get()), font=30)
            ext_line = canvas.create_line(x_dist + 5, 150 - 5, x_dist - 5, 150 + 5, width=1)
    E1.delete(0, END)
    E2.delete(0, END)


def Beam_OK():
    window1 = tk.Toplevel()
    window1.geometry("1000x690+100+0")
    window1.configure(bg="grey60")
    global canvas, a1
    canvas = tk.Canvas(window1, width=950, height=670, bg="White")
    canvas.pack()
    a1 = float(Beam_Length.get())
    if a1 >=0 and a1 <=7:
        Beam = canvas.create_line(50, 100, (a1*100) + 50, 100, width=5)
        dimen = canvas.create_line(50, 150, (a1*100) + 50, 150, width=1)
        ext_Start = canvas.create_line(55, 150 - 5, 45, 150 + 5, width=1)
        ext_end = canvas.create_line((a1*100) + 55, 150 - 5, (a1*100) + 45, 150 + 5, width=1)
        def_len = canvas.create_text((a1*100) + 30, 140, text=a1, font=30)
        Ref_line_start = canvas.create_line(50, 160, 50, 650, width=2, fill="grey70", dash = (5,1))
        Ref_line_end = canvas.create_line((a1*100) + 50, 160, (a1*100) + 50, 650, width=2, fill="grey70", dash = (5,1))
    elif a1 >7 and a1 <=14:
        Beam = canvas.create_line(50, 100, (a1*50) + 50, 100, width=5)
        dimen = canvas.create_line(50, 150, (a1*50) + 50, 150, width=1)
        ext_Start = canvas.create_line(55, 150 - 5, 45, 150 + 5, width=1)
        ext_end = canvas.create_line((a1 * 50) + 55, 150 - 5, (a1 * 50) + 45, 150 + 5, width=1)
        def_len = canvas.create_text((a1 * 50) + 30, 140, text=a1, font=30)
        Ref_line_start = canvas.create_line(50, 160, 50, 650, width=2, fill="grey70", dash = (5,1))
        Ref_line_end = canvas.create_line((a1 * 50) + 50, 160, (a1 * 50) + 50, 650, width=2, fill="grey70", dash = (5,1))
    elif a1 >14 and a1 <=23:
        Beam = canvas.create_line(50, 100, (a1*30) + 50, 100, width=5)
        dimen = canvas.create_line(50, 150, (a1*30) + 50, 150, width=1)
        ext_Start = canvas.create_line(55, 150 - 5, 45, 150 + 5, width=1)
        ext_end = canvas.create_line((a1 * 30) + 55, 150 - 5, (a1 * 30) + 45, 150 + 5, width=1)
        def_len = canvas.create_text((a1 * 30) + 30, 140, text=a1, font=30)
        Ref_line_start = canvas.create_line(50, 160, 50, 650, width=2, fill="grey70", dash = (5,1))
        Ref_line_end = canvas.create_line((a1 * 30) + 50, 160, (a1 * 30) + 50, 650, width=2, fill="grey70", dash = (5,1))
    elif a1 >23 and a1 <=35:
        Beam = canvas.create_line(50, 100, (a1*20) + 50, 100, width=5)
        dimen = canvas.create_line(50, 150, (a1*20) + 50, 150, width=1)
        ext_Start = canvas.create_line(55, 150 - 5, 45, 150 + 5, width=1)
        ext_end = canvas.create_line((a1 * 20) + 55, 150 - 5, (a1 * 20) + 45, 150 + 5, width=1)
        def_len = canvas.create_text((a1 * 20) + 30, 140, text=a1, font=30)
        Ref_line_start = canvas.create_line(50, 160, 50, 650, width=2, fill="grey70", dash = (5,1))
        Ref_line_end = canvas.create_line((a1 * 20) + 50, 160, (a1 * 20) + 50, 650, width=2, fill="grey70", dash = (5,1))
    elif a1 >35 and a1 <=70:
        Beam = canvas.create_line(50, 100, (a1*10) + 50, 100, width=5)
        dimen = canvas.create_line(50, 150, (a1*10) + 50, 150, width=1)
        ext_Start = canvas.create_line(55, 150 - 5, 45, 150 + 5, width=1)
        ext_end = canvas.create_line((a1 * 10) + 55, 150 - 5, (a1 * 10) + 45, 150 + 5, width=1)
        def_len = canvas.create_text((a1 * 10) + 30, 140, text=a1, font=30)
        Ref_line_start = canvas.create_line(50, 160, 50, 650, width=2, fill="grey70", dash = (5,1))
        Ref_line_end = canvas.create_line((a1 * 10) + 50, 160, (a1 * 10) + 50, 650, width=2, fill="grey70", dash = (5,1))
    elif a1 >70 and a1 <=140:
        Beam = canvas.create_line(50, 100, (a1*5) + 50, 100, width=5)
        dimen = canvas.create_line(50, 150, (a1*5) + 50, 150, width=1)
        ext_Start = canvas.create_line(55, 150 - 5, 45, 150 + 5, width=1)
        ext_end = canvas.create_line((a1 * 5) + 55, 150 - 5, (a1 * 5) + 45, 150 + 5, width=1)
        def_len = canvas.create_text((a1 * 5) + 30, 140, text=a1, font=30)
        Ref_line_start = canvas.create_line(50, 160, 50, 650, width=2, fill="grey70", dash = (5,1))
        Ref_line_end = canvas.create_line((a1 * 5) + 50, 160, (a1 * 5) + 50, 650, width=2, fill="grey70", dash = (5,1))
    elif a1 >140 and a1 <=350:
        Beam = canvas.create_line(50, 100, (a1*2) + 50, 100, width=5)
        dimen = canvas.create_line(50, 150, (a1*2) + 50, 150, width=1)
        ext_Start = canvas.create_line(55, 150 - 5, 45, 150 + 5, width=1)
        ext_end = canvas.create_line((a1 * 2) + 55, 150 - 5, (a1 * 2) + 45, 150 + 5, width=1)
        def_len = canvas.create_text((a1 * 2) + 30, 140, text=a1, font=30)
        Ref_line_start = canvas.create_line(50, 160, 50, 650, width=2, fill="grey70", dash = (5,1))
        Ref_line_end = canvas.create_line((a1 * 2) + 50, 160, (a1 * 2) + 50, 650, width=2, fill="grey70", dash = (5,1))
    else:
        Beam = canvas.create_line(50, 100, a1+50, 100, width=5)
        dimen = canvas.create_line(50, 150, a1+50, 150, width=1)
        ext_Start = canvas.create_line(55, 150 - 5, 45, 150 + 5, width=1)
        ext_end = canvas.create_line((a1 * 1) + 55, 150 - 5, (a1 * 1) + 45, 150 + 5, width=1)
        def_len = canvas.create_text((a1 * 1) + 30, 140, text=a1, font=30)
        Ref_line_start = canvas.create_line(50, 160, 50, 650, width=2, fill="grey70")
        Ref_line_end = canvas.create_line((a1 * 1) + 50, 160, (a1 * 1) + 50, 650, width=2, fill="grey70", dash = (5,1))


def Support_OK():
    if cant.get() == 1 and ssb.get() == 0:
        support = canvas.create_line(50, 70, 50, 130, width=3)
        for i in range(70, 130, 10):
            hatch = canvas.create_line(50, i, 40, i + 10, width=1)
    elif ssb.get() == 1 and cant.get() == 0:
        support1 = canvas.create_line(50, 100, 30, 130,70,130,50,100, width=3)
        support2 = canvas.create_line((a1 * 100) + 50, 100, (a1 * 100) + 30, 130, (a1 * 100) + 70, 130, (a1 * 100) + 50, 100, width=3)
        for i in range(30, 80, 10):
            hatch = canvas.create_line(i,130, i-10, 140, width=1)
        for i in range(int(a1 * 100)+30, int(a1 * 100)+80, 10):
            hatch = canvas.create_line(i,130, i-10, 140, width=1)
    elif ssb.get() == 1 and cant.get() == 1:
        messagebox.showerror("Error", "Type of beam not selected correctly")


def Beam():
    global L1, Beam_Length, b1, L2, Load_Unit
    try:
        # support widgets  C1,c2,b2
        b2.place_forget()
        c1.place_forget()
        c2.place_forget()
        # Load widgets  C1,c2,b3
        l1.place_forget()
        l2.place_forget()
        E1.place_forget()
        E2.place_forget()
        b3.place_forget()
        L1 = tk.Label(window, text="Length of Beam (in m)", font=10)
        L1.place(x=10, y=40)
        Beam_Length = tk.Entry(window, width=20, font=12)
        Beam_Length.place(x=220, y=40)
        L2 = tk.Label(window, text="Units of load", font=10)
        L2.place(x=10, y=70)
        Load_Unit = tk.Entry(window, width=20, font=12)
        Load_Unit.place(x=220, y=70)
        b1 = tk.Button(window, text="OK", width=10, font=12, command = Beam_OK)
        b1.place(x=300, y=120)
    except:
        L1 =  tk.Label(window, text ="Length of Beam (in m)", font=10)
        L1.place(x=10, y=40)
        Beam_Length = tk.Entry(window, width=20, font = 12)
        Beam_Length.place(x=220, y=40)
        L2 = tk.Label(window, text="Units of load", font=10)
        L2.place(x=10, y=70)
        Load_Unit = tk.Entry(window, width=20, font=12)
        Load_Unit.place(x=220, y=70)
        b1 = tk.Button(window, text="OK", width=10, font=12,command = Beam_OK)
        b1.place(x=300, y=120)


def Support():
    global c1, c2, b2
    try:
        # Beam widgets  L1,Beam_Length, b1
        L1.place_forget()
        Beam_Length.place_forget()
        L2.place_forget()
        Load_Unit.place_forget()
        b1.place_forget()
        # Load widgets  C1,c2,b3
        l1.place_forget()
        l2.place_forget()
        E1.place_forget()
        E2.place_forget()
        b3.place_forget()
        global cant, ssb
        cant = tk.IntVar()
        c1 = tk.Checkbutton(window, text="Cantilever Beam", font=10, variable=cant)
        c1.place(x=20, y=40)
        ssb = tk.IntVar()
        c2 = tk.Checkbutton(window, text="Simply Supported Beam", font=10, variable=ssb)
        c2.place(x=20, y=75)
        b2 = tk.Button(window, text="OK", width=10, font=12, command=Support_OK)
        b2.place(x=300, y=150)
    except:
        cant = tk.IntVar()
        c1 = tk.Checkbutton(window, text="Cantilever Beam", font=10, variable=cant)
        c1.place(x=20, y=40)
        ssb = tk.IntVar()
        c2 = tk.Checkbutton(window, text="Simply Supported Beam", font=10, variable=ssb)
        c2.place(x=20, y=75)
        b2 = tk.Button(window, text="OK", width=10, font=12, command=Support_OK)
        b2.place(x=300, y=150)


def Load():
    global E1, E2, b3, l1, l2
    try:
        # Beam widgets  L1,Beam_Length, b1
        b1.place_forget()
        L1.place_forget()
        Beam_Length.place_forget()
        L2.place_forget()
        Load_Unit.place_forget()
        # support widgets  C1,c2,b2
        b2.place_forget()
        c1.place_forget()
        c2.place_forget()
        l1 = tk.Label(window,text = "Load", font=10)
        l1.place(x=20, y=40)
        E1 = tk.Entry(window, width=20, font = 12)
        E1.place(x=100, y=40)
        l2 = tk.Label(window, text="Distance", font=10)
        l2.place(x=20, y=75)
        E2 = tk.Entry(window, width=20, font=12)
        E2.place(x=100, y=75)
        b3 =tk.Button(window, text = "Add", width=10, font = 12, command = Add)
        b3.place(x=120, y=120)
    except:
        l1 = tk.Label(window, text="Load", font=10)
        l1.place(x=20, y=40)
        E1 = tk.Entry(window, width=20, font=12)
        E1.place(x=100, y=40)
        l2 = tk.Label(window, text="Distance", font=10)
        l2.place(x=20, y=75)
        E2 = tk.Entry(window, width=20, font=12)
        E2.place(x=100, y=75)
        b3 = tk.Button(window, text="Add", width=10, font=12, command=Add)
        b3.place(x=120, y=120)


def Calculate():
    if cant.get() == 1:
        T1 = tk.Label(window, text="SF and BM Calculation Starting from Right End of the Beam", font=8)
        T1.place(x=10, y=250)
        y = 300
        list1 = loads_temp
        list2 = load_at_dist_temp
        temp_zip = zip(list2, list1)
        s = sorted(temp_zip, reverse=True)
        temp_unzip = zip(*s)
        global load_at_dist, loads
        load_at_dist, loads = map(list, temp_unzip)
        loads.append(0.0)
        load_at_dist.append(0.0)
        # print(loads)
        # print(load_at_dist)
        no_of_loads = len(loads)
        for i in range(1, no_of_loads + 1):
            s1 = str(i)
            s = "Shear Force" + "  " + s1
            B = "Bending Moment" + "  " + s1
            sf_label = tk.Label(window, text=s, font=10)
            sf_label.place(x=10, y=y)
            BM_label = tk.Label(window, text=B, font=10)
            BM_label.place(x=220, y=y)
            y +=30
        shearforce = 0
        y = 300
        for load in loads:
            shearforce  += load
            Sf1 = tk.Label(window, text=round(shearforce,2), font=10)
            Sf1.place(x=150, y=y)
            y += 30
            Shear_Force.append(round(shearforce,2))
        y = 300
        for i in range(no_of_loads):
            r = 0
            for j in range(0, i + 1):
                c = abs(load_at_dist[i] - load_at_dist[j])
                r += (loads[j]) * c
            bm1 = tk.Label(window, text=round(-r,2), font=10)
            bm1.place(x=400, y=y)
            y +=30
            Bending_Moment.append(round(-r,2))
    elif ssb.get() == 1:
        T1 = tk.Label(window, text="SF and BM Calculation Starting from Right End of the Beam", font=8)
        T1.place(x=10, y=250)
        R = 0
        for i in range(0, len(loads_temp)):
            R += loads_temp[i]*load_at_dist_temp[i]
        R_b = R/a1
        L_Sum = sum(loads_temp)
        R_a = L_Sum-R_b
        # print(R_a)
        # print(R_b)
        y = 300
        list1 = [ -x for x in loads_temp]
        list2 = load_at_dist_temp
        temp_zip = zip(list2, list1)
        s = sorted(temp_zip, reverse=True)
        temp_unzip = zip(*s)
        #global loads, load_at_dist
        load_at_dist, loads = map(list, temp_unzip)
        loads.insert(0,R_b)
        load_at_dist.insert(0,a1)
        loads.append(R_a)
        load_at_dist.append(0.0)
        # print(loads)
        # print(load_at_dist)
        no_of_loads = len(loads)
        for i in range(1, no_of_loads+1):
            s1 = str(i)
            s = "Shear Force" + "  " + s1
            B = "Bending Moment" + "  " + s1
            sf_label = tk.Label(window, text=s, font=10)
            sf_label.place(x=10, y=y)
            BM_label = tk.Label(window, text=B, font=10)
            BM_label.place(x=220, y=y)
            y += 30
        shearforce = 0
        y = 300
        for load in loads:
            shearforce += load
            if shearforce !=0:
                Sf1 = tk.Label(window, text=round(-shearforce,2), font=10)
                Sf1.place(x=150, y=y)
                Shear_Force.append(round(-shearforce,2))
            else:
                Sf1 = tk.Label(window, text=round(shearforce,2), font=10)
                Sf1.place(x=150, y=y)
                Shear_Force.append(round(shearforce,2))
            y += 30

        y = 300
        for i in range(no_of_loads):
            r = 0
            for j in range(0, i + 1):
                c = abs(load_at_dist[i] - load_at_dist[j])
                r += (loads[j]) * c
            bm1 = tk.Label(window, text=round(r,2), font=10)
            bm1.place(x=400, y=y)
            y += 30
            Bending_Moment.append(round(r,2))



def Draw():
    if cant.get() == 1:
        Shear_Force.reverse()
        Bending_Moment.reverse()
        load_at_dist.reverse()
        h = (max(Shear_Force))+400
        if a1 >= 0 and a1 <= 7:
            Sf_base = canvas.create_line(50, h, (a1 * 100) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 50, (a1 * 100) + 50, h + 50, width=2)
        elif a1 > 7 and a1 <= 14:
            Sf_base = canvas.create_line(50, h, (a1 * 50) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 50, (a1 * 50) + 50, h + 50, width=2)
        elif a1 > 14 and a1 <= 23:
            Sf_base = canvas.create_line(50, h, (a1 * 30) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 50, (a1 * 30) + 50, h + 50, width=2)
        elif a1 > 23 and a1 <= 35:
            Sf_base = canvas.create_line(50, h, (a1 * 20) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 50, (a1 * 20) + 50, h + 50, width=2)
        elif a1 > 35 and a1 <= 70:
            Sf_base = canvas.create_line(50, h, (a1 * 10) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 50, (a1 * 10) + 50, h + 50, width=2)
        elif a1 > 70 and a1 <= 140:
            Sf_base = canvas.create_line(50, h, (a1 * 5) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 50, (a1 * 5) + 50, h + 50, width=2)
        elif a1 > 140 and a1 <= 350:
            Sf_base = canvas.create_line(50, h, (a1 * 2) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 50, (a1 * 2) + 50, h + 50, width=2)
        else:
            Sf_base = canvas.create_line(50, h, a1 + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 50, a1 + 50, h + 50, width=2)
        x1 = 50
        for ind, force in enumerate(Shear_Force):
            if a1 >= 0 and a1 <= 7:
                x = (load_at_dist[ind]*100) + 50
            elif a1 > 7 and a1 <= 14:
                x = (load_at_dist[ind]*50) + 50
            elif a1 > 14 and a1 <= 23:
                x = (load_at_dist[ind]*30) + 50
            elif a1 > 23 and a1 <= 35:
                x = (load_at_dist[ind]*20) + 50
            elif a1 > 35 and a1 <= 70:
                x = (load_at_dist[ind]*10) + 50
            elif a1 > 70 and a1 <= 140:
                x = (load_at_dist[ind]*5) + 50
            elif a1 > 140 and a1 <= 350:
                x = (load_at_dist[ind]*2) + 50
            else:
                x = (load_at_dist[ind]*1) + 50
            y = h-(float(force)*5)
            force_line = canvas.create_line(x,y, x, h, width=2, fill = "grey70")
            hor_line = canvas.create_line(x,y,x1,y,width=2)
            sf_load = canvas.create_text(x-20, h-20, text=force, font=30)
            x1 = x
        for ind, Bend in enumerate(Bending_Moment):
            x = load_at_dist[ind]
            y = (h+50)-(Bend/2)
            if a1 >= 0 and a1 <= 7:
                BM_line = canvas.create_line((x * 100) + 50, y, (x * 100) + 50, h + 50, width=2, fill="grey70")
                Moment = canvas.create_text((x * 100) + 20, h + 65, text=Bend, font=30)
            elif a1 > 7 and a1 <= 14:
                BM_line = canvas.create_line((x * 50) + 50, y, (x * 50) + 50, h + 50, width=2, fill="grey70")
                Moment = canvas.create_text((x * 50) + 30, h + 65, text=Bend, font=30)
            elif a1 > 14 and a1 <= 23:
                BM_line = canvas.create_line((x * 30) + 50, y, (x * 30) + 50, h + 50, width=2, fill="grey70")
                Moment = canvas.create_text((x * 30) + 30, h + 65, text=Bend, font=30)
            elif a1 > 23 and a1 <= 35:
                BM_line = canvas.create_line((x * 20) + 50, y, (x * 20) + 50, h + 50, width=2, fill="grey70")
                Moment = canvas.create_text((x * 20) + 30, h + 65, text=Bend, font=30)
            elif a1 > 35 and a1 <= 70:
                BM_line = canvas.create_line((x * 10) + 50, y, (x * 10) + 50, h + 50, width=2, fill="grey70")
                Moment = canvas.create_text((x * 10) + 30, h + 65, text=Bend, font=30)
            elif a1 > 70 and a1 <= 140:
                BM_line = canvas.create_line((x * 5) + 50, y, (x * 5) + 50, h + 50, width=2, fill="grey70")
                Moment = canvas.create_text((x * 5) + 30, h + 65, text=Bend, font=30)
            elif a1 > 140 and a1 <= 350:
                BM_line = canvas.create_line((x * 2) + 50, y, (x * 2) + 50, h + 50, width=2, fill="grey70")
                Moment = canvas.create_text((x * 2) + 30, h + 65, text=Bend, font=30)
            else:
                BM_line = canvas.create_line(x + 50, y, x + 50, h + 50, width=2, fill="grey70")
                Moment = canvas.create_text(x + 30, h + 65, text=Bend, font=30)
            x1 = x
            if ind < len(Bending_Moment)-1:
                t = ind + 1
                temp = load_at_dist[t]
                y1 = (h+50) - (Bending_Moment[t]/2)
                if a1 >= 0 and a1 <= 7:
                    hor_line = canvas.create_line((x*100)+50, y, (temp*100)+50, y1, width=2)
                elif a1 > 7 and a1 <= 14:
                    hor_line = canvas.create_line((x*50)+50, y, (temp*50)+50, y1, width=2)
                elif a1 > 14 and a1 <= 23:
                    hor_line = canvas.create_line((x*30)+50, y, (temp*30)+50, y1, width=2)
                elif a1 > 23 and a1 <= 35:
                    hor_line = canvas.create_line((x*20)+50, y, (temp*20)+50, y1, width=2)
                elif a1 > 35 and a1 <= 70:
                    hor_line = canvas.create_line((x*10)+50, y, (temp*10)+50, y1, width=2)
                elif a1 > 70 and a1 <= 140:
                    hor_line = canvas.create_line((x*5)+50, y, (temp*5)+50, y1, width=2)
                elif a1 > 140 and a1 <= 350:
                    hor_line = canvas.create_line((x*2)+50, y, (temp*2)+50, y1, width=2)
                else:
                    hor_line = canvas.create_line(x+50, y, temp+50, y1, width=2)
    elif ssb.get() == 1:
        Shear_Force.reverse()
        Bending_Moment.reverse()
        load_at_dist.reverse()
        h = Shear_Force[0]+300
        if a1 >= 0 and a1 <= 7:
            Sf_base = canvas.create_line(50, h, (a1 * 100) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 300, (a1 * 100) + 50, h + 300, width=2)
        elif a1 > 7 and a1 <= 14:
            Sf_base = canvas.create_line(50, h, (a1 * 50) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 300, (a1 * 50) + 50, h + 300, width=2)
        elif a1 > 14 and a1 <= 23:
            Sf_base = canvas.create_line(50, h, (a1 * 30) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 300, (a1 * 30) + 50, h + 300, width=2)
        elif a1 > 23 and a1 <= 35:
            Sf_base = canvas.create_line(50, h, (a1 * 20) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 300, (a1 * 20) + 50, h + 300, width=2)
        elif a1 > 35 and a1 <= 70:
            Sf_base = canvas.create_line(50, h, (a1 * 10) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 300, (a1 * 10) + 50, h + 300, width=2)
        elif a1 > 70 and a1 <= 140:
            Sf_base = canvas.create_line(50, h, (a1 * 5) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 300, (a1 * 5) + 50, h + 300, width=2)
        elif a1 > 140 and a1 <= 350:
            Sf_base = canvas.create_line(50, h, (a1 * 2) + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 300, (a1 * 2) + 50, h + 300, width=2)
        else:
            Sf_base = canvas.create_line(50, h, a1 + 50, h, width=2)
            bm_base = canvas.create_line(50, h + 300, a1 + 50, h + 300, width=2)
        x1 = 50
        for ind, force in enumerate(Shear_Force):
            if a1 >= 0 and a1 <= 7:
                x = (load_at_dist[ind]*100) + 50
            elif a1 > 7 and a1 <= 14:
                x = (load_at_dist[ind]*50) + 50
            elif a1 > 14 and a1 <= 23:
                x = (load_at_dist[ind]*30) + 50
            elif a1 > 23 and a1 <= 35:
                x = (load_at_dist[ind]*20) + 50
            elif a1 > 35 and a1 <= 70:
                x = (load_at_dist[ind]*10) + 50
            elif a1 > 70 and a1 <= 140:
                x = (load_at_dist[ind]*5) + 50
            elif a1 > 140 and a1 <= 350:
                x = (load_at_dist[ind]*2) + 50
            else:
                x = (load_at_dist[ind]*1) + 50
            y = h-(float(force)*10)
            force_line = canvas.create_line(x,y, x, h, width=2, fill = "grey70")
            hor_line = canvas.create_line(x,y,x1,y,width=2)
            sf_load = canvas.create_text(x-20, y-10, text=force, font=30)
            x1 = x
        for ind, Bend in enumerate(Bending_Moment):
            x = load_at_dist[ind]
            y = (h+300)-(Bend*5)
            if a1 >= 0 and a1 <= 7:
                BM_line = canvas.create_line((x * 100) + 50, y, (x * 100) + 50, h + 300, width=2, fill="grey70")
                Moment = canvas.create_text((x * 100) + 20, y-20, text=Bend, font=30)
            elif a1 > 7 and a1 <= 14:
                BM_line = canvas.create_line((x * 50) + 50, y, (x * 50) + 50, h + 300, width=2, fill="grey70")
                Moment = canvas.create_text((x * 50) + 30, y-20, text=Bend, font=30)
            elif a1 > 14 and a1 <= 23:
                BM_line = canvas.create_line((x * 30) + 50, y, (x * 30) + 50, h + 300, width=2, fill="grey70")
                Moment = canvas.create_text((x * 30) + 30, y-20, text=Bend, font=30)
            elif a1 > 23 and a1 <= 35:
                BM_line = canvas.create_line((x * 20) + 50, y, (x * 20) + 50, h + 300, width=2, fill="grey70")
                Moment = canvas.create_text((x * 20) + 30, y-20, text=Bend, font=30)
            elif a1 > 35 and a1 <= 70:
                BM_line = canvas.create_line((x * 10) + 50, y, (x * 10) + 50, h + 300, width=2, fill="grey70")
                Moment = canvas.create_text((x * 10) + 30, y-20, text=Bend, font=30)
            elif a1 > 70 and a1 <= 140:
                BM_line = canvas.create_line((x * 5) + 50, y, (x * 5) + 50, h + 300, width=2, fill="grey70")
                Moment = canvas.create_text((x * 5) + 30, y-20, text=Bend, font=30)
            elif a1 > 140 and a1 <= 350:
                BM_line = canvas.create_line((x * 2) + 50, y, (x * 2) + 50, h + 300, width=2, fill="grey70")
                Moment = canvas.create_text((x * 2) + 30, y-20, text=Bend, font=30)
            else:
                BM_line = canvas.create_line(x + 50, y, x + 50, h + 300, width=2, fill="grey70")
                Moment = canvas.create_text(x + 30, y-20, text=Bend, font=30)
            x1 = x
            if ind < len(Bending_Moment)-1:
                t = ind + 1
                temp = load_at_dist[t]
                y1 = (h+300) - (Bending_Moment[t]*5)
                if a1 >= 0 and a1 <= 7:
                    hor_line = canvas.create_line((x*100)+50, y, (temp*100)+50, y1, width=2)
                elif a1 > 7 and a1 <= 14:
                    hor_line = canvas.create_line((x*50)+50, y, (temp*50)+50, y1, width=2)
                elif a1 > 14 and a1 <= 23:
                    hor_line = canvas.create_line((x*30)+50, y, (temp*30)+50, y1, width=2)
                elif a1 > 23 and a1 <= 35:
                    hor_line = canvas.create_line((x*20)+50, y, (temp*20)+50, y1, width=2)
                elif a1 > 35 and a1 <= 70:
                    hor_line = canvas.create_line((x*10)+50, y, (temp*10)+50, y1, width=2)
                elif a1 > 70 and a1 <= 140:
                    hor_line = canvas.create_line((x*5)+50, y, (temp*5)+50, y1, width=2)
                elif a1 > 140 and a1 <= 350:
                    hor_line = canvas.create_line((x*2)+50, y, (temp*2)+50, y1, width=2)
                else:
                    hor_line = canvas.create_line(x+50, y, temp+50, y1, width=2)

window = tk.Tk()
window.title("SFD and BMD for Point Loads")
window.geometry("500x600+100+0")
window.configure( bg = "grey60")
btn1 = tk.Button(window, text ="Beam", width=10, font = 12, command = Beam)
btn1.grid(row=1, column=1)
btn2 = tk.Button(window, text ="Support", width=10, font = 12, command = Support)
btn2.grid(row=1, column=2)
btn3= tk.Button(window, text ="Load", width=10, font = 12, command = Load)
btn3.grid(row=1, column=3)
Main_b1 = tk.Button(window, text ="Calculate", width=10, font = 12, command = Calculate)
Main_b1.place(x=50, y=550)
Main_b2 = tk.Button(window, text ="Draw", width=10, font = 12, command = Draw)
Main_b2.place(x=200, y=550)
Main_b3 = tk.Button(window, text ="Cancel", width=10, font = 12, command = window.quit)
Main_b3.place(x=350, y=550)


window.mainloop()