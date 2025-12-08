# Architecture (brief)
- Firmware (ESP32/CircuitPython) reads 6-channel e-tongue, applies offsets/gains, streams JSON over WiFi/BLE/USB.
- FastAPI backend ingests sensor and spectral uploads, preprocesses (scaling + PCA), runs ML models (rasa multi-class, quality classifier, anomaly detector, threshold regressor), stores to DB, exposes reports and SHAP explainability hooks.
- PostgreSQL (or SQLite dev) stores samples, metadata, calibration, uploads.
- React + Tailwind dashboard shows live sensor feed, predictions, spectral curves, alerts, admin model retrain and upload.
- Workers provide retraining; models stored in `models/` as joblib pickles.

