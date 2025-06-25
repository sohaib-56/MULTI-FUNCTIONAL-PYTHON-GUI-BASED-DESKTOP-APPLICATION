import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Canvas,PhotoImage
import random
import e_commerce_pricing_suggesting_bot
import google_automated_email_bot
import pm_save
import pm_retrieve
import pm_update
import pm_delete
import games_section
import gui_calculator




# ---------------------------- Starting Window of our Project ------------------------------------


def project_starter():
    "This is the Starting Window of our Project which displays our Logo and a Continue Button to proceed"


    def btn_clicked():
        """ This Function destroys the current window and take you to the \
            window containing all the functionality of our Project"""
        window.destroy()
        all_fun()




    window = tkinter.Tk()
    window.title("MS Py-Desktop Application")
    window.geometry("600x550")
    window.config(bg="black")


    pic = Image.open("MS4.png")
    photo = ImageTk.PhotoImage(pic)

    lbl= tkinter.Label(window, image=photo)
    lbl.grid(row=0,column=0,padx=20,pady=20)

    # print(lbl.keys())

    btn2 = tkinter.Button(window,text="Continue",font=("Arial",16,"bold"),fg="white",\
                    bg="maroon",width=10,cursor='hand2',command=btn_clicked)
    btn2.grid(row=1,column=0,padx=20)



    window.mainloop()




# -----------------------------------------------------------------------------------------------














# ---------------------- This Window describes all Functionalities of our Project ----------------



def all_fun():
    """ This Window describes all the Functionalities of our Project.It contains five Buttons\
        Password Manager, Bots, Games, Calculator """


    def open_password_manager():
        """ This Function will take you to the Login Page of the Password Manager """

        window.destroy()
        pm_signin_page()



    def open_bots():
        """ This Function will take you to the Bots section """
        
        window.destroy()
        bots()


    
    def open_games():
        """ This Function will take you to the Games Section """
        window.destroy()
        games_section.games()



    def open_calculator():
        """ This Function will take you to our Calculator GUI """

        window.destroy()
        gui_calculator.calculator_starter()



    def exit_app():
        """ This will close our DEsktop Application """
        window.destroy()





    window = tkinter.Tk()
    window.title("MS Multi-Functional Python GUI App")
    window.config(padx=50, pady=50, bg="#2c3e50")

    # Title Label
    title_label = tkinter.Label(text="MS Builds", font=("Poppins", 24, "bold"), fg="#1abc9c", bg="#2c3e50")
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))

    # Buttons
    btn1 = tkinter.Button(text="Password Manager", width=20, font=("Poppins", 16, "bold"), bg="#1abc9c",cursor="hand2",\
                    fg="white", command=open_password_manager)
    btn1.grid(row=1, column=0, padx=10, pady=10)

    btn2 = tkinter.Button(text="Bots", width=20, font=("Poppins", 16, "bold"), bg="#1abc9c",cursor="hand2",\
        fg="white", command=open_bots)
    btn2.grid(row=1, column=1, padx=10, pady=10)

    btn3 = tkinter.Button(text="Games", width=20, font=("Poppins", 16, "bold"), bg="#1abc9c",cursor="hand2",\
        fg="white", command=open_games)
    btn3.grid(row=2, column=0, padx=10, pady=10)

    btn4 = tkinter.Button(text="Calculator", width=20, font=("Poppins", 16, "bold"), bg="#1abc9c",cursor="hand2",\
        fg="white", command=open_calculator)
    btn4.grid(row=2, column=1, padx=10, pady=10)

    btn5 = tkinter.Button(text="Exit", width=42, font=("Poppins", 16, "bold"), bg="#e74c3c",cursor="hand2",\
    fg="white", command=exit_app)
    btn5.grid(row=3, column=0, columnspan=2, pady=(30, 0))



    window.mainloop()







# -----------------------------------------------------------------------------------------------












# ---------------------- Login Page of our Password Manager --------------------------------------
 



def pm_signin_page():
    """ This Function contains the Login GUI and it checks whether the correct \
        username & password has been written by the user."""


    def back():
        """ This Function destroys the window and take you back to the Project Starting GUI"""

        window.destroy()
        all_fun()


    def pmhome():
        """ This Function displays the Home Page of Password Manager where we have \
            Buttons to move towards the Save Password,Retrieve Password or \
            Update Password window"""
        
        try:

            username = user_entry.get().lower()
            password = user_password.get().lower()
            flag = False

            if username == "" or password == "":
                messagebox.showerror(title="Error",message="Do not let any field empty.")
                return

            with open("owner.txt",'r') as file:
                file_data = file.read()
                data_lst = file_data.strip().split(",")
                saved_user = data_lst[0]
                saved_password = data_lst[1]

                if username == saved_user and password == saved_password:
                    flag = True
                    messagebox.showinfo(title="Successful",\
                                        message="Credentials Matched Successfully! We are proceeding you to the Home Page of Password Manager")
                    window.destroy()
                    mainmenu()
                

            if flag == False:
                messagebox.showerror(title="Error",message="Wrong Username or Password")
                return



        except:
            messagebox.showerror(title="Error",message="Something went wrong")






    window = tkinter.Tk()
    window.title("Login Page")
    window.geometry("600x500")
    

    canvas = Canvas(width=600,height=500,highlightthickness=0)
    img = PhotoImage(file="signin2.png")
    canvas.create_image(300,250,image=img)
    canvas.grid(row=0)

    user_label = tkinter.Label(window,text="Username:",bg="black",fg="white",font=("Arial",14,"bold"))
    user_label.place(x=70,y=150)

    user_entry = tkinter.Entry(window,cursor="hand2")
    user_entry.place(x=100,y=190)


    password_label = tkinter.Label(window,text="Password:",bg="black",fg="white",font=("Arial",14,"bold"))
    password_label.place(x=70,y=240)

    user_password = tkinter.Entry(window,cursor="hand2",show="*")
    user_password.place(x=100,y=280)


    btn_login = tkinter.Button(window,text="LOGIN",cursor="hand2",bg="maroon",\
                               fg="white",font=("Arial",10,"bold"),command=pmhome)
    btn_login.place(x=130,y=340)
    
    
    btn_back = tkinter.Button(window,text=" Back ",cursor="hand2",bg="maroon",\
                               fg="white",font=("Arial",10,"bold"),command=back)
    btn_back.place(x=220,y=400)




    window.mainloop()






# -----------------------------------------------------------------------------------------------












#  ///////////////////////// MAIN MENU ////////////////////////////////////

def mainmenu():
    """Displays the Home Page of Password Manager/your Main Menu"""
    window = tkinter.Tk()
    window.title("Main Menu")
    window.geometry("440x410")  # Fixed window size
    window.iconbitmap("final_project_pic1.ico")


    def save_password():
        """Displays the Save Password interface"""
        window.destroy()
        pm_save.save_file()

    def retrieve_password():
        """Displays the Retrieve Password interface"""
        window.destroy()
        pm_retrieve.retrieve_file()

    def update_password():
        """Displays the Update Password interface"""
        window.destroy()
        pm_update.update_file()

    def delete_password():
        """Displays the Delete Password Interface"""
        window.destroy()
        pm_delete.delete_window()

    def back():
        """This Function will Close the Application"""
        window.destroy()
        pm_signin_page()



    # Load and resize the image
    image = Image.open("login_pm2.jpg")
    image = image.resize((220, 250))  # Increased image size
    photo = ImageTk.PhotoImage(image)

    frame = tkinter.Frame(window, bg="black")
    frame.pack()

    first_label = tkinter.Label(frame, text="Welcome to Password Manager", background="red", 
                                foreground="white", font=("Arial", 16, "bold"))
    first_label.grid(row=0, column=0, columnspan=2, pady=20)

    save_button = tkinter.Button(frame, text="Save Password", command=save_password,
                                 cursor="hand2", font=("Arial", 12))
    save_button.grid(row=1, column=0, padx=20, pady=10, sticky="w",ipadx=10)

    retrieve_button = tkinter.Button(frame, text="Retrieve Password", command=retrieve_password,
                                     cursor="hand2", font=("Arial", 12))
    retrieve_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

    update_button = tkinter.Button(frame, text="Update Password", command=update_password, 
                                   cursor="hand2",font=("Arial", 12))
    update_button.grid(row=3, column=0, padx=20, pady=10, sticky="w",ipadx=3)

    delete_button = tkinter.Button(frame, text="Delete Password", font=("Arial", 12), 
                                 cursor="hand2",command=delete_password)
    delete_button.grid(row=4, column=0, padx=20, pady=10, sticky="w",ipadx=5)

    back_button = tkinter.Button(frame, text=" Back ", font=("Arial", 12,"bold"), bg="red",fg="white",
                                 cursor="hand2",command=back)
    back_button.grid(row=5, columnspan=2, padx=30, pady=(0,20), sticky="e")

    image_label = tkinter.Label(frame, image=photo)
    image_label.grid(row=1, column=1, rowspan=4, padx=20, pady=20, sticky="e")

    window.mainloop()


# //////////////////////////////////////////////////////////////////////////////////////













# ----------------------------- Bots GUI Window -----------------------------------------------





def bots():
    """ This Function represents our Bots Section by displaying GUI.It contains two Buttons that will 
        lauch our Bots on clicking """



    def launch_first_bot():
        """ This Function will display the First Interface for our Daraz Bot where the user will
            type his/her desired product to gain Price Suggestion according to their product. 
            Here the Bot will start working and after analyzing the prices it will give the minimum 
            and maximum price of the product currently present on Daraz.pk """

        window.destroy()
        e_commerce_pricing_suggesting_bot.user_menu()
        



    def launch_second_bot():
        """ This function will display the GUI for our Email Bot. """

        window.destroy()
        google_automated_email_bot.email_bot_starter()




    def back():
        """ This Function destroys the current window and take the user back to the previous window"""

        window.destroy()
        all_fun()
    
        



    window = tkinter.Tk()
    window.title("Bots Control Panel")
    window.geometry("450x300")
    # root.configure(bg="#f0f4f7")
    window.configure(bg="chocolate")


    # Heading Label
    heading = tkinter.Label(window, text="🤖 Welcome to MS Builds Bots Section", 
                    font=("Garamond", 16, "bold"), 
                    bg="#f0f4f7", fg="#2c3e50")
    heading.pack(pady=(30, 20))
    # Segoe UI


    # First Bot Button
    first_bot_btn = tkinter.Button(window, text="Daraz Price Scraping Bot",font=("Segoe UI", 12, "bold"),
                            bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white",
                            width=25, height=2, command=launch_first_bot)
    first_bot_btn.pack(pady=10)



    # Second Bot Button
    second_bot_btn = tkinter.Button(window, text="Email Sending Bot",font=("Segoe UI", 12, "bold"),
                            bg="#27ae60", fg="white", activebackground="#1e8449", activeforeground="white",
                            width=25, height=2, command=launch_second_bot)
    second_bot_btn.pack(pady=10)


    back_btn = tkinter.Button(window,width=5,text="Back",font=("Segoe UI", 12, "bold"),bg="olivedrab1",command=back)
    back_btn.pack(padx=(340,0),pady=(10,0))



    window.mainloop()









# -----------------------------------------------------------------------------------------------








if __name__ == "__main__":
    project_starter()




