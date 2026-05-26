import { useState } from "react";

function Deposit({ onDepositDone }) {
  const [accNo, setAccNo] = useState("");
  const [amount, setAmount] = useState("");
  const [message, setMessage] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:5000/deposit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        acc_no: accNo,
        amount: amount,
      }),
    });

    const result = await response.json();
    setMessage(result.message);

    if (result.success) {
      setAccNo("");
      setAmount("");
      onDepositDone();
    }
  }

  return (
    <div>
      <h2>Deposit Money</h2>

      <form onSubmit={handleSubmit}>
        <input
          placeholder="Account Number"
          value={accNo}
          onChange={(e) => setAccNo(e.target.value)}
        />

        <input
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />

        <button type="submit">Deposit</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}

export default Deposit;