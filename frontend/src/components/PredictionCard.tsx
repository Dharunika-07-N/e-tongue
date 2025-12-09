type Props = { label: string; confidence: number };

export default function PredictionCard({ label, confidence }: Props) {
  return (
    <div className="card glass">
      <div className="text-xs text-slate-300 uppercase tracking-wide">Prediction</div>
      <div className="text-xl font-semibold text-slate-50 drop-shadow">{label}</div>
      <div className="text-sm text-slate-200">{(confidence * 100).toFixed(1)}%</div>
    </div>
  );
}

