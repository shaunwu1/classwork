import tkinter as tk
from tkinter import ttk


def set_up_window():
    
    def ok_btn_cmd():
        print("Ok clicked")
        patient_name = name_value.get()
        id_number = id_value.get()
        blood_letter = blood_letter_value.get()
        rh = rh_factor_value.get()
        print("Patient name is {}".format(patient_name))
        print("Patient ID is {}".format(id_number))
        print("Patient's bloodtype is {}".format(blood_letter))
        print("Patient rh value is {}".format(rh))
    
    def cancel_btn_cmd():
        root.destroy()
    
    root = tk.Tk()
    root.title("Donor Database GUI")
    root.geometry("800x800")
    
    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column = 0, row = 0)

    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column = 0, row = 1)
    name_value = tk.StringVar()
    name_entry = ttk.Entry(root, textvariable=name_value)
    name_entry.grid(column = 1, row = 1)
    
    
    id_label = ttk.Label(root, text="Id:")
    id_label.grid(column = 0, row = 2)
    id_value = tk.StringVar()
    id_entry = ttk.Entry(root, textvariable=id_value)
    id_entry.grid(column = 1, row = 2)
    
    
    ok_button = ttk.Button(root, text="Ok", command=ok_btn_cmd)
    ok_button.grid(column=1, row=6)
    cancel_button = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_button.grid(column=2, row=6)
    
    blood_letter_value = tk.StringVar()
    A_check = ttk.Radiobutton(root, text="A", variable=blood_letter_value,
                              value="A")
    A_check.grid(column=0, row=3)
    
    B_check = ttk.Radiobutton(root, text="B", variable=blood_letter_value,
                              value="B")
    B_check.grid(column=0, row=4)
    
    AB_check = ttk.Radiobutton(root, text="AB", variable=blood_letter_value,
                              value="AB")
    AB_check.grid(column=0, row=5)
    
    O_check = tk.Radiobutton(root, text="O", variable=blood_letter_value,
                              value="O")
    O_check.grid(column=0, row=6)
    
    rh_factor_value = tk.StringVar()
    rh_factor_value.set("+")
    check_box_widget = tk.Checkbutton(root, text="Rh Positive",
                                       variable=rh_factor_value,
                                       onvalue='+', offvalue='-')
    
    check_box_widget.grid(column=1, row=4)
    root.mainloop()


if __name__ == '__main__':
    set_up_window()