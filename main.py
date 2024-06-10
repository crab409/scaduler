import tkinter
import calendar

def fun(idx):
    print(f"Button {idx} clicked")

window = tkinter.Tk()
window.geometry("700x500")

year, month = 2024, 6
start_week, last_day = calendar.monthrange(year, month)
day = -start_week

days = []
for i in range(1, 7, 1):
    for j in range(1, 8, 1):
        if day <= 0 or day > last_day:
            pass
#            button = tkinter.Button(window, text='00', font=('Arial', 17), width=6, height=2)
        else:
            button = tkinter.Button(window, text="%02d"%day, font=('Arial', 17),
                                    command=lambda idx=day: fun(idx),width=6, height=2)
            button.grid(row=i, column=j)
            days.append(button)
        day += 1
window.mainloop()
