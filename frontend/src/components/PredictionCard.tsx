type Props = { label: string; confidence: number };

export default function PredictionCard({ label, confidence }: Props) {
  return (
    <div className="card">
      <div className="text-sm text-gray-500">Prediction</div>
      <div className="text-xl font-semibold">{label}</div>
      <div className="text-sm text-gray-600">{(confidence * 100).toFixed(1)}%</div>
    </div>
  );
}

