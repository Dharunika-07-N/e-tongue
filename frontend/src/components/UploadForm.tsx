import { useState } from "react";
import api from "../api/client";

export default function UploadForm() {
  const [status, setStatus] = useState<string>("");

  const submit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    try {
      await api.post("/spectra/upload", formData, { headers: { "Content-Type": "multipart/form-data" } });
      setStatus("Uploaded");
    } catch (err) {
      console.error(err);
      setStatus("Failed");
    }
  };

  return (
    <form className="card glass space-y-3" onSubmit={submit}>
      <div className="font-semibold text-slate-100">Upload Spectra (optional)</div>
      <input className="input" name="herb_name" placeholder="Herb name" required />
      <input className="input" name="batch_no" placeholder="Batch no" required />
      <input className="input" name="supplier" placeholder="Supplier" />
      <select className="input" name="spectra_type" required>
        <option value="ftir">FTIR</option>
        <option value="nir">NIR</option>
        <option value="raman">Raman</option>
        <option value="hptlc">HPTLC</option>
        <option value="lcms">LC-MS</option>
      </select>
      <input className="w-full" type="file" name="file" required />
      <button className="btn-secondary" type="submit">
        Upload
      </button>
      <div className="text-sm text-slate-300">{status}</div>
    </form>
  );
}

