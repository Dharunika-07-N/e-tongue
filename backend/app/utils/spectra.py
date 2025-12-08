import numpy as np
from sklearn.decomposition import PCA

pca = PCA(n_components=8)


def pca_project(spectra):
    """Reduce flattened spectral vector to PCA components."""
    mat = np.array(spectra, dtype=float).reshape(1, -1)
    return pca.fit_transform(mat)

