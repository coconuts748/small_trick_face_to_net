import tkinter as tk
import sys
from tkinter import ttk,messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import time

from 已完成.attack.attack_content import attack_content


def second_ui():
    def inner_second_ui():
        print('aaaa')
        waiting_url__ = str(waiting_url.get().strip())
        waiting_speed__ = str(waiting_speed.get().strip())
        if messagebox.askyesno('Be attention','Are you sure?\n You must undergo any possible result\nNot me'):
            attack_content(final_url=waiting_url__,final_count=waiting_speed__)



    second_ui_root = tk.Tk()
    the_time = time.asctime(time.localtime(time.time()))
    second_ui_root.title("Attack page Now it's{}".format(the_time))
    second_ui_root.geometry('600x500')

    tk.Label(second_ui_root,text='input url below').grid(row=75,column=75,columnspan=2,sticky=tk.W)
    tk.Label(second_ui_root,text='input speed below').grid(row=525,column=75,columnspan=2,sticky=tk.W)


    waiting_url = tk.Entry(second_ui_root)
    waiting_url.grid(row=425,column=75,columnspan=2,sticky=tk.W)

    waiting_speed = tk.Entry(second_ui_root)
    waiting_speed.grid(row=425,column=525,columnspan=2,sticky=tk.W)

    image = Image.open('background.png')
    tk_image = ImageTk.PhotoImage(image)

    back_ground = ttk.Label(second_ui_root,image=tk_image)
    back_ground.grid(row=205,column=300)

    second_ui_button = tk.Button(second_ui_root,text='conflict!!',command=inner_second_ui)
    second_ui_button.grid(row=350,column=290,columnspan=20,rowspan=10)

    second_ui_root.mainloop()

# second_ui()