const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export type AdulterationResponse = {
  success: boolean;
  is_adulterated: boolean;
  confidence: number;
  details: string;
};

export async function analyzeAdulteration(sensorData: number[]): Promise<AdulterationResponse> {
  // Backend mounts routes under /api/v1; include the versioned prefix here.
  const resp = await fetch(`${API_BASE_URL}/api/v1/analysis/adulteration`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ sensor_data: sensorData }),
  });

  if (!resp.ok) {
    let detail = "Analysis failed";
    try {
      const payload = await resp.json();
      detail = payload?.detail || detail;
    } catch {
      // ignore parse issues and fall back to generic error
    }
    throw new Error(detail);
  }

  return resp.json();
}

