import { useState } from "react";

function DeleteCustomer({ onDeleteSuccess }) {
  const [accNo, setAccNo] = useState("");
  const [message, setMessage] = useState("");

  async function handleDelete(e) {
    e.preventDefault();

    const confirmDelete = window.confirm(
      "Are you sure you want to delete this customer?"
    );

    if (!confirmDelete) {
      return;
    }

    const response = await fetch(`http://127.0.0.1:5000/customers/${accNo}`, {
      method: "DELETE",
    });

    const result = await response.json();
    setMessage(result.message);

    if (result.success) {
      setAccNo("");
      onDeleteSuccess();
    }
  }

  return (
    <div className="dashboard-card">
      <h2>Delete Customer</h2>

      <form onSubmit={handleDelete}>
        <input
          type="text"
          placeholder="Account Number"
          value={accNo}
          onChange={(e) => setAccNo(e.target.value)}
        />

        <button type="submit">Delete Customer</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}

export default DeleteCustomer;