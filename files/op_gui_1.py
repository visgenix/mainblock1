import tkinter as tk
from tkinter import *
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
from train import show_train_window
import pickle
import regex as re
import csv

def show_pickle_window():
    rootT = ctk.CTk()
    rootT.geometry("480x320")
    rootT.title('Pickle operation')
    rootT.attributes('-fullscreen', True)

    nm = StringVar(rootT)
    rn = StringVar(rootT)
    
    title = ctk.CTkLabel(rootT, text='Pickle opertation Details', font=('Helvetica', 16, 'bold'))
    title.place(x=170, y=20)
    
    nameInstr = ctk.CTkLabel(rootT, text='Name :', font=('Helvetica', 14))
    nameInstr.place(x=10, y=70)
    # name = ctk.CTkEntry(rootT, width=250, textvariable=nm, font=('Ubuntu', 16))
    # name.place(x=120, y=70)
    
    rnoInstr = ctk.CTkLabel(rootT, text='ID :', font=('Helvetica', 14))
    rnoInstr.place(x=10, y=120)
    rno = ctk.CTkEntry(rootT, width=90, textvariable=rn, font=('Ubuntu', 16))
    rno.place(x=120, y=120)

    def back_to_menu():
        rootT.destroy()

    def count_id(s_id):
        if(s_id==""):
            label.configure(text="Enter the  ID ")
        else:
            x = pickle.load(open("X.sav", "rb"))
            y = pickle.load(open("Y.sav", "rb"))
            count=0
            for id in y:
                if re.search(s_id, str(id)):
                    count+=1
                    print("Index: ",y.index(id))
            print("Count: ",count," ID: ",s_id)
            label.configure(text="Count : "+str(count))

    def count_name(s_name):
        if(s_name==""):
            label.configure(text="Enter the  NAME ")
        else:
            x = pickle.load(open("X.sav", "rb"))
            y = pickle.load(open("Y.sav", "rb"))
            count=0
            for id in y:
                if re.search(s_name, str(id)):
                    count+=1
                    print("Index: ",y.index(id))
            print("Count: ",count," NAME: ",s_name)
            label.configure(text="Count : "+str(count))

    def del_id(s_id):
        if(s_id==""):
            label.configure(text="Enter the  ID ")
        else:
            x = pickle.load(open("X.sav", "rb"))
            y = pickle.load(open("Y.sav", "rb"))
            count=0
            for id in y:
                if re.search(s_id, str(id)):
                    count+=1
                    start = y.index(id)
            if(count<110):
                end = start+count+1
                del x[start:end]
                del y[start:end]
                print("Deleted")
                count=0
                for id in y:
                    if re.search(s_id, str(id)):
                        count+=1
                        print("Index: ",y.index(id))
                print("Count: ",count," ID: ",s_id)
                pickle.dump(x,open("X.sav", "wb"))
                pickle.dump(y,open("Y.sav", "wb"))
                label.configure(text="Deleted... New Count : "+str(count))
            else:
                label.configure(text="Count : "+str(count)+" Delete by name")

    def del_name(s_name):
        if(s_name==""):
            label.configure(text="Enter the  NAME ")
        else:
            x = pickle.load(open("X.sav", "rb"))
            y = pickle.load(open("Y.sav", "rb"))
            count=0
            for id in y:
                if re.search(s_name, str(id)):
                    count+=1
                    start = y.index(id)
            end = start+count+1
            del x[start:end]
            del y[start:end]
            print("Deleted")
            count=0
            for id in y:
                if re.search(s_name, str(id)):
                    count+=1
                    print("Index: ",y.index(id))
            print("Count: ",count," NAME: ",s_name)
            pickle.dump(x,open("X.sav", "wb"))
            pickle.dump(y,open("Y.sav", "wb"))
            label.configure(text="Deleted... New Count : "+str(count))
            delete_name_from_csv("staff_name.csv", s_name)
    
    def delete_name_from_csv(csv_file_path, name_to_delete):
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)

        rows_to_delete = []
        for i, row in enumerate(data):
            if row[0] == name_to_delete:
                rows_to_delete.append(i)

        if rows_to_delete:
            for i in reversed(rows_to_delete):
                del data[i]

            with open(csv_file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            # print(f"Deleted {len(rows_to_delete)} occurrences of {name_to_delete} from {csv_file_path}.")
        # else:
        #     print(f"{name_to_delete} not found in {csv_file_path}.")

            
    
        
    def check_input(event):
        value = event.widget.get()
        if value == '':
            combo_box['values'] = lst
        else:
            data = []
            for item in lst:
                if value.lower() in item.lower():
                    data.append(item)
            combo_box['values'] = data

    with open('staff_name.csv', 'r') as f:
        lst = f.read().split('\n')
            
    combo_box = ttk.Combobox(rootT,width=30, height=5)
    combo_box['values'] = lst
    combo_box.bind('<KeyRelease>', check_input)
    combo_box.place(x=150, y=90)

    cntBtn1 = ctk.CTkButton(rootT, text='Count by ID', font=('Ubuntu', 14), fg_color='#21A565',width=100, height=30, command=lambda:count_id(rn.get()))
    cntBtn1.place(x=45, y=170)

    cntBtn2 = ctk.CTkButton(rootT, text='Count by NAME', font=('Ubuntu', 14), fg_color='#21A565',width=100, height=30, command=lambda:count_name(combo_box.get()))
    cntBtn2.place(x=180, y=170)

    delBtn1 = ctk.CTkButton(rootT, text='Delete by ID', font=('Ubuntu', 14), width=100, height=30, command=lambda:del_id(rn.get()))
    delBtn1.place(x=45, y=230)

    delBtn2 = ctk.CTkButton(rootT, text='Delete by NAME', font=('Ubuntu', 14), width=100, height=30, command=lambda:del_name(combo_box.get()))
    delBtn2.place(x=180, y=230)

    cancelBtn = ctk.CTkButton(rootT, text='Cancel', font=('Ubuntu', 14), fg_color='#EB455F', width=200, height=35, command=back_to_menu)
    cancelBtn.place(x=80, y=280)

    label = ctk.CTkLabel(rootT, text="Count/Delete", font=("Helvetica", 16))
    label.place(x=140, y=320)

    rootT.mainloop()

if __name__ == '__main__':
    root = ctk.CTk()
    root.geometry("480x320")
    root.attributes('-fullscreen', True)
    root.title('Visgenix')

    img = Image.open("Visgenix Logo-01.png")
    img = img.resize((105, 110))
    bg = ImageTk.PhotoImage(img)


    logo = ctk.CTkLabel(master=root, image=bg, text='')
    logo.place(x=190, y=20)

    def back_to_menu():
        root.destroy()

    pickleBtn = ctk.CTkButton(root, text='Delete weights', font=('Ubuntu', 17), width=200, height=60, command=show_pickle_window)
    pickleBtn.place(x=50, y=170)

    trainBtn = ctk.CTkButton(root, text='Train', font=('Ubuntu', 17), width=200, height=60, command=show_train_window)
    trainBtn.place(x=300, y=170)

    cancelBtn1 = ctk.CTkButton(root, text='Cancel', font=('Ubuntu', 14), fg_color='#EB455F', width=200, height=35, command=back_to_menu)
    cancelBtn1.place(x=190, y=240)

    # camBtn = ctk.CTkButton(root, text='Camera', font=('Ubuntu', 12), width=80, height=40, command=camer)
    # camBtn.place(x=100, y=250)
    
    root.mainloop()