import random
import datetime

# Global List Declaration
y=" " #date function
rn=" "
n=" "
pn=" "
cin=" "
cout=" "
v=" "
a=" "
k=" "
r=" "
rbill=[]
roomno=[]

# Global Variable Declaration


#functions:
#home
#room_info
#date
#insertion
#booking
#restaurant
#roomnodisplay
#insert
#updation
#deletion
#display
#adminonly
#bill
#payment

# Home Function 

def home():
    print('----------------------------------HOTEL FIVE SEASONS----------------------------------')
    print("                A haven of luxury and comfort that everyone deserves.")
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    print('\t\t\t\t1.ROOM INFO \n\t\t\t\t2.BOOKING \n\t\t\t\t3.RESTAURANT  \n\t\t\t\t4.BILL AND CHECKOUT \n\t\t\t\t5.ADMINonly\n\t\t\t\t0.EXIT \n')
    ch=int(input('Enter choice : '))
    if ch==1:
        print()
        room_info()
    elif ch==2:
        booking()
    elif ch==3:
        restaurant()
    elif ch==4: 
        bill()
    elif ch==5:
        adminonly()
    else:
        exit()

#ROOM info
import mysql.connector as ms
mc=ms.connect(host='localhost',user='root',passwd='Dhru2003$',database='mysql')

if mc.is_connected()==False:
    print('Error in connection')
c=mc.cursor()
c.execute('Create database if not exists hotel;')
mc.close()

mc=ms.connect(host='localhost',user='root',passwd='Dhru2003$',database='hotel')
if mc.is_connected()==False:
    print('Error in connection')
c=mc.cursor()

try:
    c.execute("CREATE table if not exists restaurantcharges(roomno int,price int)")
    c.execute("CREATE table if not exists roominfo(roomtype varchar(10),price int, typee varchar(5))")
    
    sql="insert into roominfo(roomtype,price,typee)values (%s,%s,%s)"
    val=[("Standard",9000,"AC"),("Standard",7000,"NonAC"),("DELUXE",15000,"AC"),("DELUXE",11000,"NonAC")]
    c.executemany(sql,val)
    mc.commit()
except:
    pass

def room_info():
   
    c.execute("select* from roominfo")
    d=c.fetchall()
    print("Roomtype","Price","Type")
    j=1
    for i in d:
        print(j,i)
        j+=1
    z=int(input("0-BACK\n ->"))
    if z==0:
        home()
    else:
        exit()
    
    
#date function dd/mm/yyyy
#y=1
def date(d):

    global y
    y=1
    D={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if d[2]>=2022 and d[2]<=2023:
        if d[1]==2:
            if d[2]%100==0 and d[2]%4==0:#leap yr
                if d[0]<=29 and d[0]>=1:
                    pass
                else:
                    y=0
            else:
                if d[0]<=28 and d[0]>=1:
                    pass
                else:
                    y=0
        
        elif d[1] in D.keys():
        #if d[0]>=1 and d[0]<=D[d[1]]
            if d[1] in [1,3,5,7,8,10,12]:
                if d[0]>=1 and d[0]<=31:
                    pass
                else:
                    y=0
            elif d[1] in [4,6,9,11]:
                if d[0]>=1 and d[0]<=30:
                    pass
                else:
                    y=0
                
           
        else:
            y=0
    else:
        y=0
    return y



#Booking

def booking():
   
    global rn,n,pn,cin,cout,v,a,k
    while True:
        print('\t\t\t\tBOOKING')
        print()
        n=input('Enter your Name       :')
        pn=input('Enter Phone Number    :')            
        a=input('Enter address         :')
        
        #checks if any field is not empty
        if n=='' and pn=='' and a=='':
            print('The fields can\'t be empty')

        elif len(pn)!=10 and pn.isdigit():
            print("Kindly re-check entered Phone Number.")

        else:
            break

    #checkin check out
    #now check that checkin< checkout
    while True:
        cin=input('Enter Check-IN date d/m/yyyy: ')
        cout=input('Enter Check-OUT date d/m/yyyy: ')
        q1=cin.split('/')
        d1=[int(q1[0]),int(q1[1]),int(q1[2])]
        q2=cout.split('/')
        d2=[int(q2[0]),int(q2[1]),int(q2[2])]
        d1_=datetime.date(int(d1[2]),int(d1[1]),int(d1[0])) 
        d2_=datetime.date(int(d2[2]),int(d2[1]),int(d2[0]))
        nod=(d2_-d1_).days   #### calculating no of days of stay
        while True:
            if date(d1) and date(d2):#checking true value
                break
            else:
                print("Entered date deviates from specification. Please try again.")
                cin=input('Enter Check-IN date d/m/yyyy: ')
                cout=input('Enter Check-OUT date d/m/yyyy: ')
                q1=cin.split('/')
                d1=[int(q1[0]),int(q1[1]),int(q1[2])]
                q2=cout.split('/')
                d2=[int(q2[0]),int(q2[1]),int(q2[2])]
                continue

       
      
        if d1[2]<d2[2]:
            break
        elif d1[2]>d2[2]:
            print('Invalid year')
            continue
            
        elif d1[2]==d2[2]:
            if d1[1]<d2[1]:
                break
            elif d1[1]>d2[1]:
                print('Invalid month')
                continue
            elif d1[1]==d2[1]:
                if d1[0]<d2[0]:
                    break
                elif d1[0]>d2[0]:
                    print('Invalid date')
                    continue
                elif d1[0]==d2[0]:
                    print("Checking-In and Checking-Out on same day is not allowed.")
                    continue
                else:
                    continue
            else:
                continue
        else:
            continue

        break

    #room no generation
    print()
    print("1.Room Type: Standard AC \nPrice: 9000 \n")
    print("2.Room Type: Standard Non-AC \nPrice: 7000 \n")
    print("3.Room Type: Deluxe AC \nPrice:15000 \n")
    print("4.Room Type: Deluxe Non-AC \nPrice:11000 \n")
    print()
    print("Great rooms make great mornings.")
   
    
    while True:
        ch=int(input("Enter your choice 1/2/3/4:"))
    
        if ch==1:
            print("Room Type: Standard AC")
            print("Price: 9000")
            print()
            
            k,v=9000*nod,"Standard AC"
            
            break
                
        elif ch==2:
            print("Room Type: Standard Non-AC")
            print("Price: 7000")
            print()
            
            k,v=7000*nod,"Standard Non-AC"
            break
            
        elif ch==3:
            print("Room Type: Deluxe AC")
            print("Price:15000")
            print()
            
            k,v=15000*nod,"Deluxe AC"
            break
               
        elif ch==4:
            print("Room Type: Deluxe Non-AC")
            print("Price:11000")
            print()
            
            k,v=11000*nod,"Deluxe Non-AC"
            break
    
# randomly generating room no. and customer
# id for customer
        
# checks if alloted room no. & customer

    print()
    print("Proceeding with room payment....")
    val=payment()
    rn = random.randrange(60)+300
    while rn  not in roomno :
        rn = random.randrange(60)+300
        roomno.append(rn)
    print("***ROOM BOOKED SUCCESSFULLY***")
    print("Thank you for booking with us :)")
    print()        
    print("Your Room Number is - ",rn)
    
    
    insertion()               
    #print(roomno)                
                
    z=int(input("0-BACK\n ->"))
    if z==0:
        home()
    else:
        exit()
      
def roomnodisplay():
    global dbrn
    dbrn=[]
    st2="select roomno from admin"
    c.execute(st2)
    data2=c.fetchall()
    
    for row in data2:
        for i in row:
            dbrn.append(i)
    print(dbrn)
    return dbrn

# RESTAURANT FUNCTION
    
def restaurant():
    val=roomnodisplay()
    print(val)
    global r
    q=[]
    g=[]
   
    while True:
        w=int(input('Enter your room no:'))
        if w in dbrn:
            
            print("--------------------------HOTEL FIVE SEASONS-----------------------------")
            print("     Stirring your imagination one satisfying meal at a time.            ")

            print("-------------------------------------------------------------------------")

            print("Menu Card")

            print("-------------------------------------------------------------------------")
    
            print("BEVARAGES                             26 Dal Fry................ 140.00")

            print("----------------------------------    27 Dal Makhani............ 150.00")

            print(" 1 Regular Tea............. 20.00     28 Dal Tadka.............. 150.00")

            print(" 2 Masala Tea.............. 25.00")

            print(" 3 Coffee.................. 25.00     INDIAN BREADS")

            print(" 4 Cold Drink.............. 25.00     ----------------------------------")

            print(" 5 Bread Butter............ 30.00     29 Plain Roti.............. 15.00")

            print(" 6 Bread Jam............... 30.00     30 Butter Roti............. 15.00")

            print(" 7 Veg. Sandwich........... 50.00     31 Tandoori Roti........... 20.00")

            print(" 8 Veg. Toast Sandwich..... 50.00     32 Butter Naan............. 20.00")

            print(" 9 Cheese Toast Sandwich... 70.00")

            print(" 10 Grilled Sandwich........ 70.00    RICE")

            print("                                      ----------------------------------")
    
            print(" SOUPS                                33 Plain Rice.............. 90.00")

            print("----------------------------------    34 Jeera Rice.............. 90.00")

            print(" 11 Tomato Soup............ 110.00    35 Veg Pulao.............. 110.00")

            print(" 12 Hot & Sour............. 110.00    36 Peas Pulao............. 110.00")

            print(" 13 Veg. Noodle Soup....... 110.00")

            print(" 14 Sweet Corn............. 110.00    SOUTH INDIAN")

            print(" 15 Veg. Manchow........... 110.00    ----------------------------------")

            print(" MAIN COURSE                          38 Onion Dosa............. 110.00")

            print("----------------------------------    39 Masala Dosa............ 130.00")

            print(" 16 Shahi Paneer........... 110.00    40 Paneer Dosa............ 130.00")

            print(" 17 Kadai Paneer........... 110.00    41 Rice Idli.............. 130.00")

            print(" 18 Handi Paneer........... 120.00    42 Sambhar Vada........... 140.00")

            print(" 19 Palak Paneer........... 120.00")
            print(" 21 Matar Mushroom......... 140.00    ----------------------------------")

            print(" 22 Mix Veg................ 140.00    43 Vanilla................. 60.00")

            print(" 23 Jeera Aloo............. 140.00    44 Strawberry.............. 60.00")

            print(" 24 Malai Kofta............ 140.00    45 Pineapple............... 60.00")

            print(" 25 Aloo Matar............. 140.00    46 Butter Scotch........... 60.00")
                       
    
            ch=1
            rs=0
            r=0
            print("enter 0 to end your order")
            while ch!=0:
                ch=int(input(" -> "))
                if ch==1 or ch==31 or ch==32:
                    rs=20
                    r=r+rs
                elif ch<=4 and ch>=2:
                    rs=25
                    r=r+rs
                elif ch<=6 and ch>=5:
                    rs=30
                    r=r+rs
                elif ch<=8 and ch>=7:
                    rs=50
                    r=r+rs
                elif ch<=10 and ch>=9:
                    rs=70
                    r=r+rs
                elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
                    rs=110
                    r=r+rs
                elif ch<=19 and ch>=18:
                    rs=120
                    r=r+rs
                elif (ch<=26 and ch>=20) or ch==42:
                    rs=140
                    r=r+rs
                elif ch<=28 and ch>=27:
                    rs=150
                    r=r+rs
                elif ch<=30 and ch>=29:
                    rs=15
                    r=r+rs
                elif ch==33 or ch==34:
                    rs=90
                    r=r+rs
                elif ch==37:
                    rs=100
                    r=r+rs
                elif ch<=41 and ch>=39:
                    rs=130
                    r=r+rs
                elif ch<=46 and ch>=43:
                    rs=60
                    r=r+rs
                                            
                elif ch==0:
                    
                    print("Restaurant Bill: ",r)
                    
                    rbill.append([w,r])
                    import mysql.connector as sqltor1
                    mc2 = sqltor1.connect(host="localhost", user="root",passwd="Dhru2003$", database="hotel")
                    if mc2.is_connected() == False:
                        print("Error connecting!!!")
                    c2 = mc2.cursor()
                    d="select * from restaurantcharges"
                    c2.execute(d)
                    i=c2.fetchall()
                    for j in i:
                        q.append(j[0])
                        g.append(j[1])
                        
                    if w not in q:
                        sql1="insert into restaurantcharges(roomno,price)values (%s,%s)"
                        data=(w,r)
                        c2.execute(sql1,data)
                        mc2.commit()
                        mc2.close()

                    elif w in q:
                        z5=q.index(w)
                        sql1="update restaurantcharges set price=%s where roomno=%s"
                        data=(r+g[z5],w)
                        c2.execute(sql1,data)
                        mc2.commit()
                        mc2.close()                        
                                            
                    print("Proceeding with payment...")
                    v=payment()
                    break
                else:
                    print("Invalid input!!!")
            home()
        
        else:
            print("1-Please try ordering again! \n2.Homepage")
            ch=int(input('Enter 1/2:'))
            if ch==1:
                pass
            elif ch==2:
                home()
        
def insertion():
    global rn,n,pn,cin,cout,v,a,k
    import mysql.connector as m
    mc1=m.connect(host='localhost',user='root',passwd='Dhru2003$',database='hotel')
    if mc.is_connected()==False:
        print('Error in connection')
    c=mc1.cursor()
    q="CREATE table if not exists admin(roomno int primary key,name varchar(50),phone char(10),checkin varchar(20),checkout varchar(20),roomtype varchar(15), bill int,address varchar(30))"
    c.execute(q)
    mc1.commit()
    z="insert into admin (roomno,name,phone,checkin,checkout,roomtype,bill,address)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    data=(rn,n,pn,cin,cout,v,k,a)
    c.execute(z,data)
    mc1.commit()
    z="insert into restaurantcharges values({},{})".format(rn,0)
    c.execute(z)
    mc1.commit()
    return True

#admin()
import mysql.connector as sqltor
mc = sqltor.connect(host="localhost", user="root",passwd="Dhru2003$", database="hotel")
if mc.is_connected() == False:
    print("Error connecting!!!")
c = mc.cursor()

#INSERT THE VALUES

def insert():
    global rn,n,pn,cin,cout,v,a,k
    x=int(input('Enter the number of records to be inserted:'))
    for i in range(x):
        rn=int(input('Assign a room number:'))
        n=input('Enter Guest Name: ')
        pn=int(input('Enter Phone Number:'))
        cin=input('Enter Check-IN date in format d/m/yyy: ')
        cout=input('Enter Check-OUT date in format d/m/yyy: ')
        print("1.Room Type: Standard AC \nPrice: 9000")
        print("2.Room Type: Standard Non-AC \nPrice: 7000")
        print("3.Room Type: Deluxe AC \nPrice:15000")
        print("4.Room Type: Deluxe Non-AC \nPrice:11000") 
   
        k=input("Enter the Room-Type: ")
        v=input("Enter the Amount: ")
        a=input('Enter address: ')
        
        print()
        z="insert into admin (roomno,name,phone,checkin,checkout,roomtype,bill,address)values(%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(rn,n,pn,cin,cout,k,v,a)
        c.execute(z,data)
        mc.commit()
        z="insert into restaurantcharges values({},{})".format(rn,0)
        c.execute(z)
        mc.commit()

#update the value
def updation():

    x=int(input('Enter Room Number of records to be updated:'))
    print('To update Check-IN & Check-OUT dates:')
    t=roomnodisplay()
    
    
    if x in t:
        
        while True:
            cin=input('Enter Check-IN date d/m/yyyy: ')
            cout=input('Enter Check-OUT date d/m/yyyy: ')
            q1=cin.split('/')
            d1=[int(q1[0]),int(q1[1]),int(q1[2])]
            q2=cout.split('/')
            d2=[int(q2[0]),int(q2[1]),int(q2[2])]
    
            o1=date(d1)
            o2=date(d2)
            if o1==True and o2==True:
            #now check that checkin< checkout
                if d1[2]<d2[2]:
                    break
                elif d1[2]>d2[2]:
                    print('Invalid')
                    continue
            
                elif d1[2]==d2[2]:
                    if d1[1]<d2[1]:
                        break
                    elif d1[1]>d2[1]:
                        print('Invalid')
                        continue
                    elif d1[1]==d2[1]:
                        if d1[0]<d2[0]:
                            break
                        elif d1[0]>d2[0]:
                            print('Invalid')
                            continue
                        elif d1[0]==d2[0]:
                            print('Invalid')
                            continue
        st = "update admin set checkin='%s',checkout='%s' where roomno =%s" % (cin,cout,x)
        print("Updated the record.")
        c.execute(st)
        mc.commit()
        
    
#Remove the data
def deletion(x):    
    st = "delete from admin where roomno = %s"%(x,)
    c.execute(st)
    mc.commit( )
    print("Deleted the record.")
    return True


def display(): 
    while True:
        print('OPTIONS: \n1.Display all records \n2.Access a specific record \n3.exit')
        ch=int(input('Enter your choice :'))
        if ch==1:
            st = "select * from admin"
            c.execute(st)
            data = c.fetchall()
            for row in data:
                print(row)
            print()
        elif ch==2:
            x=int(input('Enter the room no:'))
            val=roomnodisplay()
            if x in val:
                
                st = " select * from admin where roomno=%s" % x 
                c.execute(st)
                data = c.fetchall()
                print(data)
                print()
            else:
                print('No booking for this roomno')
                print()
            
        elif ch==3:
            adminonly()
                
            
def adminonly():
    ans='y'
    while ans in 'Yy':
        print("MENU: \n1. Insert record. \n2. Update record. \n3. Remove record.  \n4. Display all records. \n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            insert()
        elif choice == 2:
            updation()
        elif choice ==3:
            x=int(input('Enter the Room Number of record to be deleted:'))
            deletion(x)
        elif choice == 4:
            display()
        else:
            home()
        
def bill():
    print('To print your Bill:')
    import mysql.connector as sqltor
    mc = sqltor.connect(host="localhost", user="root",passwd="Dhru2003$", database="hotel")
    if mc.is_connected() == False:
        print("Error connecting")
    c = mc.cursor()
    
    x=int(input('Enter your Room Number: '))
    
    val=roomnodisplay()
    
    print(val)
    if x in val:
        st = " select * from admin where roomno=%s" % x 
        c.execute(st)
        data = c.fetchall()
        #print(data)
        print()
   
        a1,a2,a3,a4,a5,a6,a7,a8=data[0]
        e="select * from restaurantcharges where roomno={}".format(x)
        c.execute(e)
              
        d=c.fetchall()
        rbill=d[0][1]     
        
        print('-------------------------------------------------------------------------------------------------------------')
        print()
        print("\t \t \t HOTEL FIVE SEASONS \t \t \t")
        print('-------------------------------------------------------------------------------------------------------------\n')
        print('\t \t \t Room number  :',x,'\n')
        print('\t \t \t Booking name :',a2)
        print('\t \t \t Checkin      :',a4)
        print('\t \t \t Checkout     :',a5)
        print('\t \t \t Room type    :',a6,'\n')
        print('\t \t \t Room charges         :',a7)
        print('\t \t \t Restaurant charges   :',rbill)
        print('\t \t \t GST of 19.7%         :',(a7+rbill)*0.197)
        print('-------------------------------------------------------------------------------------------------------------')
        print('Total Bill                    :',a7+rbill+(a7+rbill)*0.197)
        print()

        print("\t \t \t Checkout successful \t \t \t")
        print()
        print("\t \t \t Thank you for staying with us and Visit us again \t \t \t")
        print("\t \t \t \t \t \t:)")


        e2="delete from restaurantcharges where roomno={}".format(x)
        c.execute(e2)
        mc.commit()
        u=deletion(x)
        home()
        print()
        
    else:
        print("Room Number entered is Invalid!!!")
        home()

        


def payment():

    #after checking if payment is done/or not
    print()
    print(" MODE OF PAYMENT")
    print(" 1- Credit/Debit Card")
    print(" 2- Paytm/PhonePe")
    print(" 3- Using UPI")
    print(" 4- Cash")
    while True:
        x=input('->>')
        if x in ['1','2','3','4']:
            print()
            print("\n	    Pay For Hotel Five Seasons")
            print(" (y/n)")
            ch=str(input("->"))
            if ch=='y' or ch=='Y':
                print("Payment made successfully!")
                print()
                break
            else:
                print("Payment unsuccessful.")
                print("1. Redirect to HOMEPAGE.")
                print("2. Try paying again.")
                op=int(input("Enter 1 or 2:"))
                if op==1:
                    home()
                elif op==2:
                    payment()
                else:
                    print("Invalid input !!!")
                    payment()
            break
                
home()   
    








