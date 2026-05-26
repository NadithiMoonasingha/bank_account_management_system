import { useState } from "react";

function SearchCustomer() {
  const [accNo, setAccNo] = useState("");
  const [customer, setCustomer] = useState(null);
  const [message, setMessage] = useState("");

  async function handleSearch(e) {
    e.preventDefault();

    const response = await fetch(`http://127.0.0.1:5000/customers/${accNo}`);
    const result = await response.json();

    if (result.success) {
      setCustomer(result.customer);
      setMessage("");
    } else {
      setCustomer(null);
      setMessage(result.message);
    }
  }

  return (
    <div>
      <h2>Search Customer</h2>

      <form onSubmit={handleSearch}>
        <input
          type="text"
          placeholder="Account Number"
          value={accNo}
          onChange={(e) => setAccNo(e.target.value)}
        />

        <button type="submit">Search</button>
      </form>

      {message && <p>{message}</p>}

      {customer && (
        <div
          style={{
            border: "1px solid #ccc",
            borderRadius: "8px",
            padding: "15px",
            marginTop: "15px",
            backgroundColor: "white",
            width: "400px",
          }}
        >
          <h3>
            {customer.f_name} {customer.l_name}
          </h3>

          <p><strong>Account Number:</strong> {customer.acc_no}</p>
          <p><strong>NIC:</strong> {customer.nic}</p>
          <p><strong>Date of Birth:</strong> {customer.dob}</p>
          <p><strong>Address:</strong> {customer.address}</p>
          <p><strong>Phone Number:</strong> {customer.phone_no}</p>
          <p><strong>Balance:</strong> Rs. {customer.balance}</p>
        </div>
      )}
    </div>
  );
}

export default SearchCustomer;