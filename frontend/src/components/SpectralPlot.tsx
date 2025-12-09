type Props = { spectra: number[] };

export default function SpectralPlot({ spectra }: Props) {
  const validSpectra = spectra.filter(s => Number.isFinite(s));

  if (validSpectra.length === 0) {
    return (
      <div className="card glass">
        <div className="font-semibold mb-2 text-slate-100">Spectral Curve</div>
        <div className="w-full h-32 flex items-center justify-center text-slate-400">
          No spectral data to display.
        </div>
      </div>
    );
  }

  const points = validSpectra.map((y, i) => ({ x: i, y }));
  const maxY = Math.max(...points.map((p) => p.y), 1); // Ensure maxY is at least 1

  return (
    <div className="card glass">
      <div className="font-semibold mb-2 text-slate-100">Spectral Curve</div>
      <svg viewBox="0 0 200 80" className="w-full h-32 text-cyan-400 drop-shadow">
        {points.length > 1 ? (
          <polyline
            fill="none"
            stroke="currentColor"
            strokeWidth="2.5"
            points={points
              .map((p) => `${(p.x / (points.length - 1)) * 200},${80 - (p.y / maxY) * 70}`)
              .join(" ")}
          />
        ) : (
          <circle cx="100" cy={80 - (points[0].y / maxY) * 70} r="3" fill="currentColor" />
        )}
      </svg>
    </div>
  );
}
