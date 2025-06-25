import tkinter
from tkinter import messagebox
import project_main



# ///////////////////////////// Delete Password /////////////////////////////////////


def delete_window():
    """ This Function will display the GUI of Delete Password window """


    def back():
        """ This Function will take you back to the Home Page of Password Manager """

        window.destroy()
        project_main.mainmenu()


    def delete_pass():
        """ This Function will delete the Password of user desired application if exits."""

        try:
                
            app_name = app_entry.get().strip().lower()
            list_after_deletion = []
            flag = True

            if app_name == "":
                messagebox.showerror(title="Error",message="Don't let the App name field empty.")
                return

            with open('pm_data.txt','r') as file:
                file_data = file.readlines()

                for line in file_data:
                    info = line.strip().split(',')
                    available_app = info[0]

                    if app_name == available_app:
                        flag = False
                        print(f"here is {app_name}")
                        continue
                    
                    list_after_deletion.append(line) 

                

            if flag == False:
                with open('pm_data.txt','w') as file:
                    file.writelines(list_after_deletion)
                    app_entry.delete(0,tkinter.END)
                
                messagebox.showinfo(title="Successful",message="Password deleted successfully")
            else:
                messagebox.showerror(title="Error",message="No such Application exits.")
                
                
        except:
            messagebox.showerror(title="Error",message="Something fishy going on.")        






    window=tkinter.Tk()
    window.geometry("260x180")
    window.title("Delete Password")
    window.configure(bg="black")
    window.iconbitmap("final_project_pic1.ico")

    frame=tkinter.Frame(window,bg="black")
    frame.grid(row=0, column=0)

    r_label=tkinter.Label(frame,text="Delete your Password",bg="red",fg="white",font="bold")
    r_label.grid(row=0, columnspan=2, padx=10, pady=(20,10))

    app_label = tkinter.Label(frame, text="App name : ", background="black", fg="white")  # Empty label initially
    app_label.grid(row=2, column=0, padx=20, pady=10)

    app_entry = tkinter.Entry(frame, background="white")
    app_entry.grid(row=2, column=1, padx=10, pady=10)

    btn_back=tkinter.Button(frame, text="  Back  ",bg="#C70039",fg="white",command=back)
    btn_back.grid(row=4,column=0, sticky="w",padx=20,pady=20)

    btn_get=tkinter.Button(frame, text="Delete Password",bg="#C70039",fg="white",command=delete_pass)
    btn_get.grid(row=4,column=1,sticky="e", padx=20,pady=20)


    window.mainloop()


# ////////////////////////////////////////////////////////////////////////////////////////////







if __name__ == "__main__":
    delete_window()








