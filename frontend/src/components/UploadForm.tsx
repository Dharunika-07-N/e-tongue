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
    <form className="card space-y-3" onSubmit={submit}>
      <div className="font-semibold">Upload Spectra</div>
      <input className="w-full border rounded p-2" name="herb_name" placeholder="Herb name" required />
      <input className="w-full border rounded p-2" name="batch_no" placeholder="Batch no" required />
      <input className="w-full border rounded p-2" name="supplier" placeholder="Supplier" />
      <select className="w-full border rounded p-2" name="spectra_type" required>
        <option value="ftir">FTIR</option>
        <option value="nir">NIR</option>
        <option value="raman">Raman</option>
        <option value="hptlc">HPTLC</option>
        <option value="lcms">LC-MS</option>
      </select>
      <input className="w-full" type="file" name="file" required />
      <button className="bg-indigo-600 text-white px-4 py-2 rounded" type="submit">
        Upload
      </button>
      <div className="text-sm text-gray-500">{status}</div>
    </form>
  );
}

