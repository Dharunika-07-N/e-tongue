# Runbook (Local Dev)

## Backend
1. Install Python 3.10+ and create venv.
2. `cd backend`
3. `pip install -r requirements.txt`
4. `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

## Frontend
1. Install Node 18+.
2. `cd frontend`
3. `npm install`
4. `npm run dev` (Vite on :5173)

## Training demo models
```
cd backend
python -m app.workers.train
```

## Hitting inference
```
curl -X POST http://localhost:8000/api/v1/infer ^
 -H "Content-Type: application/json" ^
 -d "{\"sensor\":{\"values\":[1,2,3,4,5,6]},\"spectra\":[0.1,0.2,0.3],\"herb_name\":\"Tulsi\"}"
```

## Docker (optional)
- Compose file is scaffolded in `docker/` (fill in DB creds and build).

