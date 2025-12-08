export default function Alerts() {
  const alerts = [
    { level: "info", msg: "No adulteration detected (demo)." },
    { level: "warn", msg: "Batch consistency pending sufficient samples." },
  ];
  return (
    <div className="card">
      <div className="font-semibold mb-2">Alerts & Recommendations</div>
      <ul className="space-y-1">
        {alerts.map((a, idx) => (
          <li key={idx} className="text-sm text-gray-700">
            • {a.msg}
          </li>
        ))}
      </ul>
    </div>
  );
}

