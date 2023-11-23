import database as db
from model import customer,Admin
from Requirement import valiadation
import maskpass
from datetime import date
#from prettytable import PrettyTable




print('\n______________ Welcome To The Online Gas Cylinder Booking Management System _____________________\n')

while True:

    #print('\n___________ Welcome to the online Gas Booking Management system _______________\n,')

    print('1 - Create User Account ')
    print('2 - Login ')
    print('3 - Exit')

    choice = input('Enter Your Choice :')

    if choice =="1":
        print('\n__________ < Create User Account > ____________\n')

        
        while True:
            Name = input('Enter Your Name :')
            if valiadation.NameValidation(Name):
                break
            else:
                print('\n --------- Invalid Name ----------- \n')
        while True:
            addhar1 = input("Enter Your Addhar Card No:")
            break
            #if valiadation.addharValidation(addhar):
                
            #else:
                #print("----------------- Invalid Addhar Card NO -------------")

        while True:
            Email = input('Enter Your Email Id :')
            if valiadation.EmailValidation(Email):
                break
            else:
                print('\n -------------- Invalid Email-Id --------------- \n')

        while True:
            Address = input('Enter Your Address :')
            break
        while True:
            print("1 -> HP\n2 -> BharatGAS")
            Gas_Type = input('Enter Your Gas Company Name :')
            x = db.selectGas(Gas_Type)
            if x == "HP" or "BharatGAS":
                break
            else:
                print("Invalid Input")
                continue
            
                
                    
        while True:
            Contact = input('Enter Your Contact Number :')
            if valiadation.ContactValidation(Contact):
                break
            else:
                print('\n ------------- Invalid Contact Number ----------------- \n')
        
        while True:
            Password = input ('Enter Your Password :')
            Confirm_Password = maskpass.askpass('Enter Confirm Password :',mask="*")

            if valiadation.Passwordvalidation(Password,Confirm_Password) == True:
                break
            else:
                print('\n ------------- Invalid Password -----------\n')

        m = (Name,addhar1,Email,Address,x,Contact,Password)
        y = db.Register(m)
           
        

        
        
    
# ----------------------- Admin And Customer Login Section -------------------------

    elif choice =="2":
        print('\n_______________ < Login Section > ________________\n')

        while True:
            print('1- Admin Login')
            print('2- User Login')
            print('3- Back')

            choice = input(' Enter Your Login Choice : ')

# ------------------------------ Admin Login2 ---------------------------------------------
            
            if choice =="1":
                
                print('\n__________  < Admin Login Section > ____________\n')

                
                Email = input('Enter Your Email Id :')
                Password = maskpass.askpass('Enter Your Password :',mask="*")
                    
                data = db.admin_Login(Email,Password)
                
                if data == True:
                    print('\n -------------- * Admin Login Sucessfully * ------------------\n')

# ------------------------- Admin Handle This Operation Part ---- ----------------
                
                while True:

                        print('\n_________________< Admin Choice > ______________\n')

                        
                        print(' 1 - Check Connection Type ')
                        print(' 2 - View User Information')
                        print(' 3 - Booking Status')
                        print(' 4 - Delievery Status')
                        print(' 5 - Exit')
                       
                        choice = input('Enter Your Login Choice :')

                       

                        if choice == '1':
                             print("\n ________ < Gas Connection Activity > ___________ \n")

                             q=db.connection()

                            

# ------------------------- Admin Check Customer Data ----------------------------------

                        elif choice == '2':

                            while True:

                                print('\n________ < User Activity > __________\n')

                            

                                print(' 1 - User data ')
                                print(' 2 - Remove User')
                                print(' 3 - Back To Admin Page')

                                ch = input('Enter Your Choice :')

                                if ch == '1':

                                    print('\n ----------- User Information -----------------\n')

                                    db.Customer_activity()
                                elif ch == '2':
                                    print('\n ------------ Remove User --------------\n')

                                    

                                    sql = db.customer_delete()
                                        

    

                                elif ch =='3':
                                    print('\n ---------------- Back To Admin Page -----------------\n')
                                    break
                                    
                                else:
                                    print('\n ------------------- Invalid Choice --------------------\n')


                        elif choice == '3':
                            print("\n ------------ Booking Activity --------------\n")
                            x = db.show_bookings()

                            '''
                            myTable1= PrettyTable(["ID","Type","location","Email","contact","status","time"])
                            for i in x:
                                myTable1.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
                            print(myTable1)
                            '''



                        elif choice == '4':

                            while True:

                                print('\n --------------------- Delivery Status -----------------\n')

                                print('1 - Delivery Data')
                                print('2 - Delete Delivery Data')
                                print('3 - Back To Admin Page')

                                ch = input('Enter Your Choice :')

                                if ch == "1":
                                    print('\n ------------- Delivery Data ---------------')

                                    d = db.delivery_status()

                                elif ch == "2":
                                    print('\n --------------------- Delete Delivery Data --------------------\n')

                                    sql = db.delivery_delete()

                                elif ch == "3":
                                    print('\n -------------------- Back To Admin Page ------------------------\n')
                                    break

                                else:
                                    print('\n-------------------------- Invalid Choice -----------------------\n')

                               
                        elif choice == '5':
                            print("\n -------------- Back in Login Page ------------- \n")
                            break
                            

                        else:
                            print('\n________________ <<<<<< Invalid Choice >>>>>> ___________________\n')

                else:

                    print("\n <<<<<< Admin Email or Password Wrong >>>>>>\n")


                    
# ------------------------------- Customer Login -----------------------------------------


            elif choice =="2":

                print('\n__________  < Customer Login Section > ____________\n')

                
                Email = input('Enter Your Email id :')
                Password = maskpass.askpass('Enter Your Password :',mask="*")
                data = db.customer_login(Email,Password)
                if data == True:
                    print('\n --------------- * User Login Sucessfully * ----------------\n')

# ------------------------- Customer Handle This Operations --------------------------

                    while True:

                        print('\n_________________< User Choice > ______________\n')

                        print(' 1 - Book Gas')
                        print(' 2 - Checking Booking status ')
                        print(' 3 - Update Profile ')
                        print(' 4 - Cancel Booking')
                        print(' 5 - Back in Login Page ')
                        choice = input('Enter Your Login Choice :')

                        if choice == "1":

# ---------------------- Customer Gas Booking Point Area ---------------------------

                            print('\n__________ Gas Booking _________\n')
                    
                            ch = input("You Want to order YES(1)|NO(2):")

                            if ch == "1":
                                x = db.find_user_data(Email)
                                data = []
                                for i in x:
                                    for j in i:
                                        data.append(j)
                                if db.insert_booking_data(data[5],data[4],Email,data[6]):
                                    #2
                                    # db.insert_booking_data()
                                    print("\n<-------- Gas Book Succssfully -------->\n")
                                else:
                                    print("\n ---------------- Sorry You Have Not Book Gas ------------\n")
                                
                                #db.insert_booking(Email,gas_id)
                                #print('\n -------- Gas Booking Sucessfully --------- \n')
                                #insert_booking_data(gas_type,location,cust_email,contact):

                                
                        



                            elif ch== "2":
                                print('\n ------ Sorry You have Not Book Gas -------\n')
                                break

                            else:
                                ("\n ---------- Invalid Choice Please Enter 'YES' or 'NO' -------------\n")

                                


                    
# ---------------------------------------  Booking Status ------------------------------------------ 


                        elif choice == "2":
                            print('\n --------- Checking Booking Status ------------ \n')
                            x = db.your_booking(Email)
                            
                            '''
                            myTable = PrettyTable(["booking ID","Type","status","book Time","delivery date"])
                            for i in x:
                                
                                myTable.add_row([i[0],i[1],i[5],i[6],i[7]])
                            print(myTable)
                            '''

                            

                            

# ------------------- Customer Update That Your Profile area ---------------------------

                        elif choice == '3':
                            print('\n_________ < Update Profile > _________\n')

                            
                            
                            id=input("Enter id to modify :")

                            while True:
                                Email = input('set New Email id :')
                                if valiadation.EmailValidation(Email):
                                     break
                                else:
                                    print('\n --------- Invalid Email-Id-------- \n')

                            Address = input('update New Address :')

                            while True:
                                Contact = input('Enter Your New Contact Number :')
                                if valiadation.ContactValidation(Contact):
                                    break
                                else:
                                    print('\n ------------- Invalid Contact Number ----------------- \n')
        
                            Password = input('Set New Password :')

                            
                            new = db.update_profile(Email,Address,Contact,Password,id)
                            #new = [Email,Address,Contact,Password]
                            #data = db.update_profile(new)
                            print('\n ------- Customer Data Updated Sucessfully ---------\n')



                            

# ----------------------------- Back To Login Page -------------------------------------


                        elif choice =="4":

                            print('\n ---------------- Cancel Booking Section ----------\n')
                            book1_id = int(input("Enter Booking ID:"))


                            if db.cancel_booking(book1_id,Email):
                                print("\n-------------- booking cancel -------------")
                            else:
                                print("Invalid Details")

                        elif choice == "5":
                            print('\n--------- Back in Login Page ------------\n')
                            break
            

                        else:
                            print('\n_______ <<<<<< Invalid Choice >>>>>> ___________')
                        
                else:
                    print('\n__________________ <<<<<< Invalid customer Details >>>>>> ___________________\n')


# ------------------------ Back To Home Page Area Point -------------------------------

            elif choice =="3":
               print('\n -------------------- Back To Home Page -------------\n')
               break

            else:
                print('\n__________________ < Invalid Choice > ___________________\n')


    elif choice == '3':
        print('\n______________*** Thank You To Visit Us App ***____________\n')
        break

    else:
         print('\n_______ <<<<<< Invalid Choice >>>>>> ___________\n')







