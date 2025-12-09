const samples = {
  authentic: [0.82, 0.31, 0.15, 0.93, 0.41, 0.54],
  adulterated: [0.52, 0.14, 0.35, 0.47, 0.21, 0.78],
};

export default function SampleHelper() {
  const applyValues = (vals: number[]) => {
    const inputs = Array.from(document.querySelectorAll<HTMLInputElement>(".analyzer-input"));
    vals.forEach((v, idx) => {
      if (inputs[idx]) inputs[idx].value = String(v);
    });
    if (inputs[0]) inputs[0].dispatchEvent(new Event("input", { bubbles: true }));
  };

  return (
    <div className="card glass space-y-3">
      <div className="font-semibold text-slate-100">Quick Test Values</div>
      <p className="text-xs text-slate-300">Auto-fill the analyzer with sample herbs.</p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
        <button
          className="btn-secondary"
          onClick={() => applyValues(samples.authentic)}
        >
          Fill Authentic Sample
        </button>
        <button
          className="btn-secondary"
          onClick={() => applyValues(samples.adulterated)}
        >
          Fill Adulterated Sample
        </button>
      </div>
    </div>
  );
}

