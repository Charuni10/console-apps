def status(Train):
    print("Ticket status")
    print("Is your ticket booked? or is it in waiting list?")
    a=int(input("Enter 1 to check the ticket status \n 2 to check the waiting list status  \n 3 to check ticket availability"))
    if(a==1):
        tno=int(input("Enter the ticket number"))
        if(tno in Train.ticket):
            print("Ticket found")
            print("Ticket number: ",tno)
            print("Passenger name: ",Train.ticket[tno][0])
            print("Boarding point: ",Train.ticket[tno][1])
            print("Destination point: ",Train.ticket[tno][2])
        else:
            print("Ticket not found")
    elif(a==2):
        name=input("Enter the passenger name")
        if(name in Train.waitingt1):
            print("Passenger name: ",name)
            print("Boarding point: ",Train.waitingt1[name][0])
            print("Destination point: ",Train.waitingt1[name][1])
            print("Your ticket is in waiting list")
        else:
            print("Passenger name not found")

    elif(a==3):
        print("Ticket availability")
        print("Chennai",":",10-(Train.seat1[1]))
        print("Katpadi",":",10-(Train.seat1[2]))
        print("Salem",":",10-(Train.seat1[3]))
        print("Erode",":",10-(Train.seat1[4]))
        print("Tirupur",":",10-(Train.seat1[5]))
        print("Coimbatore",":",10-(Train.seat1[6]))
    