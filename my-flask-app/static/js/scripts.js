import { useState } from "react";
import axios from "axios";

const URLChecker = () => {
    const [url, setUrl] = useState("");
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const checkURL = async () => {
        setLoading(true);
        try {
            const response = await axios.post("http://127.0.0.1:5000/check_url", { url });
            setResult(response.data); // { status: "Safe" / "Suspicious" / "Phishing" }
        } catch (error) {
            setResult({ status: "Error checking URL" });
        }
        setLoading(false);
    };

    return (
        <div className="p-6 bg-white shadow-lg rounded-lg">
            <h2 className="text-xl font-bold mb-4">URL Phishing Checker</h2>
            <input
                type="text"
                placeholder="Enter URL here..."
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                className="border p-2 w-full mb-4"
            />
            <button
                onClick={checkURL}
                className="bg-blue-500 text-white px-4 py-2 rounded-lg"
            >
                {loading ? "Checking..." : "Check URL"}
            </button>
            {result && <p className="mt-4 text-lg">Result: <b>{result.status}</b></p>}
        </div>
    );
};

export default URLChecker;
