type Props = { spectra: number[] };

export default function SpectralPlot({ spectra }: Props) {
  const points =
    spectra.length > 0
      ? spectra.map((y, i) => ({ x: i, y }))
      : Array.from({ length: 20 }, (_, i) => ({ x: i, y: Math.sin(i / 3) + 1 }));
  const maxY = Math.max(...points.map((p) => p.y));
  return (
    <div className="card glass">
      <div className="font-semibold mb-2 text-slate-100">Spectral Curve</div>
      <svg viewBox="0 0 200 80" className="w-full h-32 text-cyan-400 drop-shadow">
        <polyline
          fill="none"
          stroke="currentColor"
          strokeWidth="2.5"
          points={points.map((p) => `${(p.x / (points.length - 1 || 1)) * 200},${80 - (p.y / maxY) * 70}`).join(" ")}
        />
      </svg>
    </div>
  );
}

