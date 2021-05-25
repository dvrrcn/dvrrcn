#
# Darren Cronover
# 4 19 2021
# Python GUI Calculator

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)

        numbersFrame = Frame(self)
        numbersFrame.grid(row=0, column=0, rowspan=1)
        #create label for num1, place it on the grid
        self.num1_label = Label(numbersFrame, text = "Enter the first number: ")
        self.num1_label.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        #receive entry for num1, place it on the grid
        self.num1_ent = Entry(numbersFrame, width = 7)
        self.num1_ent.grid(row = 0, column = 2, columnspan = 2, sticky = E)

        #create label for num2, place it on the grid
        self.num2_label = Label(numbersFrame, text = "Enter the second number: ")
        self.num2_label.grid(row = 1, column = 0, columnspan = 2, sticky = W)

        #receive entry for num2, place it on the grid
        self.num2_ent = Entry(numbersFrame, width = 7)
        self.num2_ent.grid(row = 1, column = 2, columnspan = 2, sticky = E)

        #create label for result
        self.result_label = Label(numbersFrame, text = "Result: ")
        self.result_label.grid(row = 2, column = 0, columnspan = 2, sticky = W)

        #create textbox for result, place it on the grid 
        self.result_ent = Text(numbersFrame, width = 15, height = 1)
        self.result_ent.grid(row = 2, column = 2, columnspan = 2)
        
##        #addition button        
####        self.add_bttn = Button(self, text = "Add", command = self.add)
####        self.add_bttn.grid(row = 4, column = 2, columnspan = 1)
##
##        #subtraction button
##        self.subtract_bttn = Button(self, text = "Subtract", command = self.subtract)
##        self.subtract_bttn.grid(row = 4, column = 3, columnspan = 1)
##
##        #multiply button
##        self.multiply_bttn = Button(self, text = "Multiply", command = self.multiply)
##        self.multiply_bttn.grid(row = 5, column = 2, columnspan = 1)
##
##        #divide button
##        self.divide_bttn = Button(self, text = "Divide", command = self.divide)
##        self.divide_bttn.grid(row = 5, column = 3, columnspan = 1)

        #create button frame
        buttonFrame = Frame(self)
        buttonFrame.grid(row = 1, column = 0, rowspan=1)

        self.i = IntVar()
        
        #create clear button and put on grid
        self.clear_button = Button(buttonFrame, text = "Clear", command = self.clear)
        self.clear_button.grid(row = 1, column = 0)

        #create submit button and put on grid
        self.submit_button = Button(buttonFrame, text = "Submit", command = self.submit)
        self.submit_button.grid(row = 1, column = 1)

        #add buttonFrame to frame
        self.add_bttn = Radiobutton(buttonFrame, text = "Add", value=1, variable = self.i)
        self.add_bttn.grid(row = 0, column = 1)

        self.subtract_bttn = Radiobutton(buttonFrame, text = "Subtract", value=2, variable = self.i)
        self.subtract_bttn.grid(row = 0, column = 2)

        self.multiply_bttn = Radiobutton(buttonFrame, text = "Multiply", value=3, variable =self.i)
        self.multiply_bttn.grid(row = 0, column = 3)

        self.divide_bttn = Radiobutton(buttonFrame, text = "Divide", value=4, variable =self.i)
        self.divide_bttn.grid(row = 0, column = 4)

    def add(self):
        try:
            num1 = self.num1_ent.get()
            num2 = self.num2_ent.get()
            sum = int(num1) + int(num2)
            self.result_ent.delete(0.0, END)
            self.result_ent.insert(0.0, sum)

        except:
            self.err_msg.delete(0.0,END)
            self.err_msg.insert(0.0,'Numbers must be numeric!')

    def subtract(self):
        try:
            num1 = self.num1_ent.get()
            num2 = self.num2_ent.get()
            diff = int(num1) - int(num2)
            self.result_ent.delete(0.0, END)
            self.result_ent.insert(0.0, diff)

        except:
            self.err_msg.delete(0.0,END)
            self.err_msg.insert(0.0, 'Numbers must be numeric!')
            
    def multiply(self):
        try:
            num1 = self.num1_ent.get()
            num2 = self.num2_ent.get()
            product = int(num1) * int(num2)
            self.result_ent.delete(0.0, END)
            self.result_ent.insert(0.0, product)

        except:
            self.err_msg.delete(0.0,END)
            self.err_msg.insert(0.0, 'Numbers must be numeric!')
            
    def divide(self):
        try:
            num1 = self.num1_ent.get()
            num2 = self.num2_ent.get()
            quotient = int(num1) / int(num2)
            self.result_ent.delete(0.0, END)
            self.result_ent.insert(0.0, quotient)

        except:
            self.err_msg.delete(0.0,END)
            self.err_msg.insert(0.0, 'Numbers must be numeric!')
            
    def clear(self):
      self.result_ent.delete(0.0, END)

    def submit(self):
      if(self.i.get() == 1):
        self.add()
        
      elif(self.i.get() == 2):
        self.subtract()

      elif(self.i.get() == 3):
        self.multiply()

      elif(self.i.get() == 4):
        self.divide()

      else:
        self.divide()
      
# Press the green button in the gutter to run the script.
root = Tk()
root.title("Calculator")
root.geometry("350x135")
app = Application(master=root)
root.mainloop()
