# SOAR Playbook — Phishing Investigation

## Trigger Conditions
- Suspicious email reported
- DNS entropy spike
- User clicked unknown link
- TPS > 0.65 for user workstation

## Automated Actions
1. Pull email from mailbox.
2. Extract indicators (URLs, attachments, sender).
3. Detonate attachment in sandbox.
4. Check URL reputation.
5. Search for similar emails across organization.
6. Notify user and reset credentials if needed.

## Expected Outcome
Phishing attempt is contained and user account is secured.

