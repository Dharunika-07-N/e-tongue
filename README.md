# E-Tongue + Spectroscopy Herbal QA

End-to-end scaffold: FastAPI backend, React/Tailwind dashboard, firmware examples, ML placeholders.

## Quickstart
1. Backend
   - `cd backend`
   - `python -m venv .venv && .\.venv\Scripts\activate`
   - `pip install -r requirements.txt`
   - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
   - Run a demo model build (optional): `python -m app.workers.train`
2. Frontend
   - `cd frontend`
   - `npm install`
   - `npm run dev -- --host --port 5173`
3. Visit `http://localhost:5173`

## Docker
```
cd docker
docker-compose up --build
```

## Firmware
- ESP32 sketch: `firmware/esp32_e_tongue.ino`
- CircuitPython: `firmware/circuitpython_code.py`

## API
See `docs/api.md` for routes and payloads.

