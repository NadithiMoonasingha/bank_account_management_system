import { useState } from "react";

function Withdraw({ onWithdrawSuccess }) {
  const [accNo, setAccNo] = useState("");
  const [amount, setAmount] = useState("");
  const [message, setMessage] = useState("");

  async function handleWithdraw(e) {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:5000/withdraw", {
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
      onWithdrawSuccess();
    }
  }

  return (
    <div>
      <h2>Withdraw Money</h2>

      <form onSubmit={handleWithdraw}>
        <input
          type="text"
          placeholder="Account Number"
          value={accNo}
          onChange={(e) => setAccNo(e.target.value)}
        />

        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />

        <button type="submit">Withdraw</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}

export default Withdraw;