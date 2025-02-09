from tkinter import Frame, Text, messagebox
from tkinter.ttk import Combobox, Button, Entry, Label

from Circle import Circle
from Rectangle import Rectangle
from Cylinder import Cylinder

class TaskGui:
    def __init__(self, main):
        self.main = main
        main.title = "Task GUI"
        self.main.geometry("500x280")
       # self.main.title("Task GUI")

        self.frame = Frame(self.main, background="lightgreen")
        self.frame.pack(fill="both", expand=True)

        self.cmb = Combobox(self.frame, values=['Vali kujund', 'Ring', 'Ristkülik', 'Silinder'])
        self.cmb.current(0)
        self.cmb['state'] = 'readonly'
        self.cmb.grid(row = 0, column = 0, padx = 3, pady = 3, columnspan = 3, sticky='ew')

        #Ujuvad

        self.lbl_circle, self.txt_circle = self.create_circle_widget()
        self.lbl_a, self.lbl_b, self.txt_a, self.txt_b = self.create_rectangle_widget()
        self.lbl_cylinder_radius, self.lbl_cylinder_height, self.txt_cylinder_radius, self.txt_cylinder_height = self.create_cylinder_widget()
        self.btn_submit = self.create_button('Näita')
        self.result = self.create_result()


        self.forget_circle()
        self.forget_rectangle()
        self.forget_cylinder()

        self.cmb.bind('<<ComboboxSelected>>', self.changed)
        self.main.bind('<Return>', lambda event=None: self.calculate())

        
    def create_button(self, btntext = ""):
        button = Button(self.frame, text=btntext, command=lambda: self.calculate())
        button['state'] = 'disabled'
        button.grid(row = 3, column = 0, padx = 3, pady = 3, columnspan = 3, sticky='ew')
        return button

    def create_result(self):
        result = Text(self.frame, height=5, width=25)
        result.grid(row=4, column=0, padx=3, pady=3, columnspan=2, sticky='ew')
        result['state'] = 'disabled'
        return result

    def create_circle_widget(self):
        label = Label(self.frame, text="Raadius")
        label.grid(row=1, column=0, padx=3, pady=3, sticky='ew')
        text = Entry(self.frame, width=12)
        text.focus()
        text.grid(row=1, column=1, padx=3, pady=3, sticky='ew')
        return label, text

    def create_cylinder_widget(self):
        lbl_radius = Label(self.frame, text="Raadius")
        lbl_radius.grid(row=1, column=0, padx=3, pady=3, sticky='ew')

        txt_radius = Entry(self.frame, width=12)
        txt_radius.focus()
        txt_radius.grid(row=1, column=1, padx=3, pady=3, sticky='ew')

        lbl_height = Label(self.frame, text="Kõrgus")
        lbl_height.grid(row=2, column=0, padx=3, pady=3, sticky='ew')

        txt_height = Entry(self.frame, width=12)
        txt_height.focus()
        txt_height.grid(row=2, column=1, padx=3, pady=3, sticky='ew')


        return lbl_radius, lbl_height, txt_radius, txt_height

    def create_rectangle_widget(self):
        label_a = Label(self.frame, text='Külg a')
        label_a.grid(row=1, column=0, padx=3, pady=3, sticky='ew')

        text_a = Entry(self.frame, width=12)
        text_a.focus()

        text_a.grid(row=1, column=1, padx=3, pady=3, sticky='ew')

        label_b = Label(self.frame,text='Külg b')
        label_b.grid(row=2, column=0, padx=3, pady=3, sticky='ew')

        text_b = Entry(self.frame, width=12)
        text_b.grid(row=2, column=1, padx=3, pady=3, sticky='ew')
        return label_a,label_b, text_a, text_b

    def forget_circle(self):
        self.lbl_circle.grid_forget()
        self.txt_circle.grid_forget()
        self.btn_submit['state'] = 'disabled'

    def forget_rectangle(self):
        self.lbl_a.grid_forget()
        self.lbl_b.grid_forget()
        self.txt_a.grid_forget()
        self.txt_b.grid_forget()
        self.btn_submit['state'] = 'disabled'

    def forget_cylinder(self):
        self.txt_cylinder_radius.grid_forget()
        self.txt_cylinder_height.grid_forget()
        self.lbl_cylinder_radius.grid_forget()
        self.lbl_cylinder_height.grid_forget()
        self.btn_submit['state'] = 'disabled'

    def changed(self, event=None):
        combo_index = self.cmb.current()
        if combo_index == 0:
            self.forget_circle()
            self.forget_rectangle()
            self.forget_cylinder()
            self.btn_submit['state'] = 'disabled'
        elif combo_index == 1: #Circle
            self.lbl_circle, self.txt_circle = self.create_circle_widget()
            self.forget_rectangle()
            self.forget_cylinder()
            self.btn_submit['state'] = 'normal'
        elif combo_index == 2: #Rect
            self.lbl_a, self.lbl_b, self.txt_a, self.txt_b = self.create_rectangle_widget()
            self.forget_circle()
            self.forget_cylinder()
            self.btn_submit['state'] = 'normal'
        elif combo_index == 3: # Cylin
            self.lbl_cylinder_radius, self.lbl_cylinder_height, self.txt_cylinder_radius, self.txt_cylinder_height = self.create_cylinder_widget()
            self.forget_rectangle()
            self.forget_circle()
            self.btn_submit['state'] = 'normal'
            
        self.clear_result()

    def clear_result(self):
        self.result.config(state='normal')
        self.result.delete('1.0', 'end')
        self.result.config(state='disabled')

    def calculate(self):
        cmb_index = self.cmb.current()
        if cmb_index == 1: #Circle
            try:
                radius = float(self.txt_circle.get().strip())
                circle = Circle(radius=radius)

                self.clear_result()
                self.result.config(state='normal')
                self.result.insert('1.0', str(circle))
                self.result.config(state='disabled')
            except ValueError:
                messagebox.showerror("Error", "Raadius peab olema number.")
            self.txt_circle.delete(0, 'end')
            self.txt_circle.focus()
        elif cmb_index == 2:
            try:
                a = float(self.txt_a.get().strip())
                b = float(self.txt_b.get().strip())
                rectangle = Rectangle(a, b)

                self.clear_result()
                self.result.config(state='normal')
                self.result.insert('1.0', str(rectangle))
                self.result.config(state='disabled')

                pass
            except ValueError:
                messagebox.showerror("Error", "Külg/küljed peab olema number.")
            self.txt_a.delete(0, 'end')
            self.txt_b.delete(0, 'end')
            self.txt_a.focus()
        elif cmb_index == 3: #Cylinder
            try:
                radius = float(self.txt_cylinder_radius.get().strip())
                height = float(self.txt_cylinder_height.get().strip())
                cylinder = Cylinder(radius=radius, height=height)
                self.clear_result()
                self.result.config(state='normal')
                self.result.insert('1.0', str(cylinder))
                self.result.config(state='disabled')
            except ValueError:
                messagebox.showerror("Error", "Raadius/kõrgus peab olema number.")
            self.txt_cylinder_radius.delete(0, 'end')
            self.txt_cylinder_height.delete(0, 'end')
            self.txt_cylinder_radius.focus()
