# API Overview

Base URL: `http://localhost:8000/api/v1`

## Sensor
- `POST /sensor/ingest` — body: `{"sensor_id": "esp32-01", "values": [..]}` → `{status:"ok"}`
- `GET /sensor/mock` — mock sensor vector for UI/dev.

## Spectra
- `POST /spectra/upload` — multipart fields: `herb_name`, `batch_no`, `supplier`, `spectra_type`, `file`.

## Inference
- `POST /infer` — body:
```
{
  "sensor": {"values":[...]},
  "spectra": [/* flattened spectrum */],
  "herb_name": "Tulsi",
  "batch_no": "B123"
}
```
→
```
{
  "rasa": {"label":"sweet","confidence":0.82},
  "quality": {"label":"authentic","confidence":0.91},
  "adulteration_score": 0.12,
  "threshold": 0.45
}
```

## Models
- `GET /models/status` — reports which models are loaded.
- `POST /models/retrain` — trigger background retrain (placeholder).

## Reports
- `GET /reports/{sample_id}` — returns PDF report for sample.

