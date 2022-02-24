import tkinter as tk
import tkinter.font as font
from Motion_tracking import tracker
from record_video import record

window = tk.Tk()
window.title = "SMART CCTV"
window.geometry("750x800")
# label
label = tk.Label(window, text="Welcome")
label.grid(row=0, column=2)
label['font'] = font.Font(size=35, weight='bold', family='Helvetica')
# button font
btn_font = font.Font(size=15, weight='bold', family='Helvetica')
# --------------------------------------EXIT----------------------------------------------
button2 = tk.Button(window, text="EXIT", fg="red", height=3, width=20, command=window.quit)
button2['font'] = btn_font
button2.grid(row=3, pady=(25, 10), column=5)
# ---------------------------------MOTION_DETECTION---------------------------------------
button3 = tk.Button(window, text="MOTION DETECTION", fg="green", height=3, width=20, command=tracker)
button3['font'] = btn_font
button3.grid(row=1, pady=(25, 10), column=5)
# ----------------------------------RECORD------------------------------------------------
button4 = tk.Button(window, text="RECORD", fg="green", height=3, width=20, command=record)
button4['font'] = btn_font
button4.grid(row=2, pady=(25, 10), column=5)

# ------------------------------ThankYou For using----------------------------------------

label2 = tk.Label(window, text="Thanks for using")
label2.grid(row=4, column=5, columnspan=6)
label2['font'] = font.Font(size=20, weight='bold', family='Helvetica')
window.mainloop()
