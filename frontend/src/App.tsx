import { useState } from "react";
import PredictionCard from "./components/PredictionCard";
import SpectralPlot from "./components/SpectralPlot";
import UploadForm from "./components/UploadForm";
import Alerts from "./components/Alerts";
import AnalyzerCard from "./components/AnalyzerCard";
import ImageUploadCard from "./components/ImageUploadCard";
import SampleHelper from "./components/SampleHelper";

function App() {
  const [result, setResult] = useState<any | null>(null);
  const [lastSensor, setLastSensor] = useState<number[] | null>(null);

  const handleResult = (res: any, sensorValues: number[]) => {
    setResult(res);
    setLastSensor(sensorValues);
  };

  return (
    <div className="min-h-screen ocean-bg text-slate-100">
      <div className="max-w-6xl mx-auto p-6 space-y-6">
        <header className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-slate-50 drop-shadow">AI Herbal Quality Dashboard</h1>
            <p className="text-slate-300 text-sm">
              Live e-tongue + spectroscopy + ML predictions
            </p>
          </div>
          <div className="px-3 py-2 rounded-full bg-gradient-to-r from-emerald-500 to-teal-400 text-lg shadow-lg shadow-emerald-500/30">
            🌿💊
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <AnalyzerCard onResult={handleResult} />
          <ImageUploadCard />
        </div>

        <SampleHelper />

        {result && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <PredictionCard label={`Adulteration: ${result.adulteration.label}`} confidence={result.adulteration.confidence} />
            <PredictionCard label={`Quality: ${result.quality.label}`} confidence={result.quality.confidence} />
            <PredictionCard label={`Rasa: ${result.rasa.label}`} confidence={result.rasa.confidence} />
          </div>
        )}

        {result && <SpectralPlot spectra={lastSensor || []} />}

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <UploadForm />
        </div>

        {result && <Alerts result={result} />}
      </div>
    </div>
  );
}

export default App;

