# SENTINEL‑SOC: AI‑Driven Security Operations Simulation

## 1. Executive Summary
SENTINEL‑SOC is an AI‑powered SOC simulation designed to demonstrate real‑world analyst skills:
- Multi‑source log ingestion
- Threat scoring using machine learning
- Automated SOAR playbook preparation
- Alert prioritization using MITRE ATT&CK
- End‑to‑end incident response workflow

This project models how modern SOCs use AI to accelerate detection and response.

---

## 2. Architecture Overview
The system is built around three major components:

### 2.1 TPFP‑SOC — Threat Preconception & Fusion Plane
- Ingests authentication, firewall, DNS, and EDR logs  
- Extracts behavioral features  
- Runs an Isolation Forest model  
- Generates a Threat Probability Score (TPS) for each host  

### 2.2 ASPP — Adaptive Shadow Playbook Protocol
- Pre‑loads SOAR playbooks when TPS exceeds thresholds  
- Prepares quarantine, phishing, and malware response actions  
- Simulates automated response workflows  

### 2.3 WCCO‑SOC — Workload‑Coupled Context Orchestrator
- Reads TPS, MITRE severity, and asset criticality  
- Calculates risk score:  
  `TPS × severity × criticality`  
- Produces a prioritized alert queue  

---

## 3. Data Sources
### Authentication Logs
Used to detect brute force and credential misuse.

### Firewall Logs
Used to detect rare outbound ports and C2 behavior.

### DNS Logs
Used to detect high‑entropy domains and suspicious queries.

### EDR Behavioral Logs
Used to detect malicious processes and privilege escalation.

---

## 4. Machine Learning Model
The ML engine uses:
- **Isolation Forest** for anomaly detection  
- Normalized anomaly scores converted into TPS  
- Output saved to `tps_output.csv`  

This simulates AI‑driven threat scoring used in modern SOCs.

---

## 5. SOAR Playbooks
Three automated playbooks are included:
- **Quarantine** (host isolation)
- **Phishing** (email investigation)
- **Malware** (process kill, hash extraction, sandboxing)

These represent Tier‑2 SOC response workflows.

---

## 6. MITRE ATT&CK Mapping
Each detection technique is mapped to:
- MITRE Technique ID  
- Severity (1–10)  
- Criticality (1–5)  

This enables risk‑based alert prioritization.

---

## 7. Alert Prioritization
The orchestrator merges:
- SIEM alerts  
- TPS  
- MITRE severity  
- Asset criticality  

Then calculates a **risk score** and sorts alerts for analysts.

---

## 8. Analyst Value
This project demonstrates:
- Threat detection  
- Triage  
- Enrichment  
- Response  
- Documentation  
- AI‑driven SOC automation  

It is designed to showcase real SOC analyst skills for hiring managers.

---

## 9. Conclusion
SENTINEL‑SOC is a complete, AI‑powered SOC simulation that demonstrates how modern security teams use machine learning, automation, and MITRE ATT&CK to accelerate detection and response.

