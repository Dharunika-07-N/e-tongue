# TODO: Implement Image Upload for Tinkercad Screenshots and Adulteration Prediction

## Backend Changes
- [ ] Update `backend/requirements.txt`: Add `pytesseract` and `Pillow`
- [ ] Create `backend/app/services/image_processor.py`: Service for OCR and value extraction
- [ ] Update `backend/app/schemas/sensor.py`: Add schema for image upload response
- [ ] Update `backend/app/api/v1/endpoints/sensor.py`: Add `/upload_image` endpoint

## Frontend Changes
- [ ] Update `frontend/src/components/UploadForm.tsx`: Add image upload functionality

## Testing and Followup
- [ ] Install dependencies and test image processing
- [ ] Test end-to-end: upload image, extract values, run inference, display results
