import LiveFeed from "./components/LiveFeed";
import PredictionCard from "./components/PredictionCard";
import SpectralPlot from "./components/SpectralPlot";
import UploadForm from "./components/UploadForm";
import Alerts from "./components/Alerts";
import ModelUpdate from "./components/ModelUpdate";
import TestDataHelper from "./components/TestDataHelper";

function App() {
  return (
    <div className="p-6 space-y-6">
      <header className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">AI Herbal Quality Dashboard</h1>
          <p className="text-gray-500 text-sm">
            Live e-tongue + spectroscopy + ML predictions
          </p>
        </div>
      </header>

      <LiveFeed />

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <PredictionCard label="Rasa (demo)" confidence={0.82} />
        <PredictionCard label="Quality (demo)" confidence={0.91} />
      </div>

      <SpectralPlot />

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <UploadForm />
        <ModelUpdate />
      </div>

      <TestDataHelper />

      <Alerts />
    </div>
  );
}

export default App;

