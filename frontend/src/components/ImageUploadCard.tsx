import { useState } from "react";
import api from "../api/client";

export default function ImageUploadCard() {
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = new FormData(e.currentTarget);
    setLoading(true);
    setStatus("Uploading...");
    try {
      await api.post("/sensor/upload_image", form, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setStatus("Image received — OCR placeholder stored");
    } catch (err) {
      console.error(err);
      setStatus("Upload failed");
    } finally {
      setLoading(false);
      setTimeout(() => setStatus(""), 3500);
    }
  };

  return (
    <form className="card glass space-y-3" onSubmit={submit}>
      <div className="font-semibold text-slate-50">Upload Tinkercad Image</div>
      <input
        type="file"
        name="file"
        accept="image/*"
        required
        className="text-slate-200 text-sm"
      />
      <button type="submit" disabled={loading} className="btn-secondary">
        {loading ? "Uploading..." : "Send Image"}
      </button>
      {status && <div className="text-xs text-slate-300">{status}</div>}
    </form>
  );
}

