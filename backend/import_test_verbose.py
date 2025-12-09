import importlib, traceback, sys, os, warnings
warnings.simplefilter("always")
print("PYTHON", sys.version)
print("CWD", os.getcwd())
print("ENV DATABASE_URL", os.environ.get("DATABASE_URL"))
try:
    print("IMPORTING app.main ...")
    m = importlib.import_module("app.main")
    print("IMPORT_OK ->", m)
except Exception:
    print("IMPORT FAILED WITH EXCEPTION:")
    traceback.print_exc()
else:
    try:
        print("HAS APP ATTR:", hasattr(m, "app"))
        print("HAS create_app:", hasattr(m, "create_app"))
        from app.core import config
        print("CONFIG.settings.DATABASE_URL:", getattr(config.settings, "DATABASE_URL", "<missing>"))
    except Exception:
        print("ERROR WHEN INSPECTING CONFIG:")
        traceback.print_exc()
