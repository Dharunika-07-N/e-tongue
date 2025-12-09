import numpy as np
from sklearn.preprocessing import StandardScaler
from app.utils.spectra import pca_project

_scaler_instance = None

def _get_scaler():
    """Lazy-load StandardScaler instance."""
    global _scaler_instance
    if _scaler_instance is None:
        _scaler_instance = StandardScaler()
    return _scaler_instance

def preprocess_sample(req):
    """Combine sensor and spectral features, then scale."""
    scaler = _get_scaler()
    sensor = np.array(req.sensor.values, dtype=float)
    spectra = pca_project(req.spectra)
    features = np.concatenate([sensor, spectra], axis=-1).reshape(1, -1)
    return scaler.fit_transform(features)
