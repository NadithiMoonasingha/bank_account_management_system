# backend/bank_logic.py
from datetime import datetime

customers = []


def validate_account_number(acc_no):
    return acc_no.isdigit() and len(acc_no) == 10


def validate_nic(nic):
    return isinstance(nic, str) and len(nic) == 10


def validate_phone_number(phone_no):
    return isinstance(phone_no, str) and len(phone_no) == 10


def validate_f_name(name):
    return isinstance(name, str) and len(name) <= 10


def validate_l_name(name):
    return isinstance(name, str) and len(name) <= 15


def validate_birth_date(dob):
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_address(address):
    return isinstance(address, str) and len(address) <= 15


def find_customer_by_account(acc_no):
    return next((customer for customer in customers if customer["acc_no"] == acc_no), None)


def find_customer_by_nic(nic):
    return next((customer for customer in customers if customer["nic"] == nic), None)


def add_customer(data):
    acc_no = data.get("acc_no", "")
    nic = data.get("nic", "")
    f_name = data.get("f_name", "")
    l_name = data.get("l_name", "")
    dob = data.get("dob", "")
    address = data.get("address", "")
    phone_no = data.get("phone_no", "")

    if not validate_account_number(acc_no):
        return {"success": False, "message": "Invalid account number. Must be 10 digits."}

    if find_customer_by_account(acc_no):
        return {"success": False, "message": "A customer with this account number already exists."}

    if not validate_nic(nic):
        return {"success": False, "message": "Invalid NIC. Must be 10 characters."}

    if find_customer_by_nic(nic):
        return {"success": False, "message": "A customer with this NIC already exists."}

    if not validate_f_name(f_name):
        return {"success": False, "message": "Invalid first name. Maximum 10 characters."}

    if not validate_l_name(l_name):
        return {"success": False, "message": "Invalid last name. Maximum 15 characters."}

    if not validate_birth_date(dob):
        return {"success": False, "message": "Invalid birth date. Use YYYY-MM-DD format."}

    if not validate_address(address):
        return {"success": False, "message": "Invalid address. Maximum 15 characters."}

    if not validate_phone_number(phone_no):
        return {"success": False, "message": "Invalid phone number. Must be 10 digits."}

    if len(customers) >= 5:
        return {"success": False, "message": "Customer limit reached."}

    new_customer = {
        "acc_no": acc_no,
        "nic": nic,
        "f_name": f_name,
        "l_name": l_name,
        "dob": dob,
        "address": address,
        "phone_no": phone_no,
        "balance": 0
    }

    customers.append(new_customer)

    return {
        "success": True,
        "message": "Customer added successfully.",
        "customer": new_customer
    }


def get_all_customers():
    return customers


def get_customer(acc_no):
    customer = find_customer_by_account(acc_no)

    if not customer:
        return {"success": False, "message": "Customer not found."}

    return {"success": True, "customer": customer}


def deposit_money(acc_no, amount):
    customer = find_customer_by_account(acc_no)

    if not customer:
        return {"success": False, "message": "Customer not found."}

    try:
        amount = float(amount)
    except ValueError:
        return {"success": False, "message": "Amount must be a number."}

    if amount <= 0:
        return {"success": False, "message": "Deposit amount must be positive."}

    if amount > 5000000:
        return {"success": False, "message": "Deposit amount exceeds maximum limit of 5,000,000."}

    customer["balance"] += amount

    return {
        "success": True,
        "message": "Deposit successful.",
        "balance": customer["balance"]
    }


def withdraw_money(acc_no, amount):
    customer = find_customer_by_account(acc_no)

    if not customer:
        return {"success": False, "message": "Customer not found."}

    try:
        amount = float(amount)
    except ValueError:
        return {"success": False, "message": "Amount must be a number."}

    if amount <= 100:
        return {"success": False, "message": "Withdrawal amount must exceed 100."}

    if amount > 60000:
        return {"success": False, "message": "Withdrawal amount exceeds maximum limit of 60,000."}

    if customer["balance"] < amount:
        return {
            "success": False,
            "message": f"Insufficient balance. Current balance is {customer['balance']:.2f}."
        }

    customer["balance"] -= amount

    return {
        "success": True,
        "message": "Withdrawal successful.",
        "balance": customer["balance"]
    }


def update_customer(acc_no, data):
    customer = find_customer_by_account(acc_no)

    if not customer:
        return {"success": False, "message": "Customer not found."}

    if data.get("nic"):
        new_nic = data["nic"]
        existing = find_customer_by_nic(new_nic)

        if existing and existing["acc_no"] != acc_no:
            return {"success": False, "message": "A customer with this NIC already exists."}

        if not validate_nic(new_nic):
            return {"success": False, "message": "Invalid NIC."}

        customer["nic"] = new_nic

    if data.get("f_name"):
        if not validate_f_name(data["f_name"]):
            return {"success": False, "message": "Invalid first name."}
        customer["f_name"] = data["f_name"]

    if data.get("l_name"):
        if not validate_l_name(data["l_name"]):
            return {"success": False, "message": "Invalid last name."}
        customer["l_name"] = data["l_name"]

    if data.get("dob"):
        if not validate_birth_date(data["dob"]):
            return {"success": False, "message": "Invalid birth date."}
        customer["dob"] = data["dob"]

    if data.get("address"):
        if not validate_address(data["address"]):
            return {"success": False, "message": "Invalid address."}
        customer["address"] = data["address"]

    if data.get("phone_no"):
        if not validate_phone_number(data["phone_no"]):
            return {"success": False, "message": "Invalid phone number."}
        customer["phone_no"] = data["phone_no"]

    return {
        "success": True,
        "message": "Customer details updated successfully.",
        "customer": customer
    }