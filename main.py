# Atm Exercise to develop all functionalities of ATM Machine including some additonal features
import os.path
import os
import json
from datetime import datetime
from os import system, name
class Admin:
    def create_user(self, name, cnic, age, pswrd, addr, dep ):
        self.name = name
        self.cnic = cnic
        self.age = age
        self.addr = addr
        self.pswrd = pswrd
        self.dep = dep
        # your cnic is your account number, as to make it unique
        print("Congratulations, Your Account has been created Successfully...")
        print("Please remind it,Your CNIC is you bank Account Number.")
        print("Use your CNIC and Password for Login In Purpose.")
        # now creating a dictionary in the JSON Format.So that to make a file for the user
        directory = f"Accounts/{cnic}.json"

        # making a dictionary, so that to use it in JSON file
        user_dict = {
            "Name": name,
            "CNIC": cnic,
            "AGE": age,
            "Address": addr,
            "Balance": dep,
            "password": pswrd,
        }
        # Serializing json
        json_object = json.dumps(user_dict, indent=4)

        # Writing to sample.json
        file_A = open(directory, "w")
        file_A.write(json_object)

    def set_user_profile(self):
        name = str(input("Enter your Full Name: "))
        c_id = str(input("Enter your CNIC: "))

        u_age = int(input("Enter your Age: "))
        addr = str(input("Enter your Permanent address: "))

        dummy_p1 = str(input("Enter the Password for your account carefully: "))
        dummy_p2 = str(input("Enter the Password  Again : "))
        while dummy_p1 != dummy_p2:
            print("Both Passwords arent same.Please Enter Again ")
            dummy_p1 = str(input("Enter the Password for your account carefully: "))
            dummy_p2 = str(input("Enter the Password  Again : "))
        paswrd = dummy_p1
        print("If you want to deposit any amount Now, Then Enter Amount otherwise Enter zero.")
        deposit = int(input("Enter the Amount: "))
        while deposit<0:
            deposit = int(input("Please enter the positive Amount: "))

        self.create_user(name, c_id, u_age, paswrd, addr, deposit)

    # @staticmethod
    def view_user_details(self):
        dummy = str(input("Enter the CNIC OF User to view his Account Details: "))
        file_name = "Accounts/{}.json".format(dummy)
        with open(file_name, 'r') as f2:
            data = f2.read()
            print(data)

    def admin_profile(self):
        admin_dict = {
            "admin": "admin123"
        }
        print("\tPlease Enter the credentials to Access Admin Panel.")
        a_id = str(input("Enter the Administrative Username: "))
        a_key = str(input("Enter the Administrative Password: "))
        if a_id in admin_dict and a_key == admin_dict[a_id]:
            print("Login Successfully...")
            print("Choose the Option Carefully.")
            print("1.Create new Admin Profile \n2.Update admin Profile \n3.Delete Admin Profile \n 4.View Admins \n5.Back to Main Menu \n6.For Exit ")

            opt = 1000

            while opt != 0:
                opt = int(input("Enter the option number: "))
                # Create new admin
                if opt == 1:
                    new_admin_name = str(input("Enter the Username: "))
                    new_admin_pswrd = str(input("Enter the Password: "))
                    admin_dict.update({new_admin_name: new_admin_pswrd})
                    print("Admin Add Successfully.")
                    # opt = int(input("Enter the option number: "))

                # update admin profile
                elif opt == 2:
                    a_id = str(input("Enter the Username of that admin to update its password:"))
                    a_key = str(input("Enter the new Password for this Admin Profile: "))
                    if a_id in admin_dict:
                        admin_dict[a_id] = a_key
                        print("Password of Admin {} updated successfully. ".format(a_id))
                    else:
                        print("This Username is not an admin...")

                # delete admin profile
                elif opt == 3:
                    a_id = str(input("Enter the Username of the admin you want to delete:"))
                    if a_id in admin_dict:
                        del admin_dict[a_id]
                        print("{} (Admin) profile deleted successfully.".format(a_id))
                    else:
                        print("Sorry, {} is not an Admin".format(a_id))
                        pass
                # View Admin Profiles
                elif opt == 4:
                    print(admin_dict)

                elif opt == 5:
                    # os.system('clear')
                    return "main_menu"
                elif opt == 6:
                    # os.system('clear')
                    exit()
             
    def del_customer(self,num):
        self.num = num
        if os.path.exists("Accounts/"+str(num)+'.json'):
            os.remove("Accounts/"+str(num)+'.json')
            print("Account of ID: {0} deleted successfully.".format(num))


        else:
            print(" Account Records of {0}  does not exist".format(num))



    def obj_to_json(self, dict,fname):
        self.dict = dict
        self.fname = fname

        #converting dict to json
        #file_path = r'./Accounts/{}.json'.format(fname)
        with open(fname, "w") as outfile:
            json.dump(dict, outfile, indent=4)

    def updatePswrd(self,acc,pswrd):
        file_path = r'./Accounts/{}.json'.format(acc)
        # file_name = user_id
        flag = os.path.isfile(file_path)
        if flag:
            # print(f'The file {file_path} exists')
            with open(file_path) as json_file:
                data = json.load(json_file)

                data["password"] = pswrd
                json_object = json.dumps(data, indent=6)

                with open(file_path, "w") as outfile:
                    json.dump(data, outfile, indent=4)

                print("password updated successfully...")


class user:
    def obj_to_json(self, dict,fname):
        self.dict = dict
        self.fname = fname
        #converting dict to json
        with open(fname, "w") as outfile:
            json.dump(dict, outfile, indent=4)


    def user_login(self,  user_id, user_pswrd):
        # dir_path = r'Accounts/{}'.format(user_id)
        file_path = r'./Accounts/{}.json'.format(user_id)

        flag = os.path.isfile(file_path)
        if flag:
            with open(file_path) as json_file:
                data = json.load(json_file)
                json_file.close()
                print(data)
                if data["password"] != user_pswrd:
                    print("Incorrect Credentials.")
                if data["password"] == user_pswrd:
                    print("Login Successful...")
                    print("\t\t\t\t\t --Customer Menu---")

                    option = 1000
                    while option != 0:
                        print("\n1.View Profile \n2.Perform Transaction \n3.Deposit Money\n4.Withdraw Money ")
                        print("0. Exit Program")
                        option = (int(input("Enter the Option: ")))

                        if option == 1:
                            print("\t\t\t\t ***- Profile Data -***")
                            # displaying data in better format
                            for key, value in data.items():
                                print(key, ' : ', value)
                        elif option == 2:
                            amount = int(input("Enter the Amount you want to transfer: "))
                            while amount < 1:
                                amount = int(input("Enter the Positive Amount Again."))
                            sender_acc = user_id
                            rec_acc = int(input(("Enter the Receiver Account Number: ")))
                            rec_acc = str(rec_acc)

                            try:
                                file_path2 = r'./Accounts/{}.json'.format(rec_acc)
                                flag = os.path.isfile(file_path2)
                                if flag:
                                    with open(file_path2) as json_file:
                                        data2 = json.load(json_file)
                                        json_file.close()
                                        print("\t\t\t---Sender's Account Profile---")
                                        print(data2)

                            except:
                            # file_name = user_id
                                print("File not found")
                                break
                            else:
                                if amount <= data["balance"]:
                                    real_amount = amount
                                    data["balance"] = data["balance"] - amount
                                    data2["balance"] = data2["balance"] + amount
                                    self.obj_to_json(data, file_path )
                                    self.obj_to_json(data2, file_path2)


                                    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                                    # saving the transaction in transactions
                                    trans_dict = {
                                        "CNIC": data["cnic"],
                                        "Transaction Amount": real_amount,
                                        "Time": dt_string,
                                        'Receiver Account No': data2["cnic"],
                                        "Remaining": data["balance"]
                                    }

                                    os.remove(file_path)
                                    with open(file_path, 'a') as f:
                                        json.dump(data, f, indent=4)
                                        print("Your Account has been updated again")
                                        json_object = json.dumps(trans_dict, indent=6)
                                        file_a = open("./Accounts/Transactions.json", "a")
                                        # file_a.write(data )
                                        # converting old record again
                                        # file_a.write(str(data))
                                        file_a.write("\n\n ")
                                        file_a.write((json_object + ","))
                                        file_a.close()
                                        # file_a.write(json_object)
                                        print("Transaction is saved for records.")

                                else:
                                    print("Insufficent amount in your account")
                        elif option == 3:
                            amount = int(input("Enter the Amount you want  to deposit: "))
                            while(amount<0):
                                amount=int(input("You enter negtive character.Please enter deposit amount again:  "))
                            data["balance"] += amount
                            print("Amount has been added to your amount")
                            print("Your New Balance is:")
                            print(data["balance"])
                            self.obj_to_json(data, file_path)

                        elif option == 4:
                            amount = int(input("Enter the Amount you want  to Withdraw: "))
                            if amount <= data["balance"]:
                                real_amount = amount
                                data["balance"] = data["balance"] - amount
                                self.obj_to_json(data, file_path)
                        elif option == 0:
                            exit()
        else:
            print(f'The file {file_path} does not exist')



# main file
main_menu = True
while main_menu==True:

    print("\n\n\n\t\t\t\t\t****   ATM MENU   *****")
    menu_opt = int(input("1.For Admin Panel \n2.For User Panel \nEnter the Option Number: "))

    while menu_opt>0 and menu_opt <3:


        if menu_opt == 1:
            admin = Admin()

            menu_opt =1000
            while menu_opt != 1234:
                print("\t\t-----Admin Panel-----\n1.Create Customer Profile\n2.View Customer Profile\n3.Access Admin Functionalities  \n4.Delete Customer "
                      "\n5.Edit User Account Password \n6.For Previous Menu "
                      "\n7.For Exit the Program  ")
                menu_opt = int(input("Enter the option: "))
                if menu_opt == 1:
                    admin.set_user_profile()
                    print("")
                elif menu_opt == 2:
                    admin.view_user_details()
                    print("Customer Profile show successfully...")
                    _ = system('clear')
                elif menu_opt == 3:
                    check = admin.admin_profile()
                    if check=="main_menu":
                        main_menu = True

                elif menu_opt == 4:
                    account_num = int(input("Enter th Account number that you want to delete: "))
                    admin.del_customer(account_num)
                elif menu_opt == 5:
                    a_id = str(input("Enter the Account Number of that User to update its password:"))
                    # a_prevKey =str(input("Enter the old Password for this User Profile: "))
                    a_key = str(input("Enter the new Password for this User Profile: "))
                    admin.updatePswrd(a_id, a_key)

                elif menu_opt == 6:
                    menu_opt=1234
                    main_menu = True
                elif menu_opt == 7:
                    main_menu = False
                    exit()

        elif menu_opt ==2:
            person = user()
            print("\t\t---Customer Login---")
            u_name = str(input("Enter the Username of Customer: "))
            u_pass = str(input("Enter the Password of Customer: "))
            person.user_login(u_name, u_pass)








