import tkinter as tk

####################################################

def Convert(event):
    order = order_txt.get()
    from_data = float(from_count.get())
    coeff = float(coeff_ent.get())
    if order == "True":
        to_data = str(round(from_data*coeff, 5))
    else:
        to_data = str(round(from_data/coeff, 5))
    to_count.delete(0, "end")
    to_count.insert(0, to_data)

def Order(event):
    order = order_txt.get()
    if order == "True":
        order_txt.delete(0, "end")
        order_txt.insert(0, "False")
        from_btn.configure(text = "RUR")
        to_btn.configure(text = "USD")
    else:
        order_txt.delete(0, "end")
        order_txt.insert(0, "True")
        from_btn.configure(text = "USD")
        to_btn.configure(text = "RUR")
    

####################################################



window = tk.Tk()
window.title("Конвертер валют")
window.resizable(0,0)
w=window.winfo_screenwidth()//2-350
h=window.winfo_screenheight()//2-200
window.geometry(f'700x400+{w}+{h}')

order_txt = tk.Entry(
    text="True",
    font="Courier 1",
    master=window
)
order_txt.place(x=220, y=30)
order_txt.insert(0, "True")

frame = tk.Frame(
    master=window,
    width=800,
    height=400,
    bg = "#dddddd"
)
frame.pack()

title = tk.Label(
    text="Конвертер валют",
    fg="#0e0e0e",
    bg="#dddddd",
    font="Courier 30",
    master=frame
)
title.place(x=176,y=30)

from_count = tk.Entry(
    master=frame,
    bg="#d7d7d7",
    font="Courier 37",
    width=13
)
from_count.place(x=220, y=110)
to_count = tk.Entry(
    master=frame,
    bg="#d7d7d7",
    font="Courier 37",
    width=13
)
to_count.place(x=220, y=185)

from_btn = tk.Button(
    master=frame,
    bg = "#309561",
    width=6,
    height=1,
    text = "USD",
    fg="#a6ffd1",
    font="Courier 20"
)
from_btn.place(x=100, y=110)
from_btn.bind("<Button-1>", Order)

to_btn = tk.Button(
    master=frame,
    bg = "#309561",
    width=6,
    height=1,
    text = "RUR",
    fg="#a6ffd1",
    font="Courier 20"
)
to_btn.place(x=100, y=185)
to_btn.bind("<Button-1>", Order)

translate_btn = tk.Button(
    master=frame,
    bg = "#309561",
    width=17,
    height=1,
    text = "Конвертировать",
    fg="#a6ffd1",
    font="Courier 20"
)
translate_btn.place(x=220, y=270)
translate_btn.bind("<Button-1>", Convert)

info_lbl = tk.Label(
    text="1 USD =",
    fg="#0e0e0e",
    bg="#dddddd",
    font="Courier 13",
    master=frame
)
info_lbl.place(x=260, y=350)

coeff_ent = tk.Entry(
    fg="#0e0e0e",
    bg="#dddddd",
    font="Courier 13",
    width=10,
    master=frame
)
coeff_ent.place(x=340, y=350)
coeff_ent.insert(0, "91.87")

info_lbl_2 = tk.Label(
    text=" RUR",
    fg="#0e0e0e",
    bg="#dddddd",
    font="Courier 13",
    master=frame
)
info_lbl_2.place(x=420, y=350)

################################################3





window.mainloop()


