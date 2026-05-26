import { useState } from "react";

function AddCustomer({ onCustomerAdded }) {
  const [formData, setFormData] = useState({
    acc_no: "",
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

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:5000/customers", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    const result = await response.json();
    setMessage(result.message);

    if (result.success) {
      setFormData({
        acc_no: "",
        nic: "",
        f_name: "",
        l_name: "",
        dob: "",
        address: "",
        phone_no: "",
      });

      onCustomerAdded();
    }
  }

  return (
    <div>
      <h2>Add New Customer</h2>

      <form onSubmit={handleSubmit}>
        <input name="acc_no" placeholder="Account Number" value={formData.acc_no} onChange={handleChange} />
        <input name="nic" placeholder="NIC" value={formData.nic} onChange={handleChange} />
        <input name="f_name" placeholder="First Name" value={formData.f_name} onChange={handleChange} />
        <input name="l_name" placeholder="Last Name" value={formData.l_name} onChange={handleChange} />
        <input name="dob" type="date" value={formData.dob} onChange={handleChange} />
        <input name="address" placeholder="Address" value={formData.address} onChange={handleChange} />
        <input name="phone_no" placeholder="Phone Number" value={formData.phone_no} onChange={handleChange} />

        <button type="submit">Add Customer</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}

export default AddCustomer;