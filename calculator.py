from tkinter import *

operator =""


def BtnClick(numbers):
    global operator
    
    operator = operator + str(numbers)
    text_input.set(operator)

def Btn_Clear():
    global operator
    operator = ''
    text_input.set('')

def Btn_Equals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)



cal = Tk()
cal.title("Calculator")
text_input = StringVar()





    

txtDisplay = Entry(cal, font=('arial', 20 , 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg='powder blue', justify='right').grid(columnspan=4)
btn7 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('7'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='7' ).grid(row=1,column=0)
btn8 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('8'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='8' ).grid(row=1,column=1)
btn9 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('9'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='9' ).grid(row=1,column=2)
btnAddition = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('+'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='+' ).grid(row=1,column=3)
#===================================================================================================================================
btn4 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('4'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='4' ).grid(row=2,column=0)
btn5 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('5'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='5' ).grid(row=2,column=1)
btn6 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('6'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='6' ).grid(row=2,column=2)
btnSubtraction = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('-'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='-' ).grid(row=2,column=3)
#===================================================================================================================================
btn1 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('1'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='1' ).grid(row=3,column=0)
btn2 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('2'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='2' ).grid(row=3,column=1)
btn3 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('3'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='3' ).grid(row=3,column=2)
btnMultiplication = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('*'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='*' ).grid(row=3,column=3)
#===================================================================================================================================
btn0 = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('0'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='0' ).grid(row=4,column=0)
btnClear = Button(cal, font=('arial', 20 , 'bold'), command=Btn_Clear, fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='C' ).grid(row=4,column=1)
btnEquals = Button(cal, font=('arial', 20 , 'bold'), command=Btn_Equals, fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='=' ).grid(row=4,column=2)
btnDivision = Button(cal, font=('arial', 20 , 'bold'), command=lambda:BtnClick('/'), fg='black', bg='powder blue', padx=16, pady=16, bd=8, text='/' ).grid(row=4,column=3)

cal.mainloop()