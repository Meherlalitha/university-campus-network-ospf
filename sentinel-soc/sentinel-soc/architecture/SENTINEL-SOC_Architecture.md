**SENTINEL-SOC Architecture**

**1. Overview**
SENTINEL‑SOC is an AI‑powered SOC simulation designed to demonstrate real‑world analyst skills:

Multi‑source log ingestion
Threat scoring using ML
Automated playbook preparation
Alert prioritization
MITRE ATT&CK mapping

It is inspired by NVIDIA’s ADRIFT architecture but simplified for a homelab.

**2. Components**

**2.1 TPFP‑SOC — Threat Preconception & Fusion Plane**

Collects telemetry from:

Authentication logs
Firewall logs
DNS entropy
EDR behavioral events
Extracts features and runs an Isolation Forest model to generate a Threat Probability Score (TPS) every 30 seconds.

**2.2 ASPP — Adaptive Shadow Playbook Protocol**

When TPS > 0.65:

Pre‑loads the most likely SOAR playbook
Prepares quarantine commands
Prepares evidence collection steps
Prepares notification templates
This simulates real SOAR automation.

**2.3 WCCO‑SOC — Workload‑Coupled Context Orchestrator**

Re‑prioritizes SIEM alerts using:

**TPS × Asset Criticality × MITRE Severity**

Outputs a sorted alert queue for analysts.

**3. Data Flow**

Logs → Feature Extraction → ML Model → TPS → SOAR Pre‑Staging → Alert Prioritization

**4. SOC Analyst View**

This project demonstrates:

Threat detection
Triage
Enrichment
Response
Documentation

Exactly what Tier 1 → Tier 2 SOC analysts do.
