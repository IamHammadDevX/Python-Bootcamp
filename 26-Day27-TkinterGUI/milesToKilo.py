from tkinter import *

def miles_to_kilo():
    miles = float(mile_entry.get())
    km = miles * 1.609
    kilo_meter_result_label.config(text=f"{km}")


window = Tk()
window.title("GUI | Miles to Killo converter")
window.minsize(width=150, height=150)
window.config(padx=20, pady=20)

mile_entry = Entry(width=8)
mile_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilo_meter_result_label = Label(text="0")
kilo_meter_result_label.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)


calc_btn = Button(text="Calculate", command=miles_to_kilo)
calc_btn.grid(column=1, row=2)












# Keep the window on screen
window.mainloop()