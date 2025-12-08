import numpy as np
from sklearn.preprocessing import StandardScaler
from app.utils.spectra import pca_project

# In production, load persisted scaler; here we fit per call for brevity
scaler = StandardScaler()


def preprocess_sample(req):
    """Combine sensor and spectral features, then scale."""
    sensor = np.array(req.sensor.values, dtype=float)
    spectra = pca_project(req.spectra)
    features = np.concatenate([sensor, spectra], axis=-1).reshape(1, -1)
    return scaler.fit_transform(features)

