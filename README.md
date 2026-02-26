# 🛡️ IT Risk Assessment CLI Tool

**Developed by Bidemi Salami**  
ISO 27001 Certified | Cybersecurity Expert | IT Governance Specialist

-----

## Overview

A command-line tool that evaluates IT risk across five key security domains and generates a scored risk report with prioritised remediation recommendations. Built using Python, this tool is designed for IT managers, security consultants, and compliance teams conducting internal risk assessments.

-----

## Features

- ✅ Assesses risk across **5 core IT security domains**
- 📊 Generates a **scored risk report** per domain and overall
- 🔴 Colour-coded **risk ratings**: Low → Critical
- 📋 Provides **prioritised remediation recommendations**
- 💾 Optional **JSON export** of full assessment results
- 🖥️ Clean, interactive **CLI interface** — no dependencies required

-----

## Risk Domains Covered

|Domain                                 |Focus Areas                                     |
|---------------------------------------|------------------------------------------------|
|Access Control & Identity Management   |MFA, RBAC, Privileged Access, Offboarding       |
|Data Security & Privacy                |Encryption, GDPR, Data Classification, Backups  |
|Network & Infrastructure Security      |Firewalls, Patching, VPN, Vulnerability Scanning|
|Incident Response & Business Continuity|IRP, BCP, RTO, Post-Incident Reviews            |
|Compliance & Governance                |Policies, Audits, Vendor Risk, Security Training|

-----

## Risk Score Ratings

|Score  |Rating      |
|-------|------------|
|90–100%|✅ Low       |
|70–89% |🟡 Medium-Low|
|50–69% |🟠 Medium    |
|25–49% |🔴 High      |
|0–24%  |🚨 Critical  |

-----

## Getting Started

### Requirements

- Python 3.7 or higher
- No external libraries required (uses standard library only)

### Installation

```bash
git clone https://github.com/Bidexxxz/it-risk-assessment-cli.git
cd it-risk-assessment-cli
```

### Run the Tool

```bash
python3 risk_assessment.py
```

-----

## Usage

1. Enter your organisation name when prompted
1. Answer **Yes/No** questions across all 5 domains
1. Review your **domain scores** and **overall risk rating**
1. Read **prioritised recommendations** for any weak areas
1. Optionally export a full **JSON report**

-----

## Example Output

```
  DOMAIN SCORES

  ✅ Access Control & Identity Management
     [████████████████░░░░] 80% — MEDIUM-LOW

  🚨 Network & Infrastructure Security
     [████████░░░░░░░░░░░░] 40% — HIGH

  OVERALL RISK SCORE

  🔴  58% — MEDIUM RISK

  PRIORITY RECOMMENDATIONS

  ▸ Network & Infrastructure Security
    • Implement network micro-segmentation to limit lateral movement.
    • Establish a patch management policy with defined SLAs.
```

-----

## Background

This project was built to complement enterprise IT risk management workflows, drawing on real-world experience implementing security frameworks, GDPR compliance programmes, and ISO 27001 governance controls.

It reflects the intersection of **technical knowledge** and **practical risk management** — bridging the gap between security policy and operational IT teams.

-----

## Future Enhancements

- [ ] PDF report generation
- [ ] Multi-user/department scoring
- [ ] Integration with risk registers (CSV/Excel export)
- [ ] Web-based dashboard version

-----

## Author

**Bidemi Salami**  
🔗 [LinkedIn](https://www.linkedin.com/in/engr-bidemi-salami-94895736)  
📧 salamibidemi5@gmail.com  
🐙 [GitHub](https://github.com/Bidexxxz)

-----

*“Technology leadership is about balancing innovation with security.”*
