import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const generate = async () => {
    setLoading(true);

    try {
      const res = await axios.post(
        `http://127.0.0.1:8000/generate?prompt=${encodeURIComponent(prompt)}`
      );

      setResult(res.data);
    } catch (err) {
      console.log(err);
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="hero">
        <h1>🚀 AI App Compiler</h1>
        <p>
          Natural Language → Architecture → Schema → Runtime
        </p>

        <textarea
          placeholder="Build a CRM with login, contacts, dashboard and admin role..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />

        <button onClick={generate}>
          {loading ? "Generating..." : "Generate Application"}
        </button>
      </div>

      {result && (
        <div className="grid">
          <div className="card">
            <h2>Intent</h2>
            <pre>{JSON.stringify(result.intent, null, 2)}</pre>
          </div>

          <div className="card">
            <h2>Architecture</h2>
            <pre>{JSON.stringify(result.architecture, null, 2)}</pre>
          </div>

          <div className="card">
            <h2>Schemas</h2>
            <pre>{JSON.stringify(result.schemas, null, 2)}</pre>
          </div>

          <div className="card">
            <h2>Authentication</h2>
            <pre>{JSON.stringify(result.auth, null, 2)}</pre>
          </div>

          <div className="card">
            <h2>Generated FastAPI</h2>
            <pre>{result.generated_code?.fastapi}</pre>
          </div>

          <div className="card">
            <h2>Generated SQL</h2>
            <pre>{result.generated_code?.sql}</pre>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;