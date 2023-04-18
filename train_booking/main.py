from book import book
from cancel import cancel
from status import status
class train:
    def __init__(self):
        self.waitingt1={}
        # self.place1={1:[0,0,0,0,0,0,0,0,0,0],2:[0,0,0,0,0,0,0,0,0,0],3:[0,0,0,0,0,0,0,0,0,0],4:[0,0,0,0,0,0,0,0,0,0],5:[0,0,0,0,0,0,0,0,0,0],6:[0,0,0,0,0,0,0,0,0,0]}
        self.seat1={1:0,2:0,3:0,4:0,5:0,6:0}
        self.ticket={}
Train=train()

while True:
    print("Welcome to train booking system")
    print("Select a option you need to do: \n 1.Book a ticket \n 2.Cancel a ticket \n 3.Check the ticket status \n 4.Exit")
    k=int(input())
    if(k==1):
        book(Train)
    elif(k==2):
        cancel(Train)
    elif(k==3):
        status(Train)
    elif(k==4):
        break;
    else:
        print("Provide a valid input")
