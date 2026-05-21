# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

from bank_logic import (
    add_customer,
    get_all_customers,
    get_customer,
    deposit_money,
    withdraw_money,
    update_customer
)

app = Flask(__name__)
CORS(app)


@app.route("/customers", methods=["GET"])
def customers():
    return jsonify(get_all_customers())


@app.route("/customers/<acc_no>", methods=["GET"])
def customer(acc_no):
    return jsonify(get_customer(acc_no))


@app.route("/customers", methods=["POST"])
def create_customer():
    data = request.json
    return jsonify(add_customer(data))


@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.json
    return jsonify(deposit_money(data["acc_no"], data["amount"]))


@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.json
    return jsonify(withdraw_money(data["acc_no"], data["amount"]))


@app.route("/customers/<acc_no>", methods=["PUT"])
def update(acc_no):
    data = request.json
    return jsonify(update_customer(acc_no, data))


if __name__ == "__main__":
    app.run(debug=True)