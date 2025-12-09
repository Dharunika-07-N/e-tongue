import random
from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from app.core.config import settings


# Labeled samples provided by the user (Tinkercad simulated data).
# Labels are normalized to "Pure" / "Adulterated" for consistent API responses.
LABELED_SAMPLES = [
    ("A1", "Pure", [0.82, 0.31, 0.15, 0.93, 0.41, 0.54]),
    ("A2", "Pure", [0.79, 0.28, 0.19, 0.88, 0.39, 0.50]),
    ("A3", "Pure", [0.84, 0.33, 0.14, 0.95, 0.43, 0.58]),
    ("A4", "Pure", [0.80, 0.30, 0.16, 0.90, 0.40, 0.52]),
    ("B1", "Adulterated", [0.52, 0.14, 0.35, 0.47, 0.21, 0.78]),
    ("B2", "Adulterated", [0.49, 0.10, 0.30, 0.50, 0.18, 0.82]),
    ("B3", "Adulterated", [0.55, 0.12, 0.38, 0.45, 0.25, 0.75]),
    ("B4", "Adulterated", [0.50, 0.15, 0.33, 0.49, 0.20, 0.80]),
]


def build_dataset_from_samples(reps: int = 80, noise: float = 0.015, seed: int = 42):
    """
    Create a small augmented dataset from provided labeled samples.

    We jitter each provided vector slightly to avoid overfitting on the
    eight originals while keeping patterns intact.
    """
    random.seed(seed)
    np.random.seed(seed)

    X = []
    y = []
    ids = []

    for sample_id, label, values in LABELED_SAMPLES:
        base = np.array(values, dtype=float)
        for _ in range(reps):
            jitter = np.random.normal(0, noise, size=base.shape)
            vec = np.clip(base + jitter, 0.0, 1.0)
            X.append(vec)
            y.append(label)
            ids.append(sample_id)

    return np.array(X, dtype=float), np.array(y), np.array(ids)


def train_adulteration_model():
    """Train a classifier to flag adulteration using provided labeled samples."""
    X, y, ids = build_dataset_from_samples()

    # Model: StandardScaler + Logistic Regression for interpretability.
    pipe = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=500, class_weight="balanced")),
        ]
    )

    pipe.fit(X, y)

    # Persist model
    out_dir = Path(settings.MODEL_DIR)
    out_dir.mkdir(exist_ok=True)
    joblib.dump(pipe, out_dir / "adulteration.pkl")

    # Basic evaluation to stdout (not persisted).
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    pipe.fit(X_train, y_train)
    report = classification_report(y_val, pipe.predict(X_val))
    print("Adulteration model validation report:\n", report)


def train_all():
    """Entry point for training all demo models."""
    train_adulteration_model()
    # Placeholders for future models (rasa/quality/anomaly)
    # can be added here when real data is available.


if __name__ == "__main__":
    train_all()
