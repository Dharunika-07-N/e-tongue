import { useState } from "react";
import { sampleHerbs, sampleInferenceRequest } from "../data/sampleData";
import { createSampleSpectraFile } from "../data/sampleSpectraFiles";
import api from "../api/client";

export default function TestDataHelper() {
  const [status, setStatus] = useState<string>("");
  const [loading, setLoading] = useState(false);

  const fillFormWithSample = (index: number = 0) => {
    const sample = sampleHerbs[index % sampleHerbs.length];
    const form = document.querySelector('form') as HTMLFormElement;
    if (!form) {
      setStatus("Form not found");
      return;
    }

    const herbInput = form.querySelector('input[name="herb_name"]') as HTMLInputElement;
    const batchInput = form.querySelector('input[name="batch_no"]') as HTMLInputElement;
    const supplierInput = form.querySelector('input[name="supplier"]') as HTMLInputElement;
    const spectraSelect = form.querySelector('select[name="spectra_type"]') as HTMLSelectElement;

    if (herbInput) herbInput.value = sample.herb_name;
    if (batchInput) batchInput.value = sample.batch_no;
    if (supplierInput) supplierInput.value = sample.supplier;
    if (spectraSelect) spectraSelect.value = sample.spectra_type;

    setStatus(`Form filled with: ${sample.herb_name}`);
    setTimeout(() => setStatus(""), 3000);
  };

  const downloadSampleFile = async (index: number = 0) => {
    const sample = sampleHerbs[index % sampleHerbs.length];
    const data = createSampleSpectraFile(
      sample.spectra_type,
      sample.herb_name,
      sample.batch_no
    );

    const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${sample.herb_name.replace(/\s+/g, "_")}_${sample.spectra_type}_${sample.batch_no}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    setStatus(`Downloaded: ${a.download}`);
    setTimeout(() => setStatus(""), 3000);
  };

  const testSensorIngest = async () => {
    setLoading(true);
    setStatus("Testing sensor ingest...");
    try {
      await api.post("/sensor/ingest", {
        sensor_id: "test-sensor-01",
        values: [123, 256, 301, 220, 180, 90],
      });
      setStatus("✓ Sensor data ingested successfully");
    } catch (err) {
      console.error(err);
      setStatus("✗ Sensor ingest failed");
    } finally {
      setLoading(false);
      setTimeout(() => setStatus(""), 5000);
    }
  };

  const testInference = async () => {
    setLoading(true);
    setStatus("Testing inference...");
    try {
      const response = await api.post("/infer/", sampleInferenceRequest);
      setStatus(`✓ Inference successful: ${response.data.rasa?.label || "OK"}`);
    } catch (err) {
      console.error(err);
      setStatus("✗ Inference failed");
    } finally {
      setLoading(false);
      setTimeout(() => setStatus(""), 5000);
    }
  };

  return (
    <div className="card space-y-3">
      <div className="font-semibold">🧪 Test Data Helper</div>
      <div className="text-xs text-gray-500 mb-2">
        Quick actions to test the application
      </div>

      <div className="grid grid-cols-2 gap-2">
        <button
          onClick={() => fillFormWithSample(0)}
          className="bg-blue-500 text-white px-3 py-2 rounded text-sm hover:bg-blue-600"
          disabled={loading}
        >
          Fill Form (Tulsi)
        </button>
        <button
          onClick={() => fillFormWithSample(1)}
          className="bg-blue-500 text-white px-3 py-2 rounded text-sm hover:bg-blue-600"
          disabled={loading}
        >
          Fill Form (Ashwagandha)
        </button>
        <button
          onClick={() => downloadSampleFile(0)}
          className="bg-green-500 text-white px-3 py-2 rounded text-sm hover:bg-green-600"
          disabled={loading}
        >
          Download Sample File
        </button>
        <button
          onClick={testSensorIngest}
          className="bg-purple-500 text-white px-3 py-2 rounded text-sm hover:bg-purple-600"
          disabled={loading}
        >
          Test Sensor API
        </button>
        <button
          onClick={testInference}
          className="bg-orange-500 text-white px-3 py-2 rounded text-sm hover:bg-orange-600 col-span-2"
          disabled={loading}
        >
          Test Inference API
        </button>
      </div>

      {status && (
        <div className="text-sm text-gray-600 bg-gray-100 p-2 rounded">
          {status}
        </div>
      )}
    </div>
  );
}

