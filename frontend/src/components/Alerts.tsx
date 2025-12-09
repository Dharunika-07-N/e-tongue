type Props = {
  result: {
    adulteration: { label: string; confidence: number };
    quality: { label: string; confidence: number };
  };
};

export default function Alerts({ result }: Props) {
  const alerts = [];
  if (result.adulteration.label.toLowerCase().includes("adulter")) {
    alerts.push({
      level: "warn",
      msg: "Adulteration suspected. Hold batch and run confirmatory lab tests.",
    });
  } else {
    alerts.push({
      level: "info",
      msg: "Batch looks authentic. Proceed with standard QA sampling.",
    });
  }

  alerts.push({
    level: "info",
    msg: `Quality score: ${(result.quality.confidence * 100).toFixed(1)}%.`,
  });

  return (
    <div className="card glass">
      <div className="font-semibold mb-2 text-slate-100">Alerts & Recommendations</div>
      <ul className="space-y-2">
        {alerts.map((a, idx) => (
          <li
            key={idx}
            className={`text-sm ${
              a.level === "warn" ? "text-amber-300" : "text-slate-200"
            }`}
          >
            • {a.msg}
          </li>
        ))}
      </ul>
    </div>
  );
}

