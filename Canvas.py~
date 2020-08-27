import tkinter as tk

from GUI import *


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

