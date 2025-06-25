from turtle import Turtle

X_POS = 0
Y_POS = -270

class Player(Turtle):
    """ This class will creates our Turtle and place it on the bottom of the screen """
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)     #This function will set the heading of the Turtle 90 Degress so it will be facing North
        self.goto(0,-280)

    
    def move(self):
        """ This Function will move the Turtle Forward 20 paces on Up key press"""
    
        self.forward(10)


    def replace_player(self):
        """ This function will place the Turtle again to its startuing 
            Position when it reaches the Top of the Screen and completes a level"""
        
        self.goto(X_POS,Y_POS)





