import json
import tkinter
from tkinter import ttk,messagebox
import hashlib
import sys
import time
from 已完成.attack.build_ip_pool import available_ip_pool,build_ip_pool


def encrypt_something(something):
    header = 'header'
    middle_left = 'middle_left'
    middle_right = 'middle_right'
    end = 'end'
    encrypt_content = f'{header}{middle_left}{something}{middle_right}{end}'
    encrypt_result = hashlib.md5(encrypt_content.encode('utf-8')).hexdigest()
    return encrypt_result

def user_data_preparation():
    default_user_data = {
        'default_name' : 'default_password',
        'test_name' : 'test_password'
    }
    with open('user_data.json','wb') as f:
        f.write(json.dumps(default_user_data).encode('utf-8'))

# user_data_preparation()

def first_ui(source_ip_net):
    def main_content():
        print()
        your_account = your_account_here.get().strip()
        your_code = your_code_here.get().strip()
        try:
            encrypt_name = encrypt_something(your_account)
            encrypt_code = encrypt_something(your_code)

            ######versify######
            with open('user_data.json','r') as f:
                user_catalog_load = json.load(f)
                if user_catalog_load['{}'.format(encrypt_name)] == ['{}'.format(encrypt_code)]:
                    messagebox.showinfo('Correct Typing', 'welcome to this progress....')
                    ########attack_content########
                    build_ip_pool(source_ip_net)
                    main_root.destroy()
                    ########attack_content########
                else:
                    messagebox.showwarning('KeyError', 'wrong password or name?')


        except Exception:
            messagebox.showwarning('Fatal error',"Don't play tricks!!")
            sys.exit()
    def quit_progress():
        if messagebox.askyesno('Quit','Do you want to quit?'):
            main_root.destroy()


    main_root = tkinter.Tk()
    main_root.title('Enter_Progress...')
    main_root.geometry('400x200')

    tkinter.Label(main_root,text='name:').grid(row=0, column=1)
    your_account_here = tkinter.Entry(main_root)
    your_account_here.grid(row=0, column=2,columnspan=2)

    tkinter.Label(main_root,text='code:').grid(row=0, column=5)
    your_code_here = tkinter.Entry(main_root)
    your_code_here.grid(row=0, column=6,columnspan=2)

    log_button = ttk.Button(main_root,text='Login',command=main_content)
    log_button.grid(row=0,column=8,columnspan=2)

    quit_button = ttk.Button(main_root,text='Quit',command=quit_progress)
    quit_button.grid(row=0,column=10,columnspan=2)
    main_root.mainloop()


# first_ui(source_ip_net='aaaaaa')
