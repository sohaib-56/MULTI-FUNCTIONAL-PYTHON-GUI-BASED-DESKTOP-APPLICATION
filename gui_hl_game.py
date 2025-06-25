import tkinter as tk
from tkinter import messagebox
import random
import fl_data
import games_section




# --------------------------------------- Colors -------------------------------------------------------


BGCOLOR = "magenta4"
FGCOLOR = "white"
HEADERCOLOR = "midnightblue"
BTNCOLOR = "firebrick1"


# ----------------------------------------------------------------------------------------------





# ------------------------------------- Global Variables -------------------------------------------------



# SCORE = 0
score = 0
person1={}
person2 = {}




# ------------------------------------------------------------------------------------------------------






# ------------------------------------- Similarity Checker -------------------------------------------------




def check_similarity():
    """ This Function will check whether person 1 and person 2 are equal or not 
        if they are equal it will change person 2 until person 1 and person 2 are not different. """
    global person1
    global person2

    flag = True
    while flag:
        if person1 == person2:
            person2 = random.choice(fl_data.data)
        else:
            break

    return person2





# ---------------------------------------------------------------------------------------------------










# ------------------------------------- Follower Checker -------------------------------------------------




def check_answer():
    """ This Function will check whether the user guessed Person has the more followers or not. """

    if person1["follower_count"] > person2["follower_count"]:
        # print(person1)
        return "1"
    elif person1["follower_count"] < person2["follower_count"]:
        # print(person2)
        return "2"






# ---------------------------------------------------------------------------------------------------











# ------------------------------------- Game Starter -------------------------------------------------



def whole_game():
    """ This is the Function that contains the GUI of the Game """

    global person1
    global person2

    person1 = random.choice(fl_data.data)
    person2 = random.choice(fl_data.data)

    while person1 == person2:
        person2 = random.choice(fl_data.data)
    
    # print(person1)
    # print(person2)



    # ------------------------------- Fllowing Count Function -------------------------------


    def following_count():   
        """ This Function contains the whole logic of the game like changing person if the 
            user guess is right or stoping the game on a wrong answer and keeping track of 
            the user score. """

        global score     
        global person1
        global person2
        

        try:

            user_choice = entry_text.get().strip()
            # print(user_choice)


            # If user has input an invalid option then it will not proceed
            if user_choice != "1" and user_choice != "2":
                messagebox.showerror(title="Error",message="Invalid Option selected")
                entry_text.delete(0,tk.END)
                return
                
            else:
                # If the input is valid then we will continue the process 
                user_guess = check_answer()

                if user_guess == user_choice:

                    if user_guess == "1":   
                        score += 1
                        # print(f"Score = {score}")
                        
                        entry_text.delete(0,tk.END)
                        messagebox.showinfo(title="Successful",message="You have guessed the right option.")
                        score_label.configure(text=f"Score = {score}")

                        person2 = random.choice(fl_data.data)
                        person2 = check_similarity()
                        
                        option_b.configure(text=f"Option B: {person2['name']}")
                        # print(person1)
                        # print(person2)
                        return
                        


                    elif user_guess == "2":
                        score += 1
                        # print(f"Score = {score}")

                        entry_text.delete(0,tk.END)
                        messagebox.showinfo(title="Successful",message="You have guessed the right option.")
                        score_label.configure(text=f"Score = {score}")
                        
                        person1 = person2
                        option_a.configure(text=f"Option A: {person1['name']}")
                        person2 = random.choice(fl_data.data)
                        person2 = check_similarity()
                        option_b.configure(text=f"Option B: {person2['name']}")
                        # print(person1)
                        # print(person2)
                        return

                

                    
                else:
                    # print(person1)
                    # print(person2)
                    messagebox.showinfo(title="Game Over",message="You have guessed wrong.Game Over." \
                    f"Your Score is {score}")
                    entry_text.delete(0,tk.END)
                    score = 0
                    score_label.configure(text=f"Score = {score}")
                    window.destroy()
                    games_section.games()

        except:
            print("There is something fishy going on!")



    # ----------------------------------------------------------------------------------------------







    # ----------------------------- Back Function ------------------------------------------------



    def back():
        """ This Function will take you back to the Games Section """

        window.destroy()
        games_section.games()



    # ----------------------------------------------------------------------------------------------







            
    # ---------------------------- Game GUI -------------------------------------------------------





    window = tk.Tk()
    window.title("MS Creators GUI Guessing Game")
    window.configure(bg=BGCOLOR)
    window.minsize(450, 350)

    # Header
    header_frame = tk.Frame(window, bg=HEADERCOLOR, pady=15)
    header_frame.pack(fill='x')

    header_label = tk.Label(header_frame,text="Guess the Person who is more Famous",\
                            font=("Verdana", 18, "bold"),bg=HEADERCOLOR,fg=FGCOLOR)
    header_label.pack()

    # Score Section
    score_frame = tk.Frame(window, bg=BGCOLOR)
    score_frame.pack(pady=10)

    score_label = tk.Label(score_frame,text="Score: 0",font=("Verdana", 14),bg=BGCOLOR,fg=FGCOLOR)
    score_label.pack()


    # Options Section (Vertical)
    options_frame = tk.Frame(window, bg=BGCOLOR)
    options_frame.pack(pady=10)

    option_a = tk.Label(options_frame,text=f"Option A: {person1['name']}",font=("Verdana", 12),\
                        bg=BGCOLOR,fg=FGCOLOR,anchor="w")
    option_a.pack(fill='x', padx=30, pady=5)

    option_b = tk.Label(options_frame,text=f"Option B: {person2['name']}",font=("Verdana", 12),\
                        bg=BGCOLOR,fg=FGCOLOR,anchor="w")
    option_b.pack(fill='x', padx=30, pady=5)



    # Instruction
    type_frame = tk.Frame(window, bg=BGCOLOR)
    type_frame.pack(pady=10)

    type_label = tk.Label(type_frame,text="Type 1 for Option A or Type 2 for Option B",\
                        font=("Verdana", 12),bg=BGCOLOR,fg=FGCOLOR)
    type_label.pack()


    #Entry
    entry_frame = tk.Frame(window, bg=BGCOLOR)
    entry_frame.pack(pady=10)

    entry_text = tk.Entry(entry_frame,font=("Verdana", 12),width=8,cursor="hand2")
    entry_text.pack()


    # Submit Button
    button_frame = tk.Frame(window, bg=BGCOLOR)
    button_frame.pack(pady=10)

    submit_btn = tk.Button(button_frame,text="Submit",font=("Verdana", 12, "bold"),cursor="hand2",\
                        bg=BTNCOLOR,fg=FGCOLOR,padx=10,pady=3,command=following_count)
    submit_btn.pack()

    back_btn = tk.Button(window,text="Back",font=("Poppins", 12, "bold"),cursor="hand2",\
                        bg=BTNCOLOR,fg=FGCOLOR,padx=7,command=back)
    back_btn.pack(side="right",padx=20,pady=10)


    window.mainloop()




# ------------------------------------------------------------------------------------------------









# ---------------------- Game Starter ------------------------------------------





if __name__ == "__main__":
    whole_game()






# ---------------------------------------------------------------------------------







