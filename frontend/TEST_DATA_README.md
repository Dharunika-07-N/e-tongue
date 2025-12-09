# Test Data Guide

This guide explains how to use the sample test data provided in the frontend application.

## Quick Test Actions

The **Test Data Helper** component provides quick buttons to:

1. **Fill Form** - Automatically fills the upload form with sample herb data
2. **Download Sample File** - Downloads a ready-to-use JSON file for spectra upload
3. **Test Sensor API** - Sends sample sensor data to the backend
4. **Test Inference API** - Tests the ML inference endpoint with sample data

## Sample Data Files

Pre-made sample JSON files are available in the `public/` folder:

- `sample_tulsi_ftir.json` - Tulsi (Ocimum sanctum) FTIR data
- `sample_ashwagandha_nir.json` - Ashwagandha (Withania somnifera) NIR data
- `sample_turmeric_raman.json` - Turmeric (Curcuma longa) Raman data

## How to Use

### Method 1: Using Test Data Helper Component

1. Open the application in your browser
2. Scroll down to the "🧪 Test Data Helper" section
3. Click "Fill Form (Tulsi)" or "Fill Form (Ashwagandha)" to auto-fill the upload form
4. Click "Download Sample File" to get a JSON file
5. Upload the downloaded file using the form

### Method 2: Using Pre-made Sample Files

1. Navigate to `http://localhost:5173/sample_tulsi_ftir.json` (or other sample files)
2. Save the JSON file to your computer
3. Fill in the upload form:
   - Herb name: `Tulsi (Ocimum sanctum)`
   - Batch no: `BCH-9712`
   - Supplier: `Herbal Suppliers Inc.`
   - Spectra type: `ftir`
4. Select the downloaded JSON file
5. Click Upload

### Method 3: Programmatic Testing

Use the sample data constants in your code:

```typescript
import { sampleHerbs, sampleSensorData, sampleInferenceRequest } from './data/sampleData';

// Use sampleHerbs for form data
// Use sampleSensorData for sensor API calls
// Use sampleInferenceRequest for inference API calls
```

## Sample Herb Data

Available sample herbs:
- **Tulsi (Ocimum sanctum)** - FTIR, Batch: BCH-9712
- **Ashwagandha (Withania somnifera)** - NIR, Batch: BCH-9713
- **Turmeric (Curcuma longa)** - Raman, Batch: BCH-9714
- **Ginger (Zingiber officinale)** - HPTLC, Batch: BCH-9715
- **Neem (Azadirachta indica)** - LC-MS, Batch: BCH-9716

## API Testing

### Test Sensor Ingestion
```javascript
POST /api/v1/sensor/ingest
{
  "sensor_id": "demo-01",
  "values": [123, 256, 301, 220, 180, 90]
}
```

### Test Inference
```javascript
POST /api/v1/infer/
{
  "sensor": {
    "values": [123, 256, 301, 220, 180, 90]
  },
  "spectra": [0.1, 0.15, 0.22, 0.35, 0.45, 0.62, 0.78, 0.85, ...],
  "herb_name": "Tulsi (Ocimum sanctum)",
  "batch_no": "BCH-9712",
  "supplier": "Herbal Suppliers Inc."
}
```

## Notes

- All sample data is for testing purposes only
- The spectral data values are randomly generated for demonstration
- Real production data should come from actual sensor readings and spectroscopy equipment

