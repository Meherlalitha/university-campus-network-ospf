# SOAR Playbook — Host Quarantine

## Trigger Conditions
- TPS > 0.80
- High EDR severity
- Suspicious outbound connections
- Multiple failed logins

## Automated Actions
1. Isolate host from network (EDR/NAC).
2. Block host IP at firewall.
3. Collect forensic evidence:
   - Running processes
   - Network connections
   - Recent event logs
4. Notify SOC lead and user’s manager.
5. Open an incident ticket and attach evidence.

## Expected Outcome
Host is isolated, evidence is preserved, and SOC begins deeper investigation.

