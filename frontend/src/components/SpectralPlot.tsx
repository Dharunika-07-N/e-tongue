import { useMemo } from "react";

export default function SpectralPlot() {
  const points = useMemo(() => Array.from({ length: 20 }, (_, i) => ({ x: i, y: Math.sin(i / 3) + 1 })), []);
  const maxY = Math.max(...points.map((p) => p.y));
  return (
    <div className="card">
      <div className="font-semibold mb-2">Spectral Curve (demo)</div>
      <svg viewBox="0 0 200 80" className="w-full h-32 text-indigo-500">
        <polyline
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          points={points.map((p) => `${(p.x / 19) * 200},${80 - (p.y / maxY) * 70}`).join(" ")}
        />
      </svg>
    </div>
  );
}

