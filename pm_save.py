import tkinter
from tkinter import messagebox
import random
import project_main




#  /////////////////////////////// Function for Encryption ////////////////////
 
def encrypt(user):
        """This function will encrypt user password in order to maintain the Security of the user"""

        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',\
            'x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',\
                'u','v','w','x','y','z']

        key=""
        shift=5
        user_text=user
        for i in user_text:
            if i in alphabet:
                pos = alphabet.index(i)
                new = pos+shift
                key = key+alphabet[new]
            else:
                key += i
        # print(f"the generated key is {key}")
        return key


#  ******************************************************


#  /////////////////////////////  Function For Decryption    ////////////////////////////////////


def dec_pass(saved_pass):
    """This function will decrypt your password in order to diplay the actual password the user has saved"""

    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',\
        'x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',\
            'u','v','w','x','y','z']

    key=""
    shift=5
    user_text=saved_pass
    for i in user_text:
        if i in alphabet:
            pos = alphabet.index(i)
            new = pos-shift
            key = key+alphabet[new]
        else:
            key += i
    return key



# *********************************************************










#  /////////////////////////// Save File /////////////////////////////////

def save_file():
    """This function contains the Save File GUI , a back function
       and a save_password function to save password and a checkapp function
       for checking whether the application already exists or not"""
    
    
    def back():
        """It will return the control back to the Home Page"""

        window.destroy()
        project_main.mainmenu()



    def gen_pass():
        """This will automatically generate a secure password for the user"""

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


        no_of_letters=4
        no_selected=2
        
        generated_pass=""
        for l in range(0,no_of_letters):
            generated_pass += random.choice(letters)

        for i in range(0,no_selected):
            generated_pass += random.choice(numbers)

        lst = list(generated_pass)
        random.shuffle(lst)
        generated_pass = ''.join(lst)
        
        s3_entry.delete(0,tkinter.END)
        s3_entry.insert(0,generated_pass)





    def show_pass():
        """ This Function will show the user its password which is first appeared as * """

        show_val = var.get()
        if show_val == "False":
            u_pass = s3_entry.get()
            s3_entry.configure(show="*")
            s3_entry.delete(0,tkinter.END)
            s3_entry.insert(0,u_pass)
        elif show_val == "True":
            s3_entry.configure(show='')





    def check_app(app_name):
        """This funcion will check whether the app whose password \
            you want to save already exists or not"""
            

        available_app = app_name
        with open("pm_data.txt",'r') as file:
            file_lines = file.readlines()
            for app in file_lines:
                saved_data = app.strip().split(",")
                saved_app = saved_data[0]
                if saved_app == available_app:
                    return True
                



    def save_password():
        """This function will save your app name and password into the text file"""
        
        try:
            app_name = s1_entry.get().lower()
            app_password = s3_entry.get().lower()

            if app_name=="" or app_password == "":
                messagebox.showwarning(title="Error",message="Do not let any field empty")
                return


            app_check = check_app(app_name)
            encrypted_password = encrypt(app_password)

            if app_check == True:
                messagebox.showerror(title="Error",message="Application already exists.")
            else:
                with open("pm_data.txt",'a')as file:
                    file.write(f"{app_name.strip()},{encrypted_password.strip()}\n")
                    messagebox.showinfo(title="Successful",message="Your Data is saved Successfully")
                    s3_entry.delete(0,tkinter.END)
                    s1_entry.delete(0,tkinter.END)
                    var.set(False)


        except:
            messagebox.showerror(title="Error",message="Something went wrong!")






    window=tkinter.Tk()
    window.title("Save Password")
    window.geometry("250x260")
    window.iconbitmap("final_project_pic1.ico")

    frame=tkinter.Frame(window,bg="black")
    frame.grid(row=0, column=0,sticky="news")    

    s_label=tkinter.Label(frame,text="Save Your Password Here",bg="red",fg="white",font="bold")
    s_label.grid(row=0, columnspan=2, padx=10, pady=20)

    s1_label=tkinter.Label(frame,text="App Name",bg="black",fg="white")
    s1_label.grid(row=1, column=0,sticky="w", padx=10, pady=10)

    s1_entry=tkinter.Entry(frame)
    s1_entry.grid(row=1, column=1, padx=20, pady=10)

    s3_label=tkinter.Label(frame,text="Password",bg="black",fg="white")
    s3_label.grid(row=3, column=0,sticky="w",  padx=10, pady=10)

    s3_entry=tkinter.Entry(frame,show="*")
    s3_entry.grid(row=3, column=1, padx=20, pady=10)


    var = tkinter.StringVar(value="False")
    show_btn = tkinter.Checkbutton(frame,text="Show",command=show_pass,cursor="hand2",variable=var,\
                                   onvalue="True",offvalue="False")
    show_btn.grid(row=4,column=0)


    btn_generate=tkinter.Button(frame,text="Generate Password",command=gen_pass)
    btn_generate.grid(row=4,column=1, sticky="e",padx=20 ,pady=15)

    btn_back=tkinter.Button(frame, text="  Back  ",bg="#C70039",fg="white",command=back)
    btn_back.grid(row=5,column=0, sticky="w",padx=20,pady=20)

    btn_get=tkinter.Button(frame, text="Save Password",bg="#C70039",fg="white",command=save_password)
    btn_get.grid(row=5,column=1,sticky="e", padx=20,pady=20)


    window.mainloop()



# ////////////////////////////////////////////////////////////////////////////////////










if __name__ == "__main__":
    save_file()








