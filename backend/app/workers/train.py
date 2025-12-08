import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from pathlib import Path


def load_demo():
    """Load small synthetic dataset for demonstration."""
    X = np.random.rand(200, 14)
    y_rasa = np.random.choice(["sweet", "sour", "bitter", "salty"], size=200)
    y_quality = np.random.choice(["authentic", "substandard", "adulterated"], size=200)
    X_ref = X[:50]
    return X, y_rasa, y_quality, X_ref


def train_all():
    X, y_rasa, y_quality, X_ref = load_demo()

    rasa_clf = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("rf", RandomForestClassifier(n_estimators=150, class_weight="balanced")),
        ]
    )
    rasa_clf.fit(X, y_rasa)

    quality_clf = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("rf", RandomForestClassifier(n_estimators=120, class_weight="balanced")),
        ]
    )
    quality_clf.fit(X, y_quality)

    anomaly = OneClassSVM(gamma="auto").fit(X_ref)

    out_dir = Path("models")
    out_dir.mkdir(exist_ok=True)
    joblib.dump(rasa_clf, out_dir / "rasa.pkl")
    joblib.dump(quality_clf, out_dir / "quality.pkl")
    joblib.dump(anomaly, out_dir / "anomaly.pkl")


if __name__ == "__main__":
    train_all()

