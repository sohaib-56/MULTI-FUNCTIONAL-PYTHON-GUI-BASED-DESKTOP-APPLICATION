import tkinter
from tkinter import messagebox
import project_main


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












#  ////////////////////////////// Retrieve File ////////////////////////////////

def retrieve_file():
    """This function contains the Retrieve File GUI , a back function
       and a retrieve function for retrieving password"""
    
    def back():
        """It will return the control back to the Home Page"""
        window.destroy()
        project_main.mainmenu()


    def retrieve_password():
        """This Function will Retrieve your Password that you have already saved"""

        try:
            app_name = app_entry.get().lower()

            if app_name == "":
                messagebox.showwarning(title="Error",message="Do not let Application name empty")
                return

            with open("pm_data.txt",'r') as file:
                file_lines = file.readlines()
                for line in file_lines:
                    temp = line.strip().split(",")
                    temp_app = temp[0]
                    temp_password = temp[1]
                    
                    if temp_app == app_name:
                        decrypted_password = dec_pass(temp_password)
                        output_pass_label.configure(text=f"Password = {decrypted_password}")
                        messagebox.showinfo(title="Successful",message="Password retrieved successfully.")
                        app_entry.delete(0,tkinter.END)
                        output_pass_label.configure(text="")
                        return
                    
                messagebox.showwarning(title="Error",message="No such Application exists.")
        except:
            messagebox.showerror(title="Error",message="Something went wrong!")






    window=tkinter.Tk()
    window.geometry("260x190")
    window.title("Retrieve Password")
    window.iconbitmap("final_project_pic1.ico")

    frame=tkinter.Frame(window,bg="black")
    frame.grid(row=0, column=0)

    r_label=tkinter.Label(frame,text="Retrieve Your Password",bg="red",fg="white",font="bold")
    r_label.grid(row=0, columnspan=2, padx=10, pady=10)

    app_label = tkinter.Label(frame, text="App name", background="black", fg="white")  # Empty label initially
    app_label.grid(row=2, column=0, padx=20, pady=10)

    app_entry = tkinter.Entry(frame, background="white")
    app_entry.grid(row=2, column=1, padx=20, pady=10)

    output_pass_label = tkinter.Label(frame, background="black", fg="white")
    output_pass_label.grid(row=3, columnspan=2, padx=20, pady=10)

    btn_back=tkinter.Button(frame, text="  Back  ",bg="#C70039",fg="white",command=back)
    btn_back.grid(row=4,column=0, sticky="w",padx=20,pady=20)

    btn_get=tkinter.Button(frame, text="Get Password",bg="#C70039",fg="white",command=retrieve_password)
    btn_get.grid(row=4,column=1,sticky="e", padx=20,pady=20)


    window.mainloop()


# ////////////////////////////////////////////////////////////////////////////////////////////








if __name__ == "__main__":
    retrieve_file()






