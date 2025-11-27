from tkinter import *
from tkinter.ttk import Combobox 
from tkinter import filedialog, messagebox, ttk

window = Tk()
window.title("Журавлева Карина Руслановна")
window.geometry('600x400')
window.configure(bg='light blue')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control) 
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Текст')
tab_control.pack(expand=1, fill='both', padx=10, pady=10)

# Первая вкладка (калькулятор)
num1_ent = Entry(tab1, width=15, bg='white', fg='blue')
lbl_num1 = Label(tab1, text="Первое число:", bg='light blue', fg='dark blue', font=("Times New Roman", 12))
lbl_num1.grid(column=0, row=0, padx=10, pady=10, sticky=W)
num1_entry = Entry(tab1, width=15, bg='white', fg='blue')
num1_entry.grid(column=1, row=0, padx=10, pady=10)

oper_var = StringVar()
lbl_oper = Label(tab1, text="Операция:", bg='light blue', fg='dark blue', font=("Times New Roman", 12))
lbl_oper.grid(column=0, row=1, padx=10, pady=10, sticky=W)
oper_combo = Combobox(tab1, width=12, textvariable=oper_var)
oper_combo['values'] = ('+', '-', '*', '/')
oper_combo.current(0)
oper_combo.grid(column=1, row=1, padx=10, pady=10)

num2_ent = Entry(tab1, width=15, bg='white', fg='blue')
lbl_num2 = Label(tab1, text="Второе число:", bg='light blue', fg='dark blue', font=("Times New Roman", 12))
lbl_num2.grid(column=0, row=2, padx=10, pady=10, sticky=W)
num2_entry = Entry(tab1, width=15, bg='white', fg='blue')
num2_entry.grid(column=1, row=2, padx=10, pady=10)

def calc():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    oper = oper_var.get()
        
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        if num2 == 0:
            messagebox.showerror("Ошибка", "Деление на ноль!")
            return
        result = num1 / num2
        
    result_lbl.configure(text=f"Результат: {result}")

calc_btn = Button(tab1, text="Вычислить", command=calc, bg='blue', fg='white', font=("Times New Roman", 12))
calc_btn.grid(column=4, row=1, columnspan=2, padx=10, pady=20)

result_lbl = Label(tab1, text="Результат: ", font=("Times New Roman Bold", 16), bg='light blue', fg='dark blue')
result_lbl.grid(column=6, row=1, columnspan=2, padx=10, pady=10)


# Вторая вкладка (чекбоксы)
chk_st1 = BooleanVar()
chk1 = Checkbutton(tab2, text='Первый', var=chk_st1,bg='light blue', fg='dark blue', selectcolor='white', font=("Times New Roman", 12))
chk1.grid(column=0, row=0, padx=20, pady=10, sticky=W)

chk_st2 = BooleanVar()
chk2 = Checkbutton(tab2, text='Второй', var=chk_st2,bg='light blue', fg='dark blue', selectcolor='white', font=("Times New Roman", 12))
chk2.grid(column=0, row=1, padx=20, pady=10, sticky=W)

chk_st3 = BooleanVar()
chk3 = Checkbutton(tab2, text='Третий', var=chk_st3, bg='light blue', fg='dark blue', selectcolor='white', font=("Times New Roman", 12))
chk3.grid(column=0, row=2, padx=20, pady=10, sticky=W)

def clic():
    if chk_st1.get() and chk_st2.get() and chk_st3.get():
        messagebox.showinfo('Выбор', 'Вы выбрали все три варианта')
    elif chk_st1.get() and chk_st2.get():
        messagebox.showinfo('Выбор', 'Вы выбрали первый и второй варианты')
    elif chk_st1.get() and chk_st3.get():
        messagebox.showinfo('Выбор', 'Вы выбрали первый и третий варианты')
    elif chk_st2.get() and chk_st3.get():
        messagebox.showinfo('Выбор', 'Вы выбрали второй и третий варианты')
    elif chk_st1.get():
        messagebox.showinfo('Выбор', 'Вы выбрали первый вариант')
    elif chk_st2.get():
        messagebox.showinfo('Выбор', 'Вы выбрали второй вариант')
    elif chk_st3.get():
        messagebox.showinfo('Выбор', 'Вы выбрали третий вариант')
    else:
        messagebox.showinfo('Выбор', 'Вы ничего не выбрали')

btn = Button(tab2, text="Показать выбор", command=clic, bg='blue', fg='white', font=("Times New Roman", 12))
btn.grid(column=0, row=3, padx=20, pady=20)

# Третья вкладка (текст)
text_area = Text(tab3, width=50, height=10, bg='white', fg='blue', font=("Times New Roman", 12))
text_area.pack(padx=10, pady=10)

def load_text_from_file():
    path = filedialog.askopenfilename()
    if path:
        file = open(path, 'r')
        content = file.read()
        file.close()
        text_area.delete(1.0, END)
        text_area.insert(INSERT, content)
        messagebox.showinfo('Текст загружен!')

n_men = Menu(window)
file_menu = Menu(n_men, tearoff=0)
file_menu.add_command(label="Загрузить текст из файла", command=load_text_from_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.quit)
n_men.add_cascade(label="Файл", menu=file_menu)
window.config(menu=n_men)

window.mainloop()