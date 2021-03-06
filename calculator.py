from tkinter import *

expression = "" 


def press(num): 
	
	global expression 

	
	expression = expression + str(num) 

	
	equation.set(expression) 


 
def equalpress(): 
	
	try: 

		global expression 

	
		total = str(eval(expression)) 

		equation.set(total) 

		
		expression = "" 

	except: 

		equation.set(" error ") 
		expression = "" 



def clear(): 
	global expression 
	expression = "" 
	equation.set("") 



if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk()
    
   

	# set the background colour of GUI window 
	gui.configure(background="light green") 

	# set the title of GUI window 
	gui.title("Simple Calculator") 

	# set the configuration of GUI window 
	gui.geometry("570x620") 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression . 
	expression_field = Entry(gui, textvariable=equation) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expression_field.grid(ipady=40,columnspan=4, ipadx=100) 

	
    

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button1 = Button(gui, text=' 1 ', fg='black', bg='powder blue', 
					command=lambda: press(1), height=8, width=19) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='powder blue', 
					command=lambda: press(2), height=8, width=19) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='powder blue', 
					command=lambda: press(3), height=8, width=19) 
	button3.grid(row=2, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='powder blue', 
					command=lambda: press(4), height=8, width=19) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='powder blue', 
					command=lambda: press(5), height=8, width=19) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='powder blue', 
					command=lambda: press(6), height=8, width=19) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='powder blue', 
					command=lambda: press(7), height=8, width=19) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='powder blue', 
					command=lambda: press(8), height=8, width=19) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='powder blue', 
					command=lambda: press(9), height=8, width=19) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='powder blue', 
					command=lambda: press(0), height=8, width=19) 
	button0.grid(row=5, column=0) 

	plus = Button(gui, text=' + ', fg='black', bg='powder blue', 
				command=lambda: press("+"), height=8, width=19) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='powder blue', 
				command=lambda: press("-"), height=8, width=19) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='powder blue', 
					command=lambda: press("*"), height=8, width=19) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='powder blue', 
					command=lambda: press("/"), height=8, width=19) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='powder blue', 
				command=equalpress, height=8, width=19) 
	equal.grid(row=5, column=2) 

	clear = Button(gui, text='Clear', fg='black', bg='powder blue', 
				command=clear, height=8, width=19) 
	clear.grid(row=5, column='1') 

	# start the GUI 
	gui.mainloop() 
