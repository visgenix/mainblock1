# import tkinter as tk
# from tkinter import ttk
# from tkinter import *
# import customtkinter as ctk
# from Capture_Image import takeImages
# from training import training
# import csv

# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")
# def add_name_to_csv(csv_file_path, new_name):
#     # Read data from the CSV file
#         with open(csv_file_path, 'r') as f:
#             reader = csv.reader(f)
#             data = list(reader)

#         # Append the new name to the data
#         data.append([new_name])

#         # Write the updated data back to the CSV file
#         with open(csv_file_path, 'w', newline='') as f:
#             writer = csv.writer(f)
#             writer.writerows(data)
# def on_button():
#     text=nameInstr.get()
#     add_name_to_csv('/home/srec/Desktop/FaceRPI/staff_name.csv',text)

# def show_train_window():
#     rootT = ctk.CTk()
#     rootT.geometry("480x320")
#     rootT.title('Training')
#     rootT.attributes('-fullscreen', True)

#     nm = StringVar(rootT)
#     rn = StringVar(rootT)
    
#     title = ctk.CTkLabel(rootT, text='Training Details', font=('Helvetica', 16, 'bold'))
#     title.place(x=170, y=20)
    
#     nameInstr = ctk.CTkLabel(rootT, text='Name :', font=('Helvetica', 14))
#     nameInstr.place(x=10, y=70)
#     name = ctk.CTkEntry(rootT, width=250, textvariable=nm, font=('Ubuntu', 16))
#     name.place(x=120, y=70)
    
#     rnoInstr = ctk.CTkLabel(rootT, text='ID :', font=('Helvetica', 14))
#     rnoInstr.place(x=10, y=120)
#     rno = ctk.CTkEntry(rootT, width=90, textvariable=rn, font=('Ubuntu', 16))
#     rno.place(x=120, y=120)
#     with open('/home/srec/Desktop/FaceRPI/Departments.txt', 'r') as f:
#         departments = f.read().split(',')
#     dept = ttk.Combobox(rootT, width=15, height=5, values=departments)
#     dept.current([0])
#     dept.place(x=250, y=120)

#     def call_image_capture():
#         takeImages('_'.join([nm.get(),  dept.get(), rn.get()]))
#         s1_name=nm
#         add_name_to_csv('/home/srec/Desktop/FaceRPI/staff_name.csv',s1_name)
#         training()

#     ######################ṭ
#     s1_name=name
#     add_name_to_csv('/home/srec/Desktop/FaceRPI/staff_name.csv',text)
#     ######################
    
#     trainBtn1 = ctk.CTkButton(rootT, text='Train', font=('Ubuntu', 14), width=200, height=40, command=call_image_capture)
#     trainBtn1.place(x=145, y=180)

    
#     def back_to_menu():
#         rootT.destroy()

#     cancelBtn = ctk.CTkButton(rootT, text='Cancel', font=('Ubuntu', 14), fg_color='#EB455F', width=200, height=35, command=back_to_menu)
#     cancelBtn.place(x=145, y=240)

#     rootT.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import *
import customtkinter as ctk
from Capture_Image import takeImages
from training import training

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def show_train_window():
    rootT = ctk.CTk()
    rootT.geometry("480x320")
    rootT.title('Training')
    rootT.attributes('-fullscreen', True)

    nm = StringVar(rootT)
    rn = StringVar(rootT)
    
    title = ctk.CTkLabel(rootT, text='Training Details', font=('Helvetica', 16, 'bold'))
    title.place(x=170, y=20)
    
    nameInstr = ctk.CTkLabel(rootT, text='Name :', font=('Helvetica', 14))
    nameInstr.place(x=10, y=70)
    name = ctk.CTkEntry(rootT, width=250, textvariable=nm, font=('Ubuntu', 16))
    name.place(x=120, y=70)
    
    rnoInstr = ctk.CTkLabel(rootT, text='ID :', font=('Helvetica', 14))
    rnoInstr.place(x=10, y=120)
    rno = ctk.CTkEntry(rootT, width=90, textvariable=rn, font=('Ubuntu', 16))
    rno.place(x=120, y=120)
    with open('/home/srec/Desktop/FaceRPI/Departments.txt', 'r') as f:
        departments = f.read().split(',')
    dept = ttk.Combobox(rootT, width=15, height=5, values=departments)
    dept.current([0])
    dept.place(x=250, y=120)

    def call_image_capture():
        takeImages('_'.join([nm.get(),  dept.get(), rn.get()]))
        training()

    trainBtn1 = ctk.CTkButton(rootT, text='Train', font=('Ubuntu', 14), width=200, height=40, command=call_image_capture)
    trainBtn1.place(x=145, y=180)

    def back_to_menu():
        rootT.destroy()

    cancelBtn = ctk.CTkButton(rootT, text='Cancel', font=('Ubuntu', 14), fg_color='#EB455F', width=200, height=35, command=back_to_menu)
    cancelBtn.place(x=145, y=240)

    rootT.mainloop()








