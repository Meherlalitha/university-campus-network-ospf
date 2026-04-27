# SENTINEL-SOC  
### AI-Powered Predictive Threat Detection & Automated Response Framework  
*Python • Splunk-style SIEM • Wazuh • Suricata • MITRE ATT&CK • SOAR Simulation*

---

##  Overview

SENTINEL-SOC is an **AI-driven SOC simulation project** designed to demonstrate advanced skills in:

- Threat detection  
- Log analysis  
- Machine learning for anomaly detection  
- Automated incident response  
- SIEM-style alerting  
- MITRE ATT&CK mapping  
- SOAR playbook orchestration  

This project is inspired by NVIDIA’s ADRIFT architecture and adapted for **enterprise SOC workflows**.

It is built to showcase **Tier 1 → Tier 2 SOC Analyst capabilities** in a single, portfolio-ready framework.

---

##  Architecture Summary

SENTINEL-SOC contains **three original components**:

### 1. TPFP-SOC — Threat Preconception & Fusion Plane**
Collects multiple telemetry streams:

- Authentication logs  
- Firewall logs  
- DNS entropy  
- EDR behavioral events  
- Log velocity spikes  
- Geolocation anomalies  

Uses a lightweight ML model (Isolation Forest + Temporal CNN simulation) to generate a **Threat Probability Score (TPS)** every 30 seconds.

---

### 2. ASPP — Adaptive Shadow Playbook Protocol**
When TPS > 0.65:

- Pre-loads the most likely SOAR playbook  
- Prepares quarantine commands  
- Prepares evidence collection steps  
- Prepares notification templates  

This reduces response time from minutes to seconds.

---

### 3. WCCO-SOC — Workload-Coupled Context Orchestrator**
Re-prioritizes SIEM alerts based on:
TPS × Asset Criticality × MITRE Technique Severity

Ensures analysts always see the **highest-risk alerts first**.

---

## 📁 Repository Structure
sentinel-soc/
│
├── architecture/
│   └── SENTINEL-SOC_Architecture.md
│
├── logs/
│   ├── auth_logs.csv
│   ├── firewall_logs.csv
│   ├── dns_logs.csv
│   └── edr_behavior.json
│
├── ml/
│   ├── tps_model.ipynb
│   └── tps_engine.py
│
├── soar/
│   ├── playbook_quarantine.md
│   ├── playbook_phishing.md
│   └── playbook_malware.md
│
├── wcco/
│   └── alert_orchestrator.py
│
├── mitre/
│   └── mitre_mapping.md
│
└── report/
└── SENTINEL-SOC_Report.md


---

## 🎯 Skills Demonstrated

- SIEM alert triage  
- Threat hunting  
- Incident response  
- Machine learning for anomaly detection  
- SOAR automation logic  
- MITRE ATT&CK mapping  
- Log parsing & enrichment  
- Documentation & architecture design  

---

## 🧪 Lab Simulation Environment

- Python (scikit-learn, pandas, numpy)  
- Suricata-style network logs  
- Wazuh-style EDR logs  
- Splunk-style SIEM queries  
- MITRE ATT&CK technique mapping  
- SOAR playbook simulation  

---

## 📌 Purpose

This project demonstrates **real SOC analyst workflows**:

- Detect → Analyze → Enrich → Respond → Document  
- Automated threat scoring  
- Alert prioritization  
- Playbook-driven response  

It is designed to stand out in SOC Analyst job applications.

---

## 📬 Contact

**Author:** Meher Lalitha Thatavarthi  
**LinkedIn:** linkedin.com/in/meherlalitha  

