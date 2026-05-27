import { useEffect, useState } from "react";
import AddCustomer from "./Components/AddCustomer";
import Deposit from "./Components/Deposit";
import Withdraw from "./Components/Withdraw";
import UpdateCustomer from "./Components/UpdateCustomer";
import SearchCustomer from "./Components/SearchCustomer";
import DeleteCustomer from "./Components/DeleteCustomer";

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

  const totalBalance = customers.reduce(
    (total, customer) => total + Number(customer.balance),
    0
  );

  return (
    <div className="app">

      <header className="dashboard-header">
        <div>
          <h1>ABC Bank Management System</h1>
          <p>React frontend connected with Python Flask backend</p>
        </div>

        <div className="header-badge">Bank Dashboard</div>
      </header>

      <section className="summary-grid">
        <div className="summary-card">
          <h3>Total Customers</h3>
          <p>{customers.length}</p>
        </div>

        <div className="summary-card">
          <h3>Total Balance</h3>
          <p>Rs. {totalBalance}</p>
        </div>

        <div className="summary-card">
          <h3>System Status</h3>
          <p>Active</p>
        </div>
      </section>

      <section className="dashboard-grid">
        <div className="dashboard-card">
          <AddCustomer onCustomerAdded={fetchCustomers} />
        </div>

        <div className="dashboard-card">
          <Deposit onDepositSuccess={fetchCustomers} />
        </div>

        <div className="dashboard-card">
          <Withdraw onWithdrawSuccess={fetchCustomers} />
        </div>

        <div className="dashboard-card large-card">
          <UpdateCustomer onUpdateSuccess={fetchCustomers} />
        </div>

        <div className="dashboard-card">
          <SearchCustomer />
        </div>

        <div className="dashboard-card">
          <DeleteCustomer onDeleteSuccess={fetchCustomers} />
        </div>
      </section>

      <section className="customer-section">
        <h2>All Customers</h2>

        {customers.length === 0 ? (
          <p className="empty-text">No customers added yet.</p>
        ) : (
          <div className="customer-grid">
            {customers.map((customer) => (
              <div className="customer-card" key={customer.acc_no}>
                <h3>
                  {customer.f_name} {customer.l_name}
                </h3>

                <p>
                  <strong>Account Number:</strong> {customer.acc_no}
                </p>
                <p>
                  <strong>NIC:</strong> {customer.nic}
                </p>
                <p>
                  <strong>Date of Birth:</strong> {customer.dob}
                </p>
                <p>
                  <strong>Address:</strong> {customer.address}
                </p>
                <p>
                  <strong>Phone Number:</strong> {customer.phone_no}
                </p>

                <div className="balance-box">
                  Balance: Rs. {customer.balance}
                </div>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}

export default App;