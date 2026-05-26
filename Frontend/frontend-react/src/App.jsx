import { useEffect, useState } from "react";
import AddCustomer from "./Components/AddCustomer";
import Deposit from "./Components/Deposit";
import Withdraw from "./Components/Withdraw";
import UpdateCustomer from "./Components/UpdateCustomer";
import SearchCustomer from "./Components/SearchCustomer";

function App() {
  const [customers, setCustomers] = useState([]);

  function fetchCustomers() {
    fetch("http://127.0.0.1:5000/customers")
      .then((response) => response.json())
      .then((data) => setCustomers(data))
      .catch((error) => console.error("Error:", error));
  }

  useEffect(() => {
    fetchCustomers();
  }, []);

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>ABC Bank Management System</h1>
      <p>React frontend is connected to Python backend.</p>

      <AddCustomer onCustomerAdded={fetchCustomers} />
      <Deposit onDepositSuccess={fetchCustomers} />
      <Withdraw onWithdrawSuccess={fetchCustomers} />
      <UpdateCustomer onUpdateSuccess={fetchCustomers} />
      <SearchCustomer />

      <h2>Customers</h2>

      {customers.length === 0 ? (
        <p>No customers added yet.</p>
      ) : (
        <div>
          {customers.map((customer) => (
            <div
              key={customer.acc_no}
              style={{
                border: "1px solid #ccc",
                borderRadius: "8px",
                padding: "15px",
                marginBottom: "15px",
                backgroundColor: "white",
                width: "400px",
              }}
            >
              <h3>
                {customer.f_name} {customer.l_name}
              </h3>

              <p><strong>Account Number:</strong> {customer.acc_no}</p>
              <p><strong>NIC:</strong> {customer.nic}</p>
              <p><strong>Full Name:</strong> {customer.f_name} {customer.l_name}</p>
              <p><strong>Date of Birth:</strong> {customer.dob}</p>
              <p><strong>Address:</strong> {customer.address}</p>
              <p><strong>Phone Number:</strong> {customer.phone_no}</p>
              <p><strong>Balance:</strong> Rs. {customer.balance}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;