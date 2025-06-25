import tkinter as tk
from tkinter import messagebox
import time
# from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import project_main








# --------------------  GUI Window with for User Product Selection --------------------------------





def user_menu():
    """ This Function will show a window and the get the name of the Product the user wants \
        and containing a on_search function  """


    def back():
        """ This Function will take you back to the Bots Section after destroying current window """

        root.destroy()
        project_main.bots()


    def on_search():
        """ Checks whether the entry field is empty then it shows a warning to the user \
            otherwise it calls the automation function to start our Bot's working """

        product = product_entry.get().lower().strip()
        if product:
            # print(f"User wants to search for: {product}")
            root.destroy()  
            automation(product)
        else:
            messagebox.showwarning("Input Required", "Please enter a product name.")


    
    root = tk.Tk()
    root.title("Daraz Price Suggesting Bot")
    root.geometry("400x250")
    root.configure(bg="#CAA40B")

    # Label
    title_label = tk.Label(root, text="What do you want to buy?",font=("Segoe UI", 14, "bold"),\
                        bg="#f4f4f9", fg="#333")
    title_label.pack(pady=(30, 10))

    # Entry
    product_entry = tk.Entry(root, font=("Segoe UI", 11), width=30, bd=2, relief="groove")
    product_entry.pack(pady=10)
    product_entry.focus()

    # Button
    search_button = tk.Button(root, text="Search on Daraz",font=("Segoe UI", 10, "bold"),bg="#4CAF50",\
                            fg="white",activebackground="#45A049",activeforeground="white",command=on_search)
    search_button.pack(pady=20)


    back_btn = tk.Button(root,width=5,text="Back",font=("Segoe UI", 12, "bold"),bg="olivedrab1",command=back)
    back_btn.pack(padx=(300,0),pady=(10,0))


    # Run
    root.mainloop()










# ----------------------------------------------------------------------------------------------













# --------------------------------- Bot Automation Section ----------------------------------------






def automation(user_product):
    """ This function will start the working of our Bot and goes to the Daraz.pk website \
        scraps the necessary data and starts evaluating their prices then it will give the \
        suggestion to the user accordingly. """
        

    try:
            
        # Initializing the Chrome driver
        driver = uc.Chrome()
        driver.maximize_window()


        # Opening Webpage by using driver.get() method
        driver.get("https://daraz.pk")


        # specifying sleep time so that all the elements of the website will be settled
        time.sleep(3)


        page = driver.find_element(By.XPATH,"//div[@class='lzd-header-content daraz-pc-theme-style']")
        page.click()

        # Accessing Search bar by XPath by our own written class
        search_bar = driver.find_element(By.XPATH,"//input[@class='search-box__input--O34g']") 
        # print(search_bar)

        search_bar.click()
        
        search_bar.send_keys(user_product)
        
        search_bar.send_keys(Keys.ENTER)

        # Now here we will wait so that the screen tags or items gets settled
        time.sleep(3)

        # Getting the Ids of all the divs containing rupees for each product
        product_price = driver.find_elements(By.XPATH,"//span[@class='ooOxS']")

         
        price_list = []

        # Looping through all the divs and appending the text written in it one by one into the pricing_list 
        # i.e ['Rs. 199',.....]
        for i in range(len(product_price)):
            # Accessing the divs by index i one by one
            item = driver.find_elements(By.XPATH,"//span[@class='ooOxS']")[i]
            
            price_list.append(item.text)
            
            time.sleep(0.2)



        # print(price_list)

        total = 0

        all_rupees_list = []

        for price in price_list:
            amount = price.split()
            fetched_amount = amount[1].replace(",","")
            real_amount = int(fetched_amount)
            all_rupees_list.append(real_amount)
            total += real_amount



        driver.quit()

        time.sleep(2)

        average = total/len(price_list)
        # print(f"You require atleast Rs {average} for such product.Thanks a lot.")

        user_buying_amounts = value_evaluation(all_rupees_list)
        
        
        messagebox.showinfo(title="Product Price Suggestion", message=f"The minimum amount required for\
        buying such a product is Rs.{user_buying_amounts[0]} and the maximum amount for this type\
        of product is Rs.{user_buying_amounts[1]}.After doing analysis the \
        average amount will be Rs.{average}. Thanks a lot for using our Bot.\
        Have a good cup of Tea 🪶☕.Enjoy!")


        time.sleep(5)
        user_menu()



    except:
        messagebox.showerror(title="Oops",message="There might be something wrong going on!")
        user_menu()








# ----------------------------------------------------------------------------------------------








# ----------------------------- Minimum and Maximum Amount Evaluation --------------------------





def value_evaluation(coming_list):
    """ This Function returns the maximum and minimum amount needed to buy the 
        user desired product according to the products show on webpage """
    
    minimum_price = min(coming_list)
    maximum_price = 0
    for i in coming_list:
        if i > maximum_price:
            maximum_price = i
            
    min_max_list = [minimum_price,maximum_price]
    return min_max_list






# ----------------------------------------------------------------------------------------------








if __name__ == "__main__":
    user_menu()





