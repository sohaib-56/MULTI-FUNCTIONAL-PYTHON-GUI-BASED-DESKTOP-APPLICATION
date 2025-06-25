import tkinter
from tkinter import messagebox
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














#  ////////////////////////////// Update File ///////////////////////////////////////////////

def update_file():
    """This function will update the password if the user exits"""

    def back():
        """It will return the control back to the Home Page"""
        window.destroy()
        project_main.mainmenu()



    def update_password():
        """This function checks whether the user already exists or not 
           and if user exists the Password will be Updated"""
        
        try:
            app_name = app_update_entry.get().lower()
            old_password = old_pass_entry.get().lower()
            new_password = new_updated_entry.get().lower()

            updated_lst = []
            app_found = False

            if app_name == "" or old_password == "" or new_password == "":
                messagebox.showwarning(title="Error",message="Do not let any field empty")
                return


            with open("pm_data.txt","r") as file:
                file_lines = file.readlines()
                for line in file_lines:
                    temp = line.strip().split(",")
                    retrieved_app = temp[0]
                    retrieved_password = temp[1]
                    dec_password = dec_pass(retrieved_password)

                    if app_name == retrieved_app and old_password == dec_password:
                        new_enc_pass = encrypt(new_password)
                        # temp[1] = new_enc_pass
                        updated_lst.append(f"{retrieved_app},{new_enc_pass}\n")
                        app_found = True
                    else:
                        updated_lst.append(line)


            if app_found == True:
                with open("pm_data.txt",'w') as file:
                    file.writelines(updated_lst)
                    messagebox.showinfo(title="Successful",message="Your password is Updated successfully.")
                    app_update_entry.delete(0,tkinter.END)
                    old_pass_entry.delete(0,tkinter.END)
                    new_updated_entry.delete(0,tkinter.END)
                    return
            else: 
                messagebox.showerror(title="Error",message="No such App exits.")
            

        except:
            messagebox.showerror(title="Error",message="Something went wrong!")





    window=tkinter.Tk()
    window.geometry("270x230")
    window.title("Update Password")
    window.iconbitmap("final_project_pic1.ico")

    frame=tkinter.Frame(window,background="black")
    frame.pack()

    top_label=tkinter.Label(frame,text="Update Your Password Here",background="red",fg="white",font=10)
    top_label.grid(row=0,columnspan=2,padx=10, pady=10)

    a_label=tkinter.Label(frame,text="App Name ",background="black",foreground="#0ab2fa")
    a_label.grid(row=1,column=0, padx=20, pady=10)

    app_update_entry=tkinter.Entry(frame)
    app_update_entry.grid(row=1,column=1,padx=10, pady=10)

    old_label=tkinter.Label(frame,text="Old Password ",background="black",foreground="#0ab2fa")
    old_label.grid(row=3,column=0,padx=20, pady=10)

    old_pass_entry=tkinter.Entry(frame,show="*")
    old_pass_entry.grid(row=3,column=1,padx=10, pady=10)

    new_label=tkinter.Label(frame,text="New Password ",background="black",foreground="#0ab2fa")
    new_label.grid(row=4,column=0,padx=20, pady=10)

    new_updated_entry=tkinter.Entry(frame,show="*")
    new_updated_entry.grid(row=4,column=1,padx=10, pady=10)

    btn_back=tkinter.Button(frame,text="  Back  ",background="#C70039",foreground="white",command=back)
    btn_back.grid(row=5,column=0,pady=20)

    btn_update=tkinter.Button(frame,text="Update Password",background="#C70039",foreground="white", command=update_password)
    btn_update.grid(row=5,column=1,pady=20)

    window.mainloop()



# /////////////////////////////////////////////////////////////////////////////












if __name__ == "__main__":
    update_file()






