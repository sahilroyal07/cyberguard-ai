import { useState } from "react";
import "./App.css";

function App() {

const [result, setResult] = useState("");
const [showModal, setShowModal] = useState(false);

const callAPI = async (endpoint: string) => {

let url = "http://127.0.0.1:8000" + endpoint;

if (endpoint === "/ai") {
  const promptText = window.prompt("Ask cybersecurity question:");
  if (!promptText) return;
  url += "?prompt=" + encodeURIComponent(promptText);
}

if (endpoint === "/scan-link") {
  const link = window.prompt("Enter URL to scan:");
  if (!link) return;
  url += "?url=" + encodeURIComponent(link);
}

if (endpoint === "/analyze-email") {
  const email = window.prompt("Paste email text:");
  if (!email) return;

  const res = await fetch("http://127.0.0.1:8000/analyze-email", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text: email })
  });

  const data = await res.json();

  setResult(JSON.stringify(data, null, 2));
  setShowModal(true);
  return;
}

const res = await fetch(url);
const data = await res.json();

setResult(JSON.stringify(data, null, 2));
setShowModal(true);

};

return (
<div style={{padding:"40px", fontFamily:"Arial", background:"white", minHeight:"100vh"}}>

  <h1 style={{fontSize:"40px"}}>SafeCore AI</h1>
  <h2>Security Tools</h2>

  <div style={{
    display:"grid",
    gridTemplateColumns:"repeat(4,1fr)",
    gap:"20px",
    marginTop:"30px"
  }}>

    <button style={btn} onClick={() => callAPI("/ai")}>AI Assistant</button>
    <button style={btn} onClick={() => callAPI("/scan-link")}>Link Scanner</button>
    <button style={btn} onClick={() => callAPI("/analyze-email")}>Email Analyzer</button>
    <button style={btn} onClick={() => callAPI("/malware")}>Malware Diagnosis</button>
    <button style={btn} onClick={() => callAPI("/device-scan")}>Device Security Scan</button>
    <button style={btn} onClick={() => callAPI("/threat-feed")}>Threat Intelligence</button>
    <button style={btn} onClick={() => callAPI("/tips")}>Security Tips</button>
    <button style={btn} onClick={() => callAPI("/learning")}>Learning Center</button>

  </div>

  {showModal && (
    <div style={modal}>

      <div style={modalBox}>

        <pre>{result}</pre>

        <button style={closeBtn} onClick={() => setShowModal(false)}>
          Close
        </button>

      </div>

    </div>
  )}

</div>

);
}

const btn = {
background:"#94a3b8",
border:"none",
padding:"20px",
borderRadius:"10px",
fontSize:"16px",
cursor:"pointer",
color:"white"
};

const modal = {
position:"fixed",
top:0,
left:0,
width:"100%",
height:"100%",
background:"rgba(0,0,0,0.4)",
display:"flex",
justifyContent:"center",
alignItems:"center"
};

const modalBox = {
background:"white",
padding:"30px",
borderRadius:"10px",
width:"500px"
};

const closeBtn = {
marginTop:"20px",
padding:"10px 20px",
background:"#2563eb",
border:"none",
color:"white",
borderRadius:"6px",
cursor:"pointer"
};

export default App;
