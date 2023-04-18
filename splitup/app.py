users={}
payment={}
user_name=[]
print("Welcome to the split up app")
n=int(input("Enter the number of users you : "))
i=0
while i<n:
    name=input("Enter the name of user : ")
    if name in user_name:
        print("User already exists in the list")
        print("Please enter a new name")
    else:
        users[name]=0
        user_name.append(name)
        i+=1
print("Users are : ",users)
print("We are ready to split the bill")
while True:
    print("What do you need to do?")
    a=int(input("Enter any one option: \n 1 to add a new user, \n 2 to add a bill, \n 3 to pay the bils, \n 4 check status \n 5 to exit : "))
    if(a==1):
        no=int(input("Enter the number of users you : "))
        j=0
        while j<no:
            names=input("Enter the name of user : ")
            if names in user_name:
                print("User already exists in the list")
                print("Please enter a new name")
            else:
                users[names]=0
                j+=1
        print("Users are : ",users)
    if(a==2):
        pay=input("Why did you pay the bill for? : ")
        use=input("Enter the name of user who paid the bill : ")
        if use not in users:
            print("User not found")
        else:
            amount=int(input("Enter the amount paid by the user : "))
            users[use]+=amount
            amount_split=amount//n
            print("Amount to be paid by everyone is : ",amount_split)
            t=[-amount_split for i in range(n)]
            ind=user_name.index(use)
            t[ind]=0
            print(t)
            payment[pay]=t
            print(payment)
    if(a==3):
        user_pay=input("Enter the name of user who needs to pay the amount : ")
        if user_pay not in user_name:
            print("User not found")
        else:
            amount_for=input("Reason for the payment: ")
            amount_pay=int(input("Enter the amount to be paid by the user : "))
            print("Amount to be paid by the user is : ",amount_pay)
            index=user_name.index(user_pay)
            payment[amount_for][index]+=amount_pay
            print(payment)
    if(a==4):
        print("Users who payed the amount : ",users)
        print("Payments which are pending : ",payment)
    if(a==5):
        print("Thank you for using the app")
        print("Have a nice day")
        break;
    else:
        print("Enter a valid option")
            