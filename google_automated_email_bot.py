import tkinter as tk
from tkinter import messagebox
import time
# from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import project_main








# -------------------------------- User Account Details Extraction ------------------------------------------



def account_details():
    """ This Function will return the sender email and password"""

    credentials = []

    with open('email_bot_owner_info.txt','r') as file:
        file_data = file.read()
        user_data = file_data.strip().split(",")
        username = user_data[0]
        password = user_data[1]
        # print(username,password)
        credentials.append(username)
        credentials.append(password)


    return credentials





# ----------------------------------------------------------------------------------------------------------











# -------------------------------- Google Automation Section ------------------------------------------




def activate_email_bot(recipient,subject,message):
    """ This will activate our Bot and our Email Sending Prrocess is started """


    try:
        user_details = account_details() 
        sender_email = user_details[0]
        send_password = user_details[1]
        
        # print(sender_email,send_password)


        # Initializing Undetected Chrome Driver
        driver = uc.Chrome()


        # Opening Gmail Webpage
        driver.get("https://gmail.com")


        # Maximizing window
        driver.maximize_window()


        # Email Filling
        driver.implicitly_wait(5)

        email = driver.find_element(By.XPATH, "//input[@id='identifierId']").send_keys(sender_email)

        email_next = driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()


        # Password Filling 
        driver.implicitly_wait(5)

        password_entry = driver.find_element(By.XPATH,"//input[@name='Passwd']").send_keys(send_password)

        time.sleep(1)
        password_next = driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()






        # After logging into our account Clicking on Compose to start writing an Email. 
        driver.implicitly_wait(6)
        compose_btn = driver.find_element(By.XPATH, "//div[contains(text(),'Compose')]").click()



        # Wait for some seconds so that the window for composing an email opens
        time.sleep(4)

        receiver_person_email = driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys(recipient)

        subject_of_email = driver.find_element(By.XPATH, "//input[@name='subjectbox']").send_keys(subject)

        message_to_send = driver.find_element(By.XPATH, "//div[@aria-multiline='true']").send_keys(message)



        # After writing the details wait for a second and then click the Send Button
        time.sleep(1)
        send_btn = driver.find_element(By.XPATH, "//div[@aria-label='Send ‪(Ctrl-Enter)‬']").click()
        
        
        # Now here wait for some time so that the Email will be sent Successfully.
        time.sleep(5)


        # Now Exiting our Bot after Successful Email Sending.
        driver.quit()


        time.sleep(2)
        email_bot_starter()

    
    except:
        messagebox.showerror(title="Error",message="Looks like there is something wrong going on!Check " \
        "you internet connection.")
        email_bot_starter()









# ----------------------------------------------------------------------------------------------------------











# ------------------------------ User Email Writing GUI ---------------------------------------------




def email_bot_starter():



    def send_email():
        recipient = email_entry.get().strip()
        subject = subject_entry.get().strip()
        message = message_text.get("1.0", tk.END).strip()
        
        if recipient == "" or subject == "" or message == "":
            messagebox.showwarning("Missing Info", "Please fill in all fields.")
            return


        root.destroy()
        activate_email_bot(recipient,subject,message)
        



    def back():
        """ This will take us back to the Bots Window """

        root.destroy()
        project_main.bots()



    root = tk.Tk()
    root.title("MS Email Sender Bot")
    root.geometry("500x550")
    root.configure(bg="lavender")  # khaki2, 
    root.resizable(False,False)


    # Heading
    heading = tk.Label(root, text="📧 Write your Email",font=("Segoe UI", 16, "bold"),bg="lavender", fg="#2c3e50")
    heading.pack(pady=(20, 10))


    # Email Entry
    email_label = tk.Label(root, text="Recipient Email:", bg="lavender", font=("Segoe UI", 11))
    email_label.pack(anchor="w", padx=40)
    email_entry = tk.Entry(root, font=("Segoe UI", 11), width=40,cursor="hand2")
    email_entry.pack(pady=5)


    # Subject Entry
    subject_label = tk.Label(root, text="Subject:", bg="lavender", font=("Segoe UI", 11))
    subject_label.pack(anchor="w", padx=40)
    subject_entry = tk.Entry(root, font=("Segoe UI", 11), width=40,cursor="hand2")
    subject_entry.pack(pady=5)


    # Message Text Box (Multi-line)
    message_label = tk.Label(root, text="Message:", bg="lavender", font=("Segoe UI", 11))
    message_label.pack(anchor="w", padx=40)

    message_text = tk.Text(root, font=("Segoe UI", 11), width=50, height=10, wrap="word",
                           bd=2, relief="groove",cursor="hand2")
    message_text.pack(pady=5)


    # Send Button
    send_btn = tk.Button(root, text="Send Email",font=("Segoe UI", 11, "bold"),bg="#3498db", fg="white", 
                        cursor="hand2", activebackground="#2980b9", activeforeground="white",command=send_email)
    send_btn.pack(pady=15)


    # Back Button
    back_btn = tk.Button(root,text="Back",width=5,cursor="hand2",font=("Segoe UI", 11, "bold"),
                         bg="sienna",fg="white",command=back)
    back_btn.pack(anchor="e",padx=30,pady=5)

    # Run the app
    root.mainloop()






# --------------------------------------------------------------------------------------------------------







if __name__ == "__main__":
    email_bot_starter()



