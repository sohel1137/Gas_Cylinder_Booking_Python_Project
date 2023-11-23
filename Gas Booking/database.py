import mysql.connector
from mysql.connector import Error 
import pandas as pd


con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234567")

cursor = con.cursor()
try:
    sql = '''create database if not exists GasBook'''
    cursor.execute(sql)
    sql2 = '''use GasBook'''
    cursor.execute(sql2)

except Error as e:
    print("Error",e)

# ***************************** Customer Table Activity **********************************************************************

try:
    cursor = con.cursor()
    sql = 'create table if not exists customer(cust_id int auto_increment,cust_name varchar(50),Addhar_card_no bigint not null,cust_Email varchar(50),cust_address varchar(50),cust_gas_type varchar(10),cust_contact varchar(20),cust_Password varchar(20), primary key(cust_id));'

    cursor.execute(sql)
except Error as er:
    print(er)
#cust_email,cust_location,contact,gas_type,date datetime
try:
    cursor = con.cursor()
    sql = '''create table if not exists booking_data(book_id int auto_increment not null primary key,
    gas_type varchar(20),
    location varchar(20) not null,
    cust_email varchar(40) not null,
    contact bigint not null,
    status varchar(20) null default "Pending",
    book_time date,
    delivery_date DATE,
    )'''
    cursor.execute(sql)
    
except Error as e:
    print("Error:",e)

# *********************** Customer Create Account Activity ****************************************

def Register(m):
    try:
        cursor=con.cursor()
        Register_Query = "insert into customer(cust_name,Addhar_card_no,cust_Email,cust_address,cust_gas_type,cust_contact,cust_Password)values(%s,%s,%s,%s,%s,%s,%s);"
    
        cursor.execute(Register_Query,m)
        con.commit()
        print("\n ----------- Account Created Successflly -------------\n")
    except Error as er:
        #print("\n ------------- Account Not Created -------------\n")
        print(er)    
        
    

#******************************** Admin Table Activity ********************************************

try:
    cursor =con.cursor()
    Admin_query = 'create table if not exists admin(Email text, Password text)'
    cursor.execute(Admin_query)
    con.commit()

except Error as er:
    print(er)



#***************************************************************************************
def Admin():
    cursor = con.cursor()
    insert_query = 'insert into admin(Email,Password) values(%s,%s);'
    cursor.execute(insert_query)
    con.commit()

# ********************************* Admin Login *************************************

def admin_Login(Email,Password):
    cursor = con.cursor()
    login_query=" select * from admin where Email = %s and Password = %s;"
    data = (Email,Password)

 
    cursor.execute(login_query,data)
    s = cursor.fetchone()
    try:
        if s[0] == Email:
            if s [1] == Password:
                return True
            
    except:
        print('er')



# *************************   User Login    *****************************************

def customer_login(Email,Password):
    cursor = con.cursor()
    login_query = "select * from customer where cust_Email = %s and cust_Password = %s;"
    data = (Email,Password)
    cursor.execute(login_query,data)
    s = cursor.fetchone()
    # return s

    try:
        if s[3] == Email:
            if s[7] == Password:
                return True
    except:
        return " Invalid Email-id or Password "
    


# ****************************** Gas Booking Table Activity *********************************
'''
try:
    cursor =con.cursor()
    Booking_query = 'create table if not exists Gas_booking(booking_id int primary key auto_increment,booking_date datetime,Delivery_date date,cust_id int,Gas_id int, foreign key (cust_id) references customer(cust_id),foreign key(gas_id) references gas(gas_id));'
    cursor.execute(Booking_query)

except Error as er:
    print(er)

   

try:
    cursor =con.cursor()
    Booking_query = 'create table if not exists Gas_booking(booking_id int primary key auto_increment,booking_date datetime,Delivery_date date,cust_id int,Gas_id int, foreign key (cust_id) references customer(cust_id),foreign key(gas_id) references gas(gas_id));'
    cursor.execute(Booking_query)

except Error as er:
    print(er)



# ---------------------------- Gas Booking Data Insert ----------------------------


def insert_booking(email,gas_id):
    cursor = con.cursor()
    booking =f'insert into gas_booking(booking_date,Delivery_date,cust_id,Gas_id) values(curdate(),(curdate()+2),(select cust_id from customer where cust_Email="{email}"),"{gas_id}");'
    data = (email,gas_id)
    cursor.execute(booking,(data))
    con.commit()



# -------------------------------- Booking Show Data --------------------------------------------

def show_status():
    try:
        status = 'select gas_booking.Gas_id,gas_booking.cust_id,cust_name,cust_address,cust_contact,gas_booking.booking_id,booking_date,Delivery_date from gas_booking inner join customer on gas_booking.cust_id=customer.cust_id inner join gas on gas_booking.Gas_id=gas.Gas_id;'
        cursor.execute(status)
        data=cursor.fetchone()
        for row in data:
            for col in data:
                print(row,end=' ')
            print()

        if data == True:
            print(f'There is no Customer Data {show_status}')

        else:
            print(data)

            


    except Error as er:
        print('something Went Wrong')
        print(er)

        '''
    

#*********************************  Gas Table *******************************************

try:
    cursor =con.cursor()
    Gas_Query = 'create table if not exists Gas(Gas_id int primary key auto_increment,Gas_Type varchar(10))';
    cursor.execute(Gas_Query)
    con.commit()

except Error as er:
    print(er)






# ---------------------------  Gas Coonection ---------------------------------

def connection():
    cursor = con.cursor()
    q = 'select booking_data.book_id,cust_name,cust_address,cust_gas_type from booking_data inner join customer;'
    cursor.execute(q)
    bd = cursor.fetchall()
    for i in bd:
        record = pd.DataFrame(bd,columns=['book_id','cust_name','cust_address','cust_gas_type'])
        pd.set_option('display.colheader_justify','center')
        pd.set_option('display.width',None)

        if record.empty == True:
            print(f'There is no Connection Data {connection}')

        else:
            print(record)
            break
        

        


#**************************** User Information Data ***************************8

def Customer_activity():
    c = 'select * from customer'
    cursor.execute(c)
    result = cursor.fetchall()

    for i in result:
       ''' 
        print('cust_id :',i[0])
        print('cust_name :',i[1])
        print('cust_Email :',i[2])
        print('cust_address :',i[3])
        print('cust_gas_type :',i[4])
        print('cust_contact :',i[5])
        print('cust_Password :',i[6])

        print('\n________________________________________\n')
'''
        
    record = pd.DataFrame(result,columns=['cust_id','cust_name','Aadharcard','cust_Email','cust_address','cust_gas_type','cust_contact','cust_Password'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)

    if record.empty == True:
        print(f'There is no Customer Data {Customer_activity}')

    else:
        print(record)
        
        

            

            
        
# --------------------------------- UPDATE PROFILE CUSTOMER --------------------------------------

def update_profile(Email,Address,Contact,Password,id):
    cursor = con.cursor()
    u = "update customer set cust_Email = %s, cust_address = %s, cust_contact = %s, cust_Password =%s where cust_id = %s"
    
    new = (Email,Address,Contact,Password,id)
    cursor.execute(u,new)
    con.commit()



# ----------------------------------- DELIVERY STATUS -------------------------------------------------

def delivery_status():
    try:
        #d = 'select gas_booking.cust_id,cust_name,cust_address,gas_booking.booking_date,Delivery_date from gas_booking inner join customer;'
        d = 'select booking_data.book_id,cust_name,cust_address,booking_data.status,book_time,delivery_date from booking_data inner join customer;'
        cursor.execute(d)
        k = cursor.fetchall()
        for i in k:
            record = pd.DataFrame(k,columns=['book_id','cust_name','cust_address','status','book_time','delivery_date'])
            pd.set_option('display.colheader_justify','center')
            pd.set_option('display.width',None)

            if record.empty == True:
                print(f'There is no your Data {delivery_status}')
                break

        else:
            print(record)
            
            
            
            

            
        
    except Error as er:
        print('Something Went Wrong')
        print(er)
        



# ---------------------- Select Gas Type ------------------------------------

def selectGas(gas):
    if gas == "HP":
        return "HP"
    elif gas == "BharatGAS":
        return "BharatGAS"
    else:
        pass


        


'''create table if not exists booking_data(book_id int auto_increment not null primary key,
    gas_type varchar(20),
    location varchar(20) not null,
    cust_email varchar(40) not null,
    contact bigint not null,
    status varchar(20) null default "Pending",
    book_time datetime null
    )'''

# ------------------------------------ Inserted Booking Data ---------------------------------------------

def insert_booking_data(gas_type,location,cust_email,contact):
    try:
        
        sql = 'insert into booking_data(gas_type,location,cust_email,contact,book_time,delivery_date) values (%s,%s,%s,%s,current_timestamp(),(current_date() + interval 2 day));'
        data = (gas_type,location,cust_email,contact)
        cursor.execute(sql,data)
        con.commit()
        return True
    except Error as e:
        print("NOT INSERTED",e)


    
# --------------------------------------- Find Emall To Login Book The Gas  ----------------------------------



def find_gas_name(id):
    try:
        sql = 'select * from gas where Gas_id=%s'
        cursor.execute(sql,(id,))
        x = cursor.fetchone()
        return x[1]
    except:
        return "Wrong Input"
        
def find_user_data(email):
    try:
        sql = 'select * from customer where cust_Email=%s'
        cursor.execute(sql,(email,))
        data = cursor.fetchone()
        
        yield data
    except Error as e:
        print("Error",e)


# ------------------------------------------- Booking Data -------------------------------------------------

def your_booking(email):
    sql='''select * from booking_data where  cust_email=%s'''
    data = (email,)
    cursor.execute(sql,data)
    x = cursor.fetchall()
    for i in x:
        record = pd.DataFrame(x,columns=["book_id","gas_type","location","cust_email","contact","status","book_time","delivery_date"])
        pd.set_option('display.colheader_justify','center')
        pd.set_option('display.width',None)

        if record.empty == True:
            print(f'There is no your Data {your_booking}')

        else:
            print(record)
            



# ------------------------------------ Cancel Booking -------------------------------------------------------          

        

def cancel_booking(booking_id,email):
    try:
        sql = '''delete from booking_data where book_id=%s && status='Pending' && cust_email=%s'''
        cursor.execute(sql,(booking_id,email))
        con.commit()
        return True
    except:
        print("")

        
def show_bookings():
    
    sql = '''select * from booking_data'''
    cursor.execute(sql)
    x = cursor.fetchall()

    for i in x:
   
        record = pd.DataFrame(x,columns=['book_id','gas_type','location','cust_email','contact','status','book_time','delivery_date'])
        pd.set_option('display.colheader_justify','center')
        pd.set_option('display.width',None)

        if record.empty == True:
            print(f'There is no Booking Data {show_bookings}')

        else:
            print(record)
            break

        

            '''
         return x
    except:
        print("show Booking Error")
   
    
    myTable1= PrettyTable(["ID","Type","location","Email","contact","status","time"])
    for i in x:
    myTable1.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
    print(myTable1)
    

def gas():
    
    sql = 'select booking_data.gas_type,cust_name,cust_address from booking_data inner join customer;'
    cursor.execute(sql)
    x = cursor.fetchall()

    for i in x:
   
        record = pd.DataFrame(x,columns=['gas_type','cust_name','cust_address'])
        pd.set_option('display.colheader_justify','center')
        pd.set_option('display.width',None)

        if record.empty == True:
            print(f'There is no Booking Data {gas}')

        else:
            print(record)

            '''

# ----------------------------------------------- Delete user Data ------------------------------------------------

def customer_delete():
    
    user = input('Enter User Id :')
    sql = 'delete from customer where cust_id=%s'
    data = (user,)
    cursor.execute(sql,data)
    con.commit()
    print()
    print('\n ------------- User Data Deleted Sucessfully ---------------\n')
       

# --------------------------------------- Update Delivery Data -----------------------------------------------

def modify_delivery():
    book_id = input('Enter Book id :')
    delivery = input('Enter New Delivery date :')
    sql = 'update booking_data set delivery_date = %s where book_id =%s'
    data = (book_id,delivery)
    cursor.execute(sql,data)
    con.commit()
    print()
    print('\n --------------- Delivery Date Updated Sucessfully ------------------------\n')


# -------------------------------------- Delete Delivery Data --------------------------------------



def delivery_delete():
    
    user = input('Enter book Id :')
    sql = 'delete from booking_data where book_id=%s'
    data = (user,)
    cursor.execute(sql,data)
    con.commit()
    print()
    print('\n ------------- User Data Deleted Sucessfully ---------------\n')





    
            