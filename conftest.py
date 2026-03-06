import sys
from pathlib import Path

# Asegura que la raíz del repo esté en sys.path (import app funciona en Linux CI)
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
