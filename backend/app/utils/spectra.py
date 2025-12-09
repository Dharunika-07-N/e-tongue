import numpy as np
from sklearn.decomposition import PCA

_pca_instance = None

def _get_pca():
    """Lazy-load PCA instance."""
    global _pca_instance
    if _pca_instance is None:
        _pca_instance = PCA(n_components=8)
    return _pca_instance

def pca_project(spectra):
    """Reduce flattened spectral vector to PCA components."""
    pca = _get_pca()
    mat = np.array(spectra, dtype=float).reshape(1, -1)
    return pca.fit_transform(mat)
