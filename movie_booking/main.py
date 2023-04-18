admin="admin"
password="admin"
user={}
ticket1={}
ticket2={}
ticket3={}
ticket4={}
while True:
    print("Welcome to the ticket booking system")
    print("Please login to continue")
    n=input("Enter your are \n 1 admin \n 2 user \n 3 exit") 
    if n=="1":
        
            user_name=input("Enter your username: ")
            if user_name=="admin":
                
                print("Welcome admin")
                user_password=input("Enter your password: ")
                if user_password=="admin":
                    print("Login successful")
                    print("Welcome to the admin panel")
                    print("1. View all users")
                    print("2. View all tickets")
                    print("3. Exit")
                    choice=int(input("Enter your choice: "))
                    if choice==1:
                        print("The users are: ",user)
                    elif choice==2:
                        print("The tickets booked for 10:00 AM are: ",len(ticket1))
                        print("The tickets booked for 2:00 PM are: ",len(ticket2))
                        print("The tickets booked for 6:00 PM are: ",len(ticket3))
                        print("The tickets booked for 10:00 PM are: ",len(ticket4))
                    elif choice==3:
                        print("Thank you for using the ticket booking system")
                        break
                    else:
                        print("Invalid choice")
                else:
                    print("Invalid password")
    elif n=="2":

        user_name=input("Enter your username: ")
        if user_name not in user.keys():
            print("Welcome new user", user_name)
            print("Enter the timing of the movie you want to watch")
            print("1. 10:00 AM")
            print("2. 2:00 PM")
            print("3. 6:00 PM")
            print("4. 10:00 PM")
            print("5. Exit")
            choice=int(input("Enter your choice: "))
            if choice==1:
                print("You have selected 10:00 AM")
                if(len(ticket1)<100):
                    print("The seats available are: ",100-len(ticket1))
                    seats=int(input("Enter the number of seats you want to book: "))
                    if(seats<=100-len(ticket1)):
                        for i in range(seats):
                            ticket1[len(ticket1)+1]=[user_name]
                        print("Your tickets have been booked")
                        user[user_name]=[seats,"10:00 AM",len(ticket1)-seats]
                        print("You have booked",user[user_name][0],"tickets for the movie at",user[user_name][1],"your tickets start from",user[user_name][2],"to",user[user_name][2]+user[user_name][0]-1)

                    else:
                        print("Sorry,the seats are full")
                        print("Please select another timing")
                else:
                    print("Sorry,the seats are full")
                    print("Please select another timing")

            elif choice==2:
                print("You have selected 2:00 PM")
                if(len(ticket2)<100):
                    print("The seats available are: ",100-len(ticket2))
                    seats=int(input("Enter the number of seats you want to book: "))
                    if(seats<=100-len(ticket2)):
                        for i in range(seats):
                            ticket2[len(ticket2)+1]=[user_name]
                        print("Your tickets have been booked")
                        user[user_name]=[seats,"2:00 PM",len(ticket2)-seats]
                        print("You have booked",user[user_name][0],"tickets for the movie at",user[user_name][1],"your tickets start from",user[user_name][2],"to",user[user_name][2]+user[user_name][0]-1)
                        
                    else:
                        print("Sorry,the seats are full")
                        print("Please select another timing")
                else:
                    print("Sorry,the seats are full")
                    print("Please select another timing")
            elif choice==3:
                print("You have selected 6:00 PM")
                if(len(ticket3)<100):
                    print("The seats available are: ",100-len(ticket3))
                    seats=int(input("Enter the number of seats you want to book: "))
                    if(seats<=100-len(ticket3)):
                        for i in range(seats):
                            ticket3[len(ticket3)+1]=[user_name]
                        print("Your tickets have been booked")
                        user[user_name]=[seats,"6:00 PM",len(ticket3)-seats]
                        print("You have booked",user[user_name][0],"tickets for the movie at",user[user_name][1],"your tickets start from",user[user_name][2],"to",user[user_name][2]+user[user_name][0]-1)
                    else:
                        print("Sorry,the seats are full")
                        print("Please select another timing")
                else:
                    print("Sorry,the seats are full")
                    print("Please select another timing")
            elif choice==4:
                print("You have selected 10:00 PM")
                if(len(ticket4)<100):
                    print("The seats available are: ",100-len(ticket4))
                    seats=int(input("Enter the number of seats you want to book: "))
                    if(seats<=100-len(ticket4)):
                        for i in range(seats):
                            ticket4[len(ticket4)+1]=[user_name]
                        print("Your tickets have been booked")
                        user[user_name]=[seats,"10:00 PM",len(ticket4)-seats]
                        print("You have booked",user[user_name][0],"tickets for the movie at",user[user_name][1],"your tickets start from",user[user_name][2],"to",user[user_name][2]+user[user_name][0]-1)
                    else:
                        print("Sorry,the seats are full")
                        print("Please select another timing")
                else:
                    print("Sorry,the seats are full")
                    print("Please select another timing")
            elif choice==5:
                print("Thank you for using the ticket booking system")
                break
            else:
                print("Invalid choice")
        else:
            print("Welcome back",user_name)
            print("You have already booked",user[user_name][0],"tickets for the movie at",user[user_name][1],"your tickets start from",user[user_name][2],"to",user[user_name][2]+user[user_name][0]-1)
            print("Do you want to cancel the tickets? yes or no")
            y=input()
            if(y=="yes" or y=="Yes"):
                print("Your ticket has been cancelled")
                if(user[user_name][1]=="10:00 AM"):
                    for i in range(1,user[user_name][0]):
                        del ticket1[user[user_name][2]+i]
                elif(user[user_name][1]=="2:00 PM"):
                    for i in range(user[user_name][0]):
                        del ticket2[user[user_name][2]+i]
                elif(user[user_name][1]=="6:00 PM"):
                    for i in range(user[user_name][0]):
                        del ticket3[user[user_name][2]+i]
                elif(user[user_name][1]=="10:00 PM"):
                    for i in range(user[user_name][0]):
                        del ticket4[user[user_name][2]+i]
                del user[user_name]
            elif(y=="no" or y=="No"):
                print("Okay! Thanks for booking the tickets")
    elif(n=="3"):
        print("Thank you for using the ticket booking system")
        break
    else:
        print("Invalid choice")