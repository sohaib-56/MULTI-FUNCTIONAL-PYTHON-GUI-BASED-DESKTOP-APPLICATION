import tkinter as tk
from tkinter import messagebox
import crossing_game
import project_main
import gui_hl_game



# ----------------------------------- Games Section ------------------------------------------------



def games():
    """ This Function contains the two buttons which will take you to your desired Games"""

    # try:

    def launch_game1():
        """ This Function will start our Crossing Game """

        window.destroy()
        crossing_game.start_crossing_game()



    def launch_game2():
        """ This Funtion will start our Guessing Games"""
        
        window.destroy()
        gui_hl_game.whole_game()

        
        

    def back():
        """ This Function will take you back to the GUI containing all the functionality of our Project"""
        window.destroy()
        project_main.all_fun()


    
    window = tk.Tk()
    window.title("MS Builds - Py-Games")
    window.configure(bg="indianred1")
    window.geometry("400x300")

    # Header Label
    header_label = tk.Label(window,text="🎮 MS Builds - Games Collection",font=("Arial", 14, "bold"),
                            bg="black",fg="#FFFFFF",height=2,pady=15)
    header_label.pack(fill='x')

    # Game 1 Button
    game1_btn = tk.Button(window,text="🐢Turtle Trek",font=("Helvetica", 14,"bold"),bg="aqua",
                          fg="black",width=20,height=2,command=launch_game1)
    game1_btn.pack(pady=(20,10))

    # Game 2 Button
    game2_btn = tk.Button(window,text="🎮Fame Duel",font=("Helvetica", 14,"bold"),bg="aqua",
                          fg="black",width=20,height=2,command=launch_game2)
    game2_btn.pack(pady=10)
    
    # Back Button
    game2_btn = tk.Button(window,text="Back",font=("Helvetica", 12,"bold"),bg="black",
                          fg="white",width=7,command=back)
    game2_btn.pack(pady=10)

    window.mainloop()




# ----------------------------------------------------------------------------------------------------









if __name__ == "__main__":
    games()







