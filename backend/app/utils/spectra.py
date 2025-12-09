import numpy as np


def pca_project(spectra):
    """
    Lightweight projector for single-sample inputs.

    For now we skip PCA (which needs multiple samples) and just return the
    provided spectral vector as-is, shaped for downstream concatenation.
    """
    arr = np.array(spectra, dtype=float)
    if arr.size == 0:
        arr = np.array([0.0], dtype=float)
    return arr.reshape(1, -1)
