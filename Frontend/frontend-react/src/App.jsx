import { useEffect, useState } from "react";

function App() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/customers")
      .then((response) => response.json())
      .then((data) => setCustomers(data))
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>ABC Bank Management System</h1>
      <p>React frontend is connected to Python backend.</p>

      <h2>Customers</h2>

      {customers.length === 0 ? (
        <p>No customers added yet.</p>
      ) : (
        <ul>
          {customers.map((customer) => (
            <li key={customer.acc_no}>
              {customer.f_name} {customer.l_name} - Balance: Rs.{" "}
              {customer.balance}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;