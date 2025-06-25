import tkinter as tk
from tkinter import messagebox
import project_main

BGCOLOR = "hotpink4"
FGCOLOR = "white"
FONT = ("Arial",16,"bold")
HEADERFONT = ("Verdana", 18, "bold")
BTNFONT = ("Poppins",14,"bold")
BTNCOLOR = "lightsalmon3"





def calculator_starter():

    def back():
        """ This Function will take you back to the GUI containing all the 
            Functionality of our Project. """
        
        window.destroy()
        project_main.all_fun()

        
    def plus():
        if not first_value_entry.get() or not second_value_entry.get():
            messagebox.showerror(title="Error",message="Make sure you have entered both values")
            return
        else:
            num1 = int(first_value_entry.get().strip())
            num2 = int(second_value_entry.get().strip())
            answer = num1 + num2
            answer_val_label.configure(text=f"Answer = {answer}")
            messagebox.showinfo(title="After Calculation",message=f"Your answer is {answer}")
            first_value_entry.delete(0,tk.END)
            second_value_entry.delete(0,tk.END)
            answer_val_label.config(text="")


    def subtract():
        if not first_value_entry.get() or not second_value_entry.get():
            messagebox.showerror(title="Error",message="Make sure you have entered both values")
            return
        else:
            num1 = int(first_value_entry.get().strip())
            num2 = int(second_value_entry.get().strip())
            answer = num1 - num2
            answer_val_label.configure(text=f"Answer = {answer}")
            messagebox.showinfo(title="After Calculation",message=f"Your answer is {answer}")
            first_value_entry.delete(0,tk.END)
            second_value_entry.delete(0,tk.END)
            answer_val_label.config(text="")

    def multiply():
        if not first_value_entry.get() or not second_value_entry.get():
            messagebox.showerror(title="Error",message="Make sure you have entered both values")
            return
        else:
            num1 = int(first_value_entry.get().strip())
            num2 = int(second_value_entry.get().strip())
            answer = num1 * num2
            answer_val_label.configure(text=f"Answer = {answer}")
            messagebox.showinfo(title="After Calculation",message=f"Your answer is {answer}")
            first_value_entry.delete(0,tk.END)
            second_value_entry.delete(0,tk.END)
            answer_val_label.config(text="")

    def divide():
        if not first_value_entry.get() or not second_value_entry.get():
            messagebox.showerror(title="Error",message="Make sure you have entered both values")
            return
        else:
            num1 = int(first_value_entry.get().strip())
            num2 = int(second_value_entry.get().strip())
            answer = num1 / num2
            answer_val_label.configure(text=f"Answer = {answer}")
            messagebox.showinfo(title="After Calculation",message=f"Your answer is {answer}")
            first_value_entry.delete(0,tk.END)
            second_value_entry.delete(0,tk.END)
            answer_val_label.config(text="")





    window = tk.Tk()
    window.title("Welcome to our GUI Game")
    window.configure(bg=BGCOLOR)
    window.minsize(450, 350)

    # Header
    header_frame = tk.Frame(window, bg="brown3", pady=15)
    header_frame.pack(fill='x')

    header_label = tk.Label(header_frame,text="Calculator",\
                            font=HEADERFONT,bg="brown3",fg=FGCOLOR)
    header_label.pack()

    # Score Section
    entry1_frame = tk.Frame(window,width=100,bg=BGCOLOR)
    entry1_frame.pack(pady=(20,10))

    first_val_label = tk.Label(entry1_frame,text="First Value:",bg=BGCOLOR,fg=FGCOLOR,
                            font=FONT)
    first_val_label.grid(row=0,column=0,padx=27,sticky='w')

    first_value_entry = tk.Entry(entry1_frame,font=("Antono", 12,"bold"),cursor="hand2")
    first_value_entry.grid(row=0,column=1,sticky='e')


    # Options Section (Vertical)
    entry2_frame = tk.Frame(window,width=100,bg=BGCOLOR)
    entry2_frame.pack(pady=(10,10))

    second_val_label = tk.Label(entry2_frame,text="Second Value:",bg=BGCOLOR,fg=FGCOLOR,
                                font=FONT)
    second_val_label.grid(row=0,column=0,padx=10)

    second_value_entry = tk.Entry(entry2_frame,font=("Antono", 12,"bold"),cursor="hand2")
    second_value_entry.grid(row=0,column=1)




    # Instruction
    answer_frame = tk.Frame(window, bg=BGCOLOR)
    answer_frame.pack(pady=10)

    answer_val_label = tk.Label(answer_frame,text="",bg=BGCOLOR,fg=FGCOLOR,
                                font=FONT)
    answer_val_label.grid(row=0,column=2)


    # Buttons

    first_two_btn = tk.Frame(window, bg=BGCOLOR)
    first_two_btn.pack(pady=10)

    btn_plus = tk.Button(first_two_btn,text=" Add ",width=7,font=BTNFONT,cursor="hand2",\
                        bg=BTNCOLOR,fg="#FFFFFF",command=plus)
    btn_plus.grid(row=0,column=0)

    btn_subtract = tk.Button(first_two_btn,text="Subtract",font=BTNFONT,cursor="hand2",\
                        bg=BTNCOLOR,fg="#FFFFFF",command=subtract)
    btn_subtract.grid(row=0,column=1,padx=20)


    seconf_two_btn  = tk.Frame(window, bg=BGCOLOR)
    seconf_two_btn.pack(pady=10)

    btn_multiply = tk.Button(seconf_two_btn,text="Multiply",font=BTNFONT,cursor="hand2",\
                        bg=BTNCOLOR,fg="#FFFFFF",command=multiply)
    btn_multiply.grid(row=0,column=0)

    btn_divide = tk.Button(seconf_two_btn,text="Divide",width=7,font=BTNFONT,cursor="hand2",\
                        bg=BTNCOLOR,fg="#FFFFFF",command=divide)
    btn_divide.grid(row=0,column=1,padx=20)



    btn_back = tk.Button(window,text="Back",font=BTNFONT,cursor="hand2",\
                        bg="mediumblue",fg=FGCOLOR,command=back)
    btn_back.pack(padx=20,pady=10,side="right")

    window.mainloop()









if __name__ == "__main__":
    calculator_starter()







