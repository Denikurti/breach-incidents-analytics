# Breach Incidents Analytics

**Goal:** Explore breach data — records exposed, causes, sectors, and time-to-discovery.

## Structure
- data/raw/        → original CSV (breaches.csv)
- data/processed/  → cleaned exports
- figures/         → charts
- breach_eda.py    → main script

## How to run
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 breach_eda.py
