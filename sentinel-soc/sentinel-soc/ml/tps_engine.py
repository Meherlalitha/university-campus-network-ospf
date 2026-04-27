import time
import json
import pandas as pd
from sklearn.ensemble import IsolationForest
from pathlib import Path

# Paths
LOG_DIR = Path(__file__).resolve().parents[1] / "logs"
OUTPUT_FILE = Path(__file__).resolve().parents[1] / "ml" / "tps_output.csv"

# -----------------------------
# FEATURE EXTRACTION FUNCTIONS
# -----------------------------

def load_auth_features():
    df = pd.read_csv(LOG_DIR / "auth_logs.csv")
    fails = (
        df[df["action"] == "FAIL"]
        .groupby("host")
        .size()
        .rename("failed_logins")
    )
    return fails

def load_firewall_features():
    df = pd.read_csv(LOG_DIR / "firewall_logs.csv")
    rare = (
        df[~df["dest_port"].isin([80, 443])]
        .groupby("host")
        .size()
        .rename("rare_ports")
    )
    return rare

def load_dns_features():
    df = pd.read_csv(LOG_DIR / "dns_logs.csv")
    high_entropy = (
        df[df["entropy"] > 3.5]
        .groupby("host")
        .size()
        .rename("high_entropy_queries")
    )
    return high_entropy

def load_edr_features():
    with open(LOG_DIR / "edr_behavior.json", "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    sev = df.groupby("host")["severity"].sum().rename("edr_severity_sum")
    return sev

# -----------------------------
# BUILD FEATURE TABLE
# -----------------------------

def build_feature_table():
    auth = load_auth_features()
    fw = load_firewall_features()
    dns = load_dns_features()
    edr = load_edr_features()

    features = pd.concat([auth, fw, dns, edr], axis=1).fillna(0)
    return features

# -----------------------------
# COMPUTE TPS USING ML MODEL
# -----------------------------

def compute_tps(features: pd.DataFrame) -> pd.DataFrame:
    model = IsolationForest(contamination=0.25, random_state=42)
    model.fit(features)

    anomaly_score = model.decision_function(features)

    # Normalize to 0–1 (higher = more suspicious)
    min_s, max_s = anomaly_score.min(), anomaly_score.max()
    if max_s - min_s == 0:
        tps = pd.Series(0.5, index=features.index)
    else:
        tps = 1 - (anomaly_score - min_s) / (max_s - min_s)

    result = features.copy()
    result["TPS"] = tps.round(3)
    return result

# -----------------------------
# MAIN LOOP
# -----------------------------

def main(loop_once: bool = True, interval_seconds: int = 30):
    while True:
        features = build_feature_table()
        tps_table = compute_tps(features)
        tps_table.to_csv(OUTPUT_FILE)
        print("Updated TPS:")
        print(tps_table)

        if loop_once:
            break
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main(loop_once=True)

