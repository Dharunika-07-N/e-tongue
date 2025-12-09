import random
from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from app.core.config import settings


# Baseline taste profiles for known medicines.
# Values are normalized 0-1 taste intensities for each sensor channel.
BASELINE_PROFILES = {
    "amoxicillin": [0.32, 0.18, 0.44, 0.21, 0.29, 0.35],
    "azithromycin": [0.41, 0.23, 0.38, 0.25, 0.33, 0.27],
    "paracetamol": [0.28, 0.12, 0.31, 0.19, 0.22, 0.26],
    "ciprofloxacin": [0.36, 0.27, 0.42, 0.31, 0.24, 0.30],
    "ibuprofen": [0.34, 0.20, 0.36, 0.23, 0.31, 0.28],
}


def generate_adulterated(base_profile, deviation=0.1):
    """Return a profile perturbed by +/- deviation, clipped to [0,1]."""
    return [
        max(0.0, min(1.0, v + random.uniform(-deviation, deviation)))
        for v in base_profile
    ]


def build_simulated_dataset(
    n_pure_per_med: int = 300, n_adulterated_per_med: int = 300, seed: int = 42
):
    """Create a labeled dataset using baseline taste profiles."""
    random.seed(seed)
    np.random.seed(seed)

    X = []
    y = []
    meds = []

    for medicine, baseline in BASELINE_PROFILES.items():
        # Pure: small deviation
        for _ in range(n_pure_per_med):
            X.append(generate_adulterated(baseline, deviation=0.05))
            y.append("Pure")
            meds.append(medicine)

        # Adulterated: larger deviation
        for _ in range(n_adulterated_per_med):
            X.append(generate_adulterated(baseline, deviation=0.2))
            y.append("Adulterated")
            meds.append(medicine)

    return np.array(X, dtype=float), np.array(y), np.array(meds)


def train_adulteration_model():
    """Train a simple classifier to flag adulteration."""
    X, y, meds = build_simulated_dataset()

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

    # Optional: basic evaluation to stdout (not persisted).
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
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
