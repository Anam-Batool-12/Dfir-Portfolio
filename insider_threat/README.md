# Insider Threat Investigation — DFIR Portfolio

## Overview
Forensic investigation of a simulated insider 
threat case involving potential data exfiltration 
via USB device.

## Investigator
- Alias: Anam Batool

## Tools Used
| Tool | Purpose |
|------|---------|
| dd | Disk imaging |
| md5sum / sha256sum | Hash verification |
| Autopsy 4.21 | File system analysis |
| Registry Explorer | Windows registry analysis |
| LECmd | LNK file parsing |
| PECmd | Prefetch file analysis |

## Investigation Structure
| Folder | Contents |
|--------|---------|
| evidence/ | Disk image, hash files |
| registry_evidence/ | USBSTOR, RecentDocs analysis |
| LNK_Analysis/ | LECmd output, findings |
| Prefetch_Analysis/ | PECmd output, findings |

## Key Findings
- USB device connection confirmed via USBSTOR registry
- File access history extracted via LNK files
- PowerShell executed 6 times — suspicious activity
- Chain of custody maintained throughout

## Outcome
Successfully completed forensic examination.
All artifacts documented and analyzed.
