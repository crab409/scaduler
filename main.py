import tkinter
import calendar
from datetime import datetime 


def fun(idx):
    sub_window = tkinter.Tk()
    sub_window.geometry("300x200")
    sub_window.title(f"{idx}")
    sub_window.mainloop()


def day_select(day) :
    global selected_day 
    selected_day = day 


def reset_calender(year, month) :
    start_week, last_day = calendar.monthrange(year, month)
    day = -start_week

    days = []
    for i in range(1, 7, 1) :
        for j in range(1, 8, 1) :
            if not (day<=0 or day > last_day) :

                button = tkinter.Button(
                    window, 
                    text="%02d"%day, 
                    font=('Arial', 17),
                    width=6, height=2,
                    command=lambda idx=day: day_select(idx)
                )
                
                button.grid(row=i, column=j)
                days.append(button)
            day-=-1


now = datetime.now()
current_year = now.year()
current_month = now.month()

#나중에 이 부분에 년도, 달 변환 버튼 추가 하기

reset_calender(current_year, current_month)

selected_day = 0

window = tkinter.Tk()
window.geometry("850x700")

window.mainloop()