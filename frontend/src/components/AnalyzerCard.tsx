import { useState } from "react";
import api from "../api/client";

type InferenceResult = {
  rasa: { label: string; confidence: number };
  quality: { label: string; confidence: number };
  adulteration: { label: string; confidence: number };
  adulteration_score: number;
  threshold: number;
};

type Props = {
  onResult: (res: InferenceResult, sensorValues: number[]) => void;
};

export default function AnalyzerCard({ onResult }: Props) {
  const tasteNames = ["Sweet", "Sour", "Bitter", "Astringent", "Pungent", "Salt"];
  const [values, setValues] = useState<string[]>(Array(tasteNames.length).fill(""));
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (idx: number, val: string) => {
    const copy = [...values];
    copy[idx] = val;
    setValues(copy);
  };

  const submit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const numeric = values.map((v) => Number(v || 0));
    setLoading(true);
    setStatus("Analyzing...");
    try {
      const payload = {
        sensor: { values: numeric },
        spectra: [0, 0, 0], // placeholder spectral vector
        herb_name: "tinkercad",
        batch_no: "sim-001",
        supplier: "tinkercad",
      };
      const res = await api.post<InferenceResult>("/infer", payload);
      onResult(res.data, numeric);
      setStatus("Analysis complete");
    } catch (err) {
      console.error(err);
      setStatus("Failed to analyze");
    } finally {
      setLoading(false);
      setTimeout(() => setStatus(""), 3000);
    }
  };

  return (
    <form className="card glass space-y-3" onSubmit={submit}>
      <div className="font-semibold text-slate-50">Tinkercad Sensor Ingest</div>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
        {values.map((v, idx) => (
          <div key={idx} className="space-y-1">
            <div className="text-xs text-slate-300">{tasteNames[idx]}</div>
            <input
              value={v}
              onChange={(e) => handleChange(idx, e.target.value)}
              type="number"
              step="0.01"
              placeholder={tasteNames[idx]}
              className="input analyzer-input bg-slate-900/70 text-slate-100"
              required
            />
          </div>
        ))}
      </div>
      <button
        type="submit"
        disabled={loading}
        className="btn-primary"
      >
        {loading ? "Analyzing..." : "Analyze Adulteration"}
      </button>
      {status && <div className="text-xs text-slate-300">{status}</div>}
    </form>
  );
}

