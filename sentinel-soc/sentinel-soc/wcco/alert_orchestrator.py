import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
TPS_FILE = BASE_DIR / "ml" / "tps_output.csv"
MITRE_FILE = BASE_DIR / "mitre" / "mitre_mapping.csv"

# -----------------------------
# LOAD DATA
# -----------------------------

def load_tps():
    return pd.read_csv(TPS_FILE, index_col=0)

def load_mitre():
    return pd.read_csv(MITRE_FILE)

def load_siem_alerts():
    # Simulated SIEM alerts
    data = [
        {"host": "WIN10-WS01", "alert": "Suspicious PowerShell", "technique": "T1059"},
        {"host": "DC01", "alert": "Credential Access Attempt", "technique": "T1003"},
        {"host": "BACKUP01", "alert": "Unusual Network Traffic", "technique": "T1041"},
    ]
    return pd.DataFrame(data)

# -----------------------------
# PRIORITIZATION LOGIC
# -----------------------------

def calculate_priority():
    tps = load_tps()
    mitre = load_mitre()
    alerts = load_siem_alerts()

    merged = alerts.merge(tps, left_on="host", right_index=True)
    merged = merged.merge(mitre, on="technique")

    merged["risk_score"] = (
        merged["TPS"] * merged["severity"] * merged["criticality"]
    ).round(3)

    return merged.sort_values(by="risk_score", ascending=False)

# -----------------------------
# MAIN
# -----------------------------

def main():
    prioritized = calculate_priority()
    print("\n=== PRIORITIZED ALERT QUEUE ===\n")
    print(prioritized[["host", "alert", "technique", "risk_score"]])

if __name__ == "__main__":
    main()

