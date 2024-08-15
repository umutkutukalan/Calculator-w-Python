from simpleeval import SimpleEval
import tkinter as tk

evaluator = SimpleEval()
calculation = ""
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)
def evaluation_calculation():
    global calculation
    try:
        result = evaluator.eval(calculation)
        calculation = str(result)
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, 'Error')
def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')

def displayKey(event):
    return 'break'

root = tk.Tk()
root.title('Calculator')
root.geometry("235x300")

text_result = tk.Text(root, height=2, width=15, font=('Ariel', 24), bg='white', fg='black')
text_result.grid(columnspan=5)

text_result.bind("<Key>", displayKey)


#Numbers and Operators
buttons = [
    ('1',2,1), ('2',2,2), ('3',2,3), ('+',2,4),
    ('4',3,1), ('5',3,2), ('6',3,3), ('-',3,4),
    ('7',4,1), ('8',4,2), ('9',4,3), ('*',4,4),
    ('(',5,1), ('0',5,2), (')',5,3), ('/',5,4),
    ('C',6,1), ('=',6,2)
]

for (text, row, column) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, command=clear_field, height=2, width=2, font=('Ariel', 14))
        button.grid(row=row, column=column)
    elif text == '=':
        button = tk.Button(root, text=text, command=evaluation_calculation, height=2, width=15, font=('Ariel', 14))
        button.grid(row=row, column=column, columnspan=3)
    else:
        button = tk.Button(root, text=text, command=lambda t=text : add_to_calculation(t),height=2, width=2, font=('Ariel', 14))
        button.grid(row=row, column=column)


root.mainloop()



