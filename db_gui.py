import tkinter as tk
from tkinter import ttk


def set_up_window():

    def ok_btn_cmd():


    root = tk.Tk()
    root.title("Donor")
    root.geometry("800x800")

    top_label = ttk.Label(root, text="blood")
    top_label.grid(column=0, row=0)

    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1)
    name_entry = ttk.Entry(root, width=50)
    name_entry.grid(column=1, row=1)

    id_label = ttk.Label(root, text="Id:")
    id_label.grid(column=0, row=2)
    id_entry = ttk.Entry(root)
    id_entry.grid(column=1, row=2)

    root.mainloop()


if __name__ == '__main__':
    set_up_window()



    # root = tk.Tk()  # Defines the top, or root, window, so doesn't have a parent
    # content = ttk.Frame(root)  # The content Frame is placed in root
    # ok_btn = ttk.Button(content)  # The ok_btn button is placed in the content Frame