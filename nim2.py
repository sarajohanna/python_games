
from Tkinter import *
import tkSimpleDialog
from tkMessageBox import askyesno, showerror

# # Create GUI frame
# root = Tk()

# # Create some text to put in GUI
# theLabel = Label(root, text="Woho, lets play!")

# # Add or "pack" theLabel in the frame
# theLabel.pack()

# # Makes sure the window is displayed until you close it
# root.mainloop()

# Create dialogbox to enter names of players
class MyDialog(tkSimpleDialog.Dialog):

    def body(self, master):
        Label(master, text="First:").grid(row=0, sticky=W)
        Label(master, text="Second:").grid(row=1, sticky=W)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        print first, second

root = Tk()
d = MyDialog(root)
print d.result

# Make buttons with alternatives to draw 1, 2 or 3 sticks

class NewDialogDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()

    def greet(self):
        print "hi"

    def createWidgets(self):
        Label(self,  text='Label').pack(side=TOP)
        Button(self, text='Button 1', command=self.dialog1).pack()
        Button(self, text='Button 2', command=self.dialog2).pack()
        Button(self, text='Button 3', command=self.greet ).pack(side=LEFT)
        Button(self, text='Button 4', command=self.quit ).pack(side=RIGHT)

    def dialog1(self):
        ans = askyesno('Title!', 'Text')
        if ans: self.dialog2()

    def dialog2(self):
        showerror('Error title', "Text")

if __name__ == '__main__': NewDialogDemo().mainloop()








# Set active player to 1 and print active player

players = [" ", " "]
print "Welcome to this beautiful game of Nim!"
players[0] = raw_input("What shall I call you, player 1? ")
players[1] = raw_input("What shall I call you, player 2? ")
player = players[0]

# Set the initial state, which is the number of objects we start with
state = 21
print "The game starts with {} sticks and the active player can draw 1, 2 or 3 sticks at a time.".format(state)

while (state > 1):
    # Get move from player
    move = input("{}, how many sticks do you want to draw? ".format(player))

    while (move > 3) or (move < 0):
        move = input("Oh no, I told you to draw 1, 2 or 3 sticks. Try again. ")

    # Update the state and show it
    state = state - move
    print "You draw {}, so now there are {} sticks left".format(move, state)

    # Check if player has won or lost
    if (state == 1):
        print "{}, you win the game!".format(player)

    # If the player did not win or lose, swtich players
    if (player == players[0]):
        player = players[1]
    else:
        player = players[0]

print "Game is over, hope you enjoyed it!"
