import { useEffect, useState } from "react";
import api from "../api/client";

type SensorResponse = { sensor_id: string; values: number[] };

export default function LiveFeed() {
  const [data, setData] = useState<SensorResponse | null>(null);

  useEffect(() => {
    const id = setInterval(async () => {
      try {
        const res = await api.get<SensorResponse>("/sensor/mock");
        setData(res.data);
      } catch (err) {
        console.error(err);
      }
    }, 1500);
    return () => clearInterval(id);
  }, []);

  return (
    <div className="card">
      <div className="font-semibold">Live Sensor Feed</div>
      <div className="text-xs text-gray-500 mb-2">{data?.sensor_id ?? "—"}</div>
      <div className="flex flex-wrap gap-2">
        {data?.values.map((v, i) => (
          <div key={i} className="px-3 py-2 bg-gray-100 rounded text-sm">
            Ch{i + 1}: {v}
          </div>
        )) || "Waiting for data..."}
      </div>
    </div>
  );
}

