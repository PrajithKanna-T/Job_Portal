import React, { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [accessToken, setAccessToken] = useState(""); // LinkedIn token (optional)

  const handleSearch = async () => {
    try {
      const res = await axios.post("http://localhost:5000/query", {
        query,
        access_token: accessToken,
      });
      setResponse(res.data.result);
    } catch (err) {
      setResponse("Error: " + err.message);
    }
  };

  return (
  <div style={{
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
    fontFamily: "Arial",
    flexDirection: "column"
  }}>
    <h2>🎯 Job Search Chatbot</h2>
    <input
      type="text"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Enter your job query"
      style={{ padding: "10px", width: "300px", marginBottom: "1rem" }}
    />
    <button onClick={handleSearch} style={{ padding: "10px 20px" }}>
      Search
    </button>
    <div style={{ marginTop: "20px", maxWidth: "600px", textAlign: "center" }}>
      <strong>Response:</strong>
      <p>{response}</p>
    </div>
  </div>
);
  
}

export default App;