import { useState } from "react";
import api from "../api/client";

export default function ModelUpdate() {
  const [status, setStatus] = useState<string>("");
  const retrain = async () => {
    try {
      await api.post("/models/retrain");
      setStatus("Retrain queued");
    } catch (err) {
      console.error(err);
      setStatus("Failed");
    }
  };
  return (
    <div className="card space-y-2">
      <div className="font-semibold">Model Management</div>
      <button className="bg-emerald-600 text-white px-4 py-2 rounded" onClick={retrain}>
        Trigger Retrain
      </button>
      <div className="text-sm text-gray-500">{status}</div>
    </div>
  );
}

