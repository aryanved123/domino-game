#Author: Aryan Ved
#Date: November 26, 2020
#Purpose: OOP2
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import random
from tkinter import *
from tkinter import messagebox
myScreen = Tk()


#PY5 CODE (DOMINOES)
class Domino:    
    #Construct
    def __init__ (self, value = 0, size = 30, direction = "H", face = True):
        self.value = value
        self.size = size
        self.diameter = self.size // 5
        self.direction = direction
        self.face = face
        
        self.valid()

    #Date: 11/21/20
    def __str__ (self):
        return "Value of your domino is " + str(self.value)

    #Date: 11/21/20
    def valid (self):
        if str(self.value).isdigit():
            if self.value//10 > 6 or self.value%10 > 6:
                self.value = 0
        else:
            self.value = 0
        if str(self.size).isdigit():
            if self.size < 30 or self.size > 100:
                self.size = 60
        else:
            self.size = 60
        self.diameter = self.size // 5
        self.gap = self.diameter // 2
        if self.direction != "H" and self.direction != "V":
            self.direction = "H"
        if type(self.face) != bool:
            self.face = True

    #Date: 11/21/20
    def getValue (self):
        digitOne = self.getInt("Please input a value x, with restrictions 0 <= x <= 6, for the first vale of your domino")
        digitTwo = self.getInt("Please input a value y, with restrictions 0 <= y <= 6, for the second value of your domino")

    #Date: 11/21/20
    def setValue (self,x=0):
        if intvalue >= 0 and intvalue // 10 <= 6 and intvalue % 6 <= 6:
            self.value = intvalue
        else:
            self.value = 0

    #Date: 11/21/20
    def getInt (self,prompt="Enter a positive integer:",low=0,high=6):
        strInput = " "
        intInput = -1
        validate = False
        while (not strInput.isdigit() or not validate):
            strInput = input(prompt)
            if strInput.isdigit():
                intInput = int(strInput)
                if (intInput >= low and intInput <= high):
                    validate = True
                else:
                    print("Error, the interger you input was not valid. Please try again>")
        return intInput

    #Date: 11/21/20
    def flip (self):
        digitOne = self.value // 10
        digitTwo = self.value % 10
        self.value = int(str(digitTwo) + str(digitOne))

    #Date: 11/21/20
    def setDirection (self, direction="H"):
        if direction == "H" or direction == "V":
            self.direction = direction
        else:
            self.direction = "H"

    #Date: 11/21/20
    def setSize (self, size=30):
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 30

    #Date: 11/21/20
    def setFace (self, face=True):
        if face == True or face == False:
            self.face = face
        else:
            self.face = True

    #Date: 11/21/20
    def randValue (self):
        self.value = random.randInt(0,6) * 10 + random.randInt(0,6)

    #Date: 11/22/20
    def create (self, canvas, x=0, y=0):
        self.diameter = self.size // 5
        self.gap = self.diameter // 2
        #Top half
        self.createHalf(canvas, x, y, self.value//10, "H")
        #Bottom half
        self.createHalf(canvas, x+self.size, y, self.value%10, "H")

    #Date: 11/22/20
    def createHalf (self, c, x=0, y=0, value=0, direction="H"):
        c.create_rectangle(x, y, x+self.size, y+self.size, width = 1, outline = "black", fill = "white")
        #TOP LEFT
        if value == 4 or value == 5 or value == 6:
            c.create_oval(x+self.gap, y+self.gap, x+self.gap+self.diameter, y+self.gap+self.diameter, fill = "black")
        #MIDDLE TOP
        if value == 6:
            c.create_oval(x+2*self.gap+self.diameter, y+self.gap, x+2*self.gap+2*self.diameter, y+self.gap+self.diameter, fill = "black")
        #BOTTOM LEFT
        if value == 2 or value == 3 or value == 4 or value == 5 or value == 6:
            c.create_oval(x+self.gap, y+7*self.gap, x+self.gap+self.diameter, y+3*self.gap+3*self.diameter, fill = "black")
        #MIDDLE
        if value == 1 or value == 3 or value == 5:
            c.create_oval(x+2*self.gap+self.diameter, y+2*self.gap+self.diameter, x+2*self.gap+2*self.diameter, \
                          y+2*self.gap+2*self.diameter, fill = "black")
        #TOP RIGHT
        if value == 2 or value == 3 or value == 4 or value == 5 or value == 6:
            c.create_oval(x+3*self.gap+2*self.diameter, y+self.gap, x+3*self.gap+3*self.diameter, y+self.gap+self.diameter, fill = "black")
        #MIDDLE BOTTOM
        if value == 6:
            c.create_oval(x+2*self.gap+self.diameter, y+3*self.gap+2*self.diameter, x+2*self.gap+2*self.diameter, \
                          y+3*self.gap+3*self.diameter, fill = "black")
        #BOTTOM RIGHT
        if value == 4 or value == 5 or value == 6:
            c.create_oval(x+3*self.gap+2*self.diameter, y+3*self.gap+2*self.diameter, x+3*self.gap+3*self.diameter, \
                          y+3*self.gap+3*self.diameter, fill = "black")



#PY6 CODE (DOMINO HANDS)
class DominoHands:
    #Defines the value of the three dominoes using random.randint
    #Defines the size of the three dominoes
    #Sets the face
    #Sets the Direction either Horizontal or Vertical
    #___CONSTRUCT___
    def __init__(self, domino1 = Domino(), domino2 = Domino(), domino3 = Domino(), notRandom = 0, size = 30, direction = "H", face = True):
        self.domino1 = domino1
        self.domino2 = domino2
        self.domino3 = domino3
        self.domino1.value = random.randint(0,6) * 10 + random.randint(0,6)
        self.domino2.value = random.randint(0,6) * 10 + random.randint(0,6)
        self.domino3.value = random.randint(0,6) * 10 + random.randint(0,6)
        self.value1 = domino1.value
        self.value2 = domino2.value
        self.value3 = domino3.value 
        self.domino1.valid
        self.domino2.valid
        self.domino3.valid
        self.size = size
        self.diameter = size // 5
        self.direction = direction
        self.face = face
    #Returns a String Value that is given from the randomizer
    def __str__ (self):
        strValue = "Value of your domino is " + str(self.value1 + self.value2 + self.value3)
        return strValue
    #Seperates each of the three values into two different digits
    #The letter "A" means it is the Tens Digit of the value
    #The letter "B" means it is the Ones Digit of the value
    def getDigit (self):
        # B variables are the ones digits
        # A variables are the tens digits
        self.valueB1 = self.domino1.value % 10
        self.valueB2 = self.domino2.value % 10
        self.valueB3 = self.domino3.value % 10
        self.valueA1 = self.domino1.value // 10
        self.valueA2 = self.domino2.value // 10
        self.valueA3 = self.domino3.value // 10

    #This sets the size based on user input or it goes by 60 as default
    #If the user enter a value then it is used otherwise 60 will be used
    def setSize (self):
        if size >= 30 and size <= 100:
            size = objsize.get()
        else:
            self.size = 60

        self.domino1.setSize(size,True)
        self.domino2.setSize(size, True)
        self.domino3.setSize(size, True)

    #This will sort the dominoes in order from least to greatest
    #This only occurs for the bottom hand
    #Here is where the values are really assigned to the bottom hand of the dominoes
    def sort (self):
        if self.value1 >= self.value2 and self.value1 >= self.value3:
            if self.value2 > self.value3:
                self.domino3.value = self.value1
                self.domino1.value = self.value3
            else:
                self.domino1.value = self.value2
                self.domino2.value = self.value3
                self.domino3.value = self.value1
        elif self.value2 >= self.value3 and self.value2 >= self.value1:
            if self.value3 > self.value1:
                self.domino1.value = self.value1
                self.domino2.value = self.value3
                self.domino3.value = self.value2
            else:
                self.domino1.value = self.value3
                self.domino2.value = self.value1
                self.domino3.value = self.value2
        elif self.value3 >= self.value2 and self.value3 >= self.value1:
            if self.value2 < self.value1:
                self.domino1.value = self.value2
                self.domino2.value = self.value1
                
    #This is the roll function that determines the random value of each of the domino
    def roll (self):
        self.domino1.value = random.randint(0,6) * 10 + random.randint(0,6)
        self.domino2.value = random.randint(0,6) * 10 + random.randint(0,6)
        self.domino3.value = random.randint(0,6) * 10 + random.randint(0,6)
    #This is where the dominoes will be created
    #Each domino is separated and there are two hands that print
    #The true values of the dominoes are pulled from here and given to the createHalf function
    #The bottom three dominoes are not created here since it has to be sorted
    def create(self, canvas, x, y, sort):
        if sort == True:
            self.sort()
        else:
            canvas.delete(ALL)
        curN1 = 10
        curN2 = 10
        curN3 = 10
        for n in range (3):
            size = -1
            size = objsize.get()
            self.domino1 = Domino(self.domino1.value,size,"H",True)
            self.domino2 = Domino(self.domino2.value,size,"H",True)
            self.domino3 = Domino(self.domino3.value,size,"H",True)
            if n == 1:
                self.domino1.setDirection("V")
                self.domino2.setDirection("V")
                self.domino3.setDirection("V")
            elif n == 2:
                curN1 = 10
                curN2 = 10
                curN3 = 10
                self.domino1.setFace(False)
                self.domino2.setFace(False)
                self.domino3.setFace(False)
            curN1 = 10
            curN2 = 10
            curN3 = 10
        self.domino1.create(canvas, x,y)
        self.domino2.create(canvas,x+self.domino1.size*2+self.domino1.diameter,y)
        self.domino3.create(canvas,x+self.domino1.size*4+self.domino1.diameter*2,y)
        curN1 += 10 + self.domino1.size
        curN2 += 10 + self.domino2.size
        curN3 += 10 + self.domino3.size
        if self.domino1.direction == "H" or self.domino2.direction == "H" or self.domino3.direction == "H":
            curN1 += self.domino1.size
            curN2 += self.domino2.size
            curN3 += self.domino3.size
    #This is where the run of the dominoes is calculated
    #This function uses the getDigit function in order pull the seperated values
    #It calculates the run of some of the special cases
    def getRun (self):
        runs=0
      #special case if all 3 numbers are the same
        if self.domino1.value == self.domino2.value == self.domino3.value:
            runs=3
            self.runs = runs
            return runs
        self.getDigit()
        if self.valueA1 == self.valueA2 or self.valueA1 == self.valueA3 or self.valueA1 == self.valueB2 or self.valueA1 == self.valueB3:
            runs += 2
        if self.valueB1 == self.valueA2 or self.valueB1 == self.valueB2 or self.valueB1 == self.valueA3 or self.valueB1 == self.valueB3:
            runs += 2
        if self.valueA2 == self.valueA3 or self.valueA2 == self.valueB3:
            runs += 2
        if self.valueB2 == self.valueA3 or self.valueB2 == self.valueB3:
            runs += 2
      #special case if overcounted situations, since max runs is 3
        if runs > 3:
            runs = 3
      #special case if 2 dominos are the same 
        if self.domino1.value == self.domino2.value or self.domino1.value == self.domino3.value:
            runs = 2
    
      #special case when one matching digit between ALL 3 values
        if (self.valueA1==self.valueA2==self.valueA3 or self.valueA1==self.valueB2==self.valueB3 or self.valueA1==self.valueB2==self.valueA3 or self.valueA1==self.valueA2==self.valueB3 or self.valueA1==self.valueA2==self.valueB2):
            runs=2
        if (self.valueB1==self.valueA2==self.valueA3 or self.valueB1==self.valueB2==self.valueB3 or self.valueB1==self.valueB2==self.valueA3 or self.valueB1==self.valueA2==self.valueB3 or self.valueB1==self.valueA2==self.valueB2):
            runs=2
        self.runs = runs
        return runs
#This will calculate the percent of each possible run that occurs within 10000 hands
#The percents will go up to two decimal place
#The percent are returned as strings with the percentage symbol beside them
def getGenerate (zerorun = 0, tworuns = 0, threeruns=0):
    percentzero = float(zerorun / 100)
    percenttwo = float(tworuns / 100)
    percentthree = float(threeruns / 100)
    return str(percentzero) + '%'+ ' - ' + str(percenttwo) + '%'+ ' - ' + str(percentthree) + '%'
#Dominoes for the bottom hand are printed here is the sort option becomes true
#Error message will print if the values are less than or equal to 6
#Run is brought in from the getRun function and it is printed within a label
#Generating the percentages of the possible runs occuring within 10000 hands
#The generate uses a loop to calculate the amount of times the run with the same value is given
#The genereate is also printed within a label just below the getRun label
def keyPress (event):
    import random
    if event.char == "d" or event.char == "D":
	    if objvalue1.get() % 10 > 6 or objvalue2.get() % 10 > 6 or  objvalue3.get() % 10 > 6:
		    messagebox.showerror("Error, make sure that both values are less than or equal to 6")
	    else:
	         dominoHandsObject = DominoHands()
	         dominoHandsObject.create(canvas, x=0, y=0, sort = False)
	         dominoHandsObject.create(canvas, x=0, y=100, sort = True)
	         
    elif event.char == "r" or event.char == "R":
        dominoHandsObject1 = DominoHands()
        dominoHandsObject1.getRun()
        inEncLbl = Label(myScreen, width = 48, text="Your RUN Value Is: ")
        inEncLbl.config(background = "light green")
        inEncLbl.grid(row=2, column=2, columnspan = 1, padx=5, pady=0, sticky=NW)
        inEncLbl = Label(myScreen, width = 20, text=dominoHandsObject1.runs, background = "white", relief = "groove")
        inEncLbl.grid(row=2, column=2, padx=1, pady=0, sticky=NE)
    elif event.char == "g" or event.char == "G":
        notRandom = 1
        getrun1 = 0
        getrun2 = 0
        getrun3 = 0
        generate = StringVar()
        generate.set(' ')
        for i in range(1, 10001):
            runTester = DominoHands()
            if runTester.getRun() == 0:
                getrun1 += 1
            elif runTester.getRun() == 2:
                getrun2 += 1
            else:
                getrun3 += 1
        generate.set(getGenerate(getrun1, getrun2, getrun3))
        inEncLbl = Label(myScreen, width = 48, text="Number of Runs of 0, 2, 3 That Can Be Produced From 10000 Hands ")
        inEncLbl.config(background = "light green")
        inEncLbl.grid(row=4, column=2, columnspan = 1, padx=5, pady=10, sticky=W)
        inEncLbl = Label(myScreen, width = 20, textvariable=generate, background = "white", relief = "groove")
        inEncLbl.grid(row=4, column=2, padx=1, pady=10, sticky=E)
    elif event.char == "x" or event.char == "X":
        myScreen.destroy()


#MAIN----------------------------------------------------------------------------
run=IntVar()
canvas = Canvas(myScreen, width = 660, height = 200)
myScreen.title("Domino Hands")
myScreen.config(background = "black")
myScreen.resizable (0,0)
canvas.config(background = "purple")
canvas.bind("<Key>", keyPress)
canvas.focus_set()
canvas.grid(column = 2, row = 1, padx = 5, pady = 5)
objsort = StringVar()
objroll = IntVar()
objvalue1 = IntVar()
objvalue2 = IntVar()
objvalue3 = IntVar()
objsize = IntVar()
myScreen.geometry("1000x300")
widSizeFrame = LabelFrame(myScreen,text="Size",padx=90,pady=15)
widScales = Scale(widSizeFrame,from_=60,to=100,orient=HORIZONTAL,variable=objsize)
widSizeFrame.grid(row=1,column=1,sticky=NW,padx=10)
widScales.grid(row=1)
inEncLbl = Label(myScreen, text="1. Select Your Size and Hit The 'd' key to draw  ")
inEncLbl.config(background = "light blue")
inEncLbl.grid(row=1, column=1, padx=0, pady=0)
inEncLbl = Label(myScreen, text=" 2. To Calculate The Run Hit The 'r' Key")
inEncLbl.config(background = "light blue")
inEncLbl.grid(row=1, column=1, padx=0, pady=0, sticky=S)
inEncLbl = Label(myScreen, text="3. Hit The 'g' Key to Calculate The Generate ")
inEncLbl.config(background = "light blue")
inEncLbl.grid(row=2, column=1, padx=0, pady=0)
inEncLbl = Label(myScreen, text="4. Hit The 'x' Key To Exit The Program  ")
inEncLbl.config(background = "light blue")
inEncLbl.grid(row=3, column=1, padx=0, pady=0, sticky=N)


mainloop()
