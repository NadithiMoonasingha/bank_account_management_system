import { useState } from "react";

function UpdateCustomer({ onUpdateSuccess }) {
  const [accNo, setAccNo] = useState("");
  const [formData, setFormData] = useState({
    nic: "",
    f_name: "",
    l_name: "",
    dob: "",
    address: "",
    phone_no: "",
  });

  const [message, setMessage] = useState("");

  function handleChange(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  }

  async function handleUpdate(e) {
    e.preventDefault();

    const response = await fetch(`http://127.0.0.1:5000/customers/${accNo}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    const result = await response.json();
    setMessage(result.message);

    if (result.success) {
      setAccNo("");
      setFormData({
        nic: "",
        f_name: "",
        l_name: "",
        dob: "",
        address: "",
        phone_no: "",
      });

      onUpdateSuccess();
    }
  }

  return (
    <div>
      <h2>Update Customer Details</h2>

      <form onSubmit={handleUpdate}>
        <input
          type="text"
          placeholder="Account Number"
          value={accNo}
          onChange={(e) => setAccNo(e.target.value)}
        />

        <input
          name="nic"
          placeholder="New NIC"
          value={formData.nic}
          onChange={handleChange}
        />

        <input
          name="f_name"
          placeholder="New First Name"
          value={formData.f_name}
          onChange={handleChange}
        />

        <input
          name="l_name"
          placeholder="New Last Name"
          value={formData.l_name}
          onChange={handleChange}
        />

        <input
          name="dob"
          type="date"
          value={formData.dob}
          onChange={handleChange}
        />

        <input
          name="address"
          placeholder="New Address"
          value={formData.address}
          onChange={handleChange}
        />

        <input
          name="phone_no"
          placeholder="New Phone Number"
          value={formData.phone_no}
          onChange={handleChange}
        />

        <button type="submit">Update Customer</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}

export default UpdateCustomer;