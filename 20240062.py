#Import Date and Time
from datetime import datetime

#Validate account number
def validate_account_number(acc_no):
    return acc_no.isdigit() and len(acc_no) == 10

#Validate NIC
def validate_nic(nic):
    return isinstance(nic, str) and len(nic) == 10

#Validate phone number
def validate_phone_number(phone_no):
    return isinstance(phone_no, str) and len(phone_no) == 10

#Validate the first name
def validate_f_name(name):
    return isinstance(name, str) and len(name) <= 10

#Validate the last name
def validate_l_name(name):
    return isinstance(name, str) and len(name) <= 15

#Validate birth date
def validate_birth_date(dob):
    try:
        datetime.strptime(dob, '%Y-%m-%d')
        return True
    except ValueError:
        return False

#Validate address
def validate_address(address):
    return isinstance(address,str) and len(address) <= 15

#Find customer by account number
def find_customer_by_account(customers, acc_no):
    return any(customer['acc_no'] == acc_no for customer in customers)

#Find customer by NIC
def find_customer_by_nic(customers, nic):
    return any(customer['nic'] == nic for customer in customers)

#Display customer details
def display_customer(customer):
    print(f"Account Number: {customer['acc_no']}")
    print(f"NIC: {customer['nic']}")
    print(f"Name: {customer['f_name']} {customer['l_name']}")
    print(f"Balance: {customer['balance']}")

#Add a new customer
def add_customer(customers):
#Repeates until the condition becomes true
    while True:
        acc_no = input("Bank Account Number: ")
        if validate_account_number(acc_no):
            if find_customer_by_account(customers, acc_no):
                print("A customer with this account number already exists. Please try again.")
            else:
                break
        else:
            print("Invalid account number! Must be 10 digits.")
#Repeates until the condition becomes true
    while True:
        nic = input("NIC: ")
        if validate_nic(nic):
            if find_customer_by_nic(customers, nic):
                print("A customer with this NIC already exists. Please try again.")
            else:
                break
        else:
            print("Invalid NIC!")
#Repeates until the condition becomes true
    while True:
        f_name = input("First Name: ")
        if validate_f_name(f_name):
            break
        else:
            print("Invalid first name! Must contain only letters.")
#Repeates until the condition becomes true
    while True:
        l_name = input("Last Name: ")
        if validate_l_name(l_name):
            break
        else:
            print("Invalid last name! Must contain only letters.")
#Repeates until the condition becomes true
    while True:
        dob = input("Birth Date (YYYY-MM-DD): ")
        if validate_birth_date(dob):
            break
        else:
            print("Invalid birth date! Must be in the format YYYY-MM-DD.")
#Repeates until the condition becomes true
    while True:
        address = input("Permanent Address: ")
        if validate_address(address):
            break
        else:
            print("Invalid Address. Maximum length is 15 characters")
#Repeates until the condition becomes true
    while True:
        phone_no = input("Phone Number: ")
        if validate_phone_number(phone_no):
            break
        else:
            print("Invalid phone number! Must be 10 characters.")
# Creat a new customer dictionary
    new_customer = {
        'acc_no': acc_no,
        'nic': nic,
        'f_name': f_name,
        'l_name': l_name,
        'dob': dob,
        'address': address,
        'phone_no': phone_no,
        'balance': 0
    }

    save_customer = input("Do you want to save this new customer? (yes/no): ").strip().lower()
    if save_customer == 'yes':
        if len(customers) <= 4:
            customers.append(new_customer)
            print("Customer added successfully!")
        else:
            print("Customer limit reached.")
    else:
        print("Customer not saved.")

#View details of a customer
def view_customer_details(customers):
#Loops until the condition becomes true
    while True:
        acc_no = input("Enter account number: ")
        customer = next((customer for customer in customers if customer['acc_no'] == acc_no), None)
        if customer:
            display_customer(customer)
        else:
            print("Customer not found!")

        view_another = input("Do you want to view details of another account? (yes/no): ").strip().lower()
        if view_another == 'no':
            break

#View details of all customers
def view_all_customers(customers):
    for customer in customers:
        display_customer(customer)
#Loops until the condition becomes true
    while True:
        update_details = input("Do you want to update any customer details? (yes/no): ").strip().lower()
        if update_details == 'yes':
            update_customer_details(customers)
            break
        elif update_details == 'no':
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

# Deposit money to an account
def deposit_money(customers):
#Loops until the condition becomes true
    while True:
        acc_no = input("Enter account number: ")
        customer = next((customer for customer in customers if customer['acc_no'] == acc_no), None)
        if customer:
            break
        else:
            print("Customer not found! Please try again.")
#Loops until the condition becomes true
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if 0 < amount <= 5000000:
                break
            elif amount > 5000000:
                print("Deposit amount exceeds maximum limit of 5,000,000. Please enter a smaller amount.")
            else:
                print("Deposit amount must be positive and not exceed 5,000,000!")
        except ValueError:
            print("Must be a number!")

    confirm_deposit = input("Do you want to save? (yes/no): ").strip().lower()
    if confirm_deposit == 'yes':
        customer['balance'] = customer['balance'] + amount
        print("Deposit successful!")
        print(f"New balance: {customer['balance']:.2f}")
    else:
        print("Deposit canceled.")

# Withdraw money from an account
def withdraw_money(customers):
#Loops until the condition becomes true
    while True:
        acc_no = input("Enter account number: ")
        customer = next((customer for customer in customers if customer['acc_no'] == acc_no), None)
        if customer:
            break
        else:
            print("Customer not found! Please try again.")
#Loops until the condition becomes true
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if 100 < amount <= 60000:
                if customer['balance'] >= amount:
                    break
                else:
                    print(f"Insufficient account balance! Your current balance is {customer['balance']:.2f}")
            elif amount > 60000:
                print("Withdrawal amount exceeds maximum limit of 60,000. Please enter a smaller amount.")
            elif amount<100:
                print("Withdrawal amount must exceed 100.Please enter a higher number.")
            else:
                print("Withdrawal amount must be positive and between 100 and 60,000!")
        except ValueError:
            print("Must be a number!")

    confirm_withdrawal = input("Do you want to save? (yes/no): ").strip().lower()
    if confirm_withdrawal == 'yes':
        customer['balance'] -=amount
        print(f"Withdrawal of {amount:.2f} successful!")
        print(f"New balance: {customer['balance']:.2f}")
    else:
        print("Withdrawal canceled!")

# Update customer details
def update_customer_details(customers):
#Loops until the condition becomes true
    while True:
        acc_no = input("Enter account number: ")
        customer = next((customer for customer in customers if customer['acc_no'] == acc_no), None)
        if customer:
            break
        else:
            print("Customer not found! Please try again.")

    nic = f_name = l_name = dob = address = phone_no = None
#Loops until the condition becomes true    
    while True:
        nic_input = input("NIC (Leave blank to keep current): ")
        if not nic_input:
            break
        if validate_nic(nic_input):
            if nic_input != customer['nic'] and find_customer_by_nic(customers, nic_input):
                print("A customer with this NIC already exists. Please try again.")
            else:
                nic = nic_input
                break
        else:
            print("Invalid NIC!")
#Loops until the condition becomes true
    while True:
        f_name_input = input("First Name (Leave blank to keep current): ")
        if not f_name_input or validate_f_name(f_name_input):
            f_name = f_name_input
            break
        else:
            print("Invalid first name! Must contain only letters.")
#Loops until the condition becomes true
    while True:
        l_name_input = input("Last Name (Leave blank to keep current): ")
        if not l_name_input or validate_l_name(l_name_input):
            l_name = l_name_input
            break
        else:
            print("Invalid last name! Must contain only letters.")
#Loops until the condition becomes true
    while True:
        dob_input = input("Birth Date (Leave blank to keep current): ")
        if not dob_input or validate_birth_date(dob_input):
            dob = dob_input
            break
        else:
            print("Invalid birth date! Must be in the format YYYY-MM-DD.")
#Loops until the condition becomes true
    while True:
        address_input = input("Permanent Address (Leave blank to keep current): ")
        if not address_input or validate_address(address_input):
            address = address_input
            break
        else:
            print("Invalid Address. Maximum length is 15 characters")
#Loops until the condition becomes true
    while True:
        phone_no_input = input("Phone Number (Leave blank to keep current): ")
        if not phone_no_input or validate_phone_number(phone_no_input):
            phone_no = phone_no_input
            break
        else:
            print("Invalid phone number! Must be 10 digits.")

    save_info = input("Do you want to save the updated information? (yes/no): ").strip().lower()
    if save_info == 'yes':
        if nic is not None: customer['nic'] = nic
        if f_name is not None: customer['f_name'] = f_name
        if l_name is not None: customer['l_name'] = l_name
        if dob is not None: customer['dob'] = dob
        if address is not None: customer['address'] = address
        if phone_no is not None: customer['phone_no'] = phone_no
        print("Customer details updated successfully!")
    else:
        print("Changes discarded.")

#Main menu
def main_menu():
    customers = []
    while True:
        print('''
                       ABC Bank Main Menu
1) Add a new customer
2) View details of a customer including his/her bank balance
3) View details of all the customers with their bank balances
4) Deposit money to a given account
5) Withdraw money from a given account
6) Update Customer Details
7) Exit
        ''')
        choice = input("Your Choice: ")

        if choice == '1':
            add_customer(customers)
        elif choice == '2':
            view_customer_details(customers)
        elif choice == '3':
            view_all_customers(customers)
        elif choice == '4':
            deposit_money(customers)
        elif choice == '5':
            withdraw_money(customers)
        elif choice == '6':
            update_customer_details(customers)
        elif choice == '7':
            print("Thank you for using ABC Bank Services")
            break
        else:
            print("Invalid choice! Please try again.")
#Call the main menu
main_menu()
