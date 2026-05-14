# Ransomware Incident Response Report
**Case ID:** Ransomware-Case02  
**Investigator:** Anam Batool  
**Date:** 2026-05-14  

---

## What Happened
A ransomware attack encrypted 4 confidential files on a 
workstation. Attacker dropped a ransom note demanding 
0.5 BTC. All files were successfully recovered.

---

## Evidence
| Item | Details |
|------|---------|
| Disk Image | ransomware_disk.img (200MB) |
| MD5 | [paste yours] |
| SHA256 | [paste yours] |

---

## Findings
| File | Status |
|------|--------|
| finance_report.txt.locked | 🔓 Recovered |
| employee_db.txt.locked | 🔓 Recovered |
| contracts.txt.locked | 🔓 Recovered |
| source_code.txt.locked | 🔓 Recovered |

**Attack Time:** 2026-05-14 00:36:35  
**Ransom Note:** READ_ME_NOW.txt  
**Attacker ID:** SIM-2026-CASE02  

---

## Recovery
All 4 files recovered using base64 decode.  
Real ransomware requires AES-256 decryption key.

---

## Recommendations
1. Keep offline backups
2. Isolate infected machine immediately
3. Report to FIA under PECA 2016 Section 32

---
*Simulated lab — educational purposes only.*
