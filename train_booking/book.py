import random
def book(Train):
    
        print("Booking")

        bor1=int(input("Select the boarding point \n 1.Chennai \n 2.Katpadi \n 3.Salem \n 4.Erode \n 5.Tirupur "))
        des1=int(input(("Select the destination point \n 1.Katpadi \n 2.Salem \n 3.Erode \n 4.Tirupur \n 5. Coimbatore ")))
        user=input("Enter the passenger name ")
        print(bor1,des1)
        if(bor1>des1 or bor1>5 or des1>5):
            print("Enter the boarding point and destination correctly")
        else:
            if(bor1==1):
                bor1="Chennai"
                t1=1
            elif(bor1==2):
                bor1="Katpadi"
                t1=2
            elif(bor1==3):
                bor1="Salem"
                t1=3
            elif(bor1==4):
                bor1="Erode"
                t1=4
            elif(bor1==5):
                bor1="Tirupur"
                t1=5
            if(des1==1):
                des1="Katpadi"
                d1=2
            elif(des1==2):
                des1="Salem"
                d1=3
            elif(des1==3):
                des1="Erode"
                d1=4
            elif(des1==4):
                des1="Tirupur"
                d1=5
            elif(des1==5):
                des1="Coimbatore"
                d1=6
            print("Passenger ",user," needs to book a ticket from ",bor1, " to ",des1)
            y=int(input("Do you want to confirm it: \n 1.Yes \n 2.No "))
            if(y==1):
                yes=False
                for i in range(t1,d1+1):
                    if(Train.seat1[i]<2):
                        yes=True
                        
                    else:
                        yes=False
                        break
                if(yes==True):
                    tn=random.randint(10000,99999)
                    for i in range(t1,d1+1):
                        Train.seat1[i]+=1
                    print("Yay!Your ticket is booked")
                    print("Your ticket number is ",tn)
                    print("Your boarding point is ",bor1)
                    print("Your destination point is ",des1)
                    Train.ticket[tn]=[user,bor1,des1,t1,d1]
                else:
                    print("Oops!No seats available")
                    w=int(input("Do you want to add your name to waiting list: \n 1.Yes \n 2.No "))
                    if(w==1):
                        if(len(Train.waitingt1)<=5):
                            Train.waitingt1[len(Train.waitingt1)+1]=[user,bor1,des1,t1,d1]
                            print("Your name is added to waiting list")
                            print(Train.waitingt1)
                        else:
                            print("Sorry!No seats available")
                    else:
                        print("Okay, your ticket is not booked")

            