import random
def cancel(Train):
    global t1,d1
    print("Cancel the ticket here")
    tno=int(input("Enter the ticket number"))
    if(tno in Train.ticket):
        print("Ticket found")
        print("Ticket number: ",tno)
        print("Passenger name: ",Train.ticket[tno][0])
        print("Boarding point: ",Train.ticket[tno][1])
        print("Destination point: ",Train.ticket[tno][2])
        y=int(input("Do you want to cancel the ticket: \n 1.Yes \n 2.No"))
        if(y==1):
            print("Ticket cancelled")
            for i in range(Train.ticket[tno][3],Train.ticket[tno][4]+1):
                Train.seat1[i]-=1
            print(Train.seat1)
                   
            del Train.ticket[tno]
            if(len(Train.waitingt1)!=0):
                for i in range(1,len(Train.waitingt1)+1):
                    print(i)
                    t1=Train.waitingt1[i][3]
                    d1=Train.waitingt1[i][4]
                    print(t1,d1)
                    yes=False
                    for k in range(t1,d1+1):
                        if(Train.seat1[k]<2):
                            yes=True
                            break
                        else:
                            yes=False
                    if(yes==True):
                        tn=random.randint(10000,99999)
                        for j in range(t1,d1+1):
                            Train.seat1[j]+=1
                        print(Train.seat1)
                        print(Train.waitingt1[i])
                        Train.ticket[tn]=Train.waitingt1[i]
                        Train.waitingt1.pop(i)








                    # for(t1,d1) in Train.waitingt1.items():
                    # if(Train.seat1[t1]<2 and Train.seat1[d1]<2):
                    #     tn=random.randint(10000,99999)
                    #     print(t1,d1)
                    #     for i in range(t1,d1+1):
                    #         if(Train.seat1[i]==2):
                    #             break;
                    #         else:
                    #             Train.seat1[i]+=1
                    #             # Train.place1[i][Train.seat1[i]-1]=tn
                    #             print(Train.seat1)
                    #         # print(Train.place1)
                            
                    #             Train.ticket[tn]=[Train.waitingt1[i][0],Train.waitingt1[i][1],Train.waitingt1[i][2],Train.waitingt1[i][3],Train.waitingt1[i][4]]
                    #             print(Train.ticket[tn])
                    #     Train.waitingt1.pop(i)
        else:
            print("Ticket not cancelled")
            
    else:
        print("Ticket is not found")
