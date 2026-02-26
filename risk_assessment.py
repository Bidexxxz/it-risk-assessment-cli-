#!/usr/bin/env python3
"""
IT Risk Assessment CLI Tool
Author: Bidemi Salami
Description: A command-line tool that evaluates IT risks across key domains
             and generates a scored risk report with mitigation recommendations.
"""

import json
import datetime
import os

# ─── Risk Categories & Questions ────────────────────────────────────────────

RISK_DOMAINS = {
    "Access Control & Identity Management": [
        ("Are privileged accounts reviewed and audited regularly?", True),
        ("Is Multi-Factor Authentication (MFA) enforced for all users?", True),
        ("Are access rights revoked promptly when staff leave?", True),
        ("Is role-based access control (RBAC) implemented?", True),
        ("Are shared/generic accounts prohibited?", True),
    ],
    "Data Security & Privacy": [
        ("Is sensitive data encrypted at rest and in transit?", True),
        ("Is a data classification policy in place?", True),
        ("Are data retention and disposal policies enforced?", True),
        ("Is GDPR or relevant data protection compliance maintained?", True),
        ("Are data backup and recovery procedures tested regularly?", True),
    ],
    "Network & Infrastructure Security": [
        ("Are firewalls and intrusion detection systems in place?", True),
        ("Is network segmentation implemented?", True),
        ("Are security patches applied within 30 days of release?", True),
        ("Is remote access secured via VPN or Zero Trust architecture?", True),
        ("Are vulnerability scans conducted at least quarterly?", True),
    ],
    "Incident Response & Business Continuity": [
        ("Is there a documented and tested incident response plan?", True),
        ("Are staff trained on incident reporting procedures?", True),
        ("Is a Business Continuity Plan (BCP) in place and tested?", True),
        ("Are critical system recovery time objectives (RTOs) defined?", True),
        ("Are post-incident reviews conducted and documented?", True),
    ],
    "Compliance & Governance": [
        ("Is there a current IT security policy approved by leadership?", True),
        ("Are security awareness training sessions conducted annually?", True),
        ("Is there a third-party/vendor risk management process?", True),
        ("Are audit logs retained and regularly reviewed?", True),
        ("Is there a formal risk register maintained?", True),
    ],
}

RISK_LEVELS = {
    (90, 100): ("LOW", "✅", "\033[92m"),
    (70, 89):  ("MEDIUM-LOW", "🟡", "\033[93m"),
    (50, 69):  ("MEDIUM", "🟠", "\033[33m"),
    (25, 49):  ("HIGH", "🔴", "\033[91m"),
    (0, 24):   ("CRITICAL", "🚨", "\033[31m"),
}

RECOMMENDATIONS = {
    "Access Control & Identity Management": [
        "Implement a Privileged Access Management (PAM) solution.",
        "Enforce MFA across all systems, including legacy applications.",
        "Automate user offboarding through HR-IT integration.",
        "Conduct quarterly access reviews and recertification.",
    ],
    "Data Security & Privacy": [
        "Adopt AES-256 encryption for data at rest; enforce TLS 1.2+ in transit.",
        "Deploy a Data Loss Prevention (DLP) solution.",
        "Establish a formal data retention schedule aligned to legal requirements.",
        "Register a Data Protection Officer (DPO) if processing personal data at scale.",
    ],
    "Network & Infrastructure Security": [
        "Implement network micro-segmentation to limit lateral movement.",
        "Establish a patch management policy with defined SLAs.",
        "Adopt a Zero Trust Network Access (ZTNA) framework.",
        "Schedule automated vulnerability scans and remediate findings within SLA.",
    ],
    "Incident Response & Business Continuity": [
        "Develop and table-top test an Incident Response Plan annually.",
        "Define and communicate escalation paths for security incidents.",
        "Test backup restoration procedures quarterly.",
        "Align BCP with ISO 22301 or equivalent standard.",
    ],
    "Compliance & Governance": [
        "Review and update security policies annually or after major incidents.",
        "Deliver mandatory security awareness training using phishing simulations.",
        "Establish a third-party risk assessment process for all critical vendors.",
        "Implement a SIEM solution for centralised log management and alerting.",
    ],
}

RESET = "\033[0m"
BOLD  = "\033[1m"
CYAN  = "\033[96m"
WHITE = "\033[97m"


# ─── Helpers ────────────────────────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_risk_level(score):
    for (low, high), (label, icon, color) in RISK_LEVELS.items():
        if low <= score <= high:
            return label, icon, color
    return "UNKNOWN", "❓", RESET

def ask_yes_no(question, index, total):
    while True:
        print(f"\n  {CYAN}[{index}/{total}]{RESET} {question}")
        answer = input(f"  {WHITE}Your answer (y/n): {RESET}").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  ⚠️  Please enter 'y' for Yes or 'n' for No.")

def print_separator(char="─", width=60):
    print(f"\n  {CYAN}{char * width}{RESET}")

def print_header():
    clear()
    print(f"""
  {BOLD}{CYAN}╔══════════════════════════════════════════════════════════╗
  ║         IT RISK ASSESSMENT CLI TOOL v1.0                 ║
  ║         Developed by Bidemi Salami                       ║
  ║         ISO 27001 | Cybersecurity | IT Governance        ║
  ╚══════════════════════════════════════════════════════════╝{RESET}
""")


# ─── Core Assessment Logic ──────────────────────────────────────────────────

def run_assessment():
    print_header()
    print(f"  {WHITE}This tool evaluates IT risk across 5 key domains.")
    print(f"  Answer each question honestly for an accurate risk score.{RESET}")
    print_separator()

    org_name = input(f"\n  {WHITE}Enter organisation name (or press Enter to skip): {RESET}").strip()
    if not org_name:
        org_name = "Your Organisation"

    results = {}
    domain_scores = {}

    for domain, questions in RISK_DOMAINS.items():
        print_separator("═")
        print(f"\n  {BOLD}{WHITE}DOMAIN: {domain}{RESET}")
        print_separator()

        yes_count = 0
        total = len(questions)

        for i, (question, _) in enumerate(questions, 1):
            answer = ask_yes_no(question, i, total)
            if answer:
                yes_count += 1

        score = round((yes_count / total) * 100)
        domain_scores[domain] = score
        results[domain] = {"score": score, "answered_yes": yes_count, "total": total}

    return org_name, results, domain_scores


def generate_report(org_name, results, domain_scores):
    overall_score = round(sum(domain_scores.values()) / len(domain_scores))
    risk_label, risk_icon, risk_color = get_risk_level(overall_score)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    clear()
    print_header()
    print(f"  {BOLD}{WHITE}RISK ASSESSMENT REPORT{RESET}")
    print(f"  Organisation : {org_name}")
    print(f"  Date         : {timestamp}")
    print_separator("═")

    print(f"\n  {BOLD}DOMAIN SCORES{RESET}\n")
    for domain, data in results.items():
        score = data["score"]
        label, icon, color = get_risk_level(score)
        bar_filled = int(score / 5)
        bar = "█" * bar_filled + "░" * (20 - bar_filled)
        print(f"  {icon} {WHITE}{domain[:42]:<42}{RESET}")
        print(f"     [{color}{bar}{RESET}] {color}{score}% — {label}{RESET}\n")

    print_separator("═")
    print(f"\n  {BOLD}OVERALL RISK SCORE{RESET}")
    print(f"\n  {risk_color}{BOLD}  {risk_icon}  {overall_score}% — {risk_label} RISK{RESET}\n")
    print_separator("═")

    # Recommendations for low-scoring domains
    weak_domains = {d: s for d, s in domain_scores.items() if s < 70}
    if weak_domains:
        print(f"\n  {BOLD}{WHITE}PRIORITY RECOMMENDATIONS{RESET}\n")
        for domain in sorted(weak_domains, key=weak_domains.get):
            print(f"  {BOLD}{CYAN}▸ {domain}{RESET}")
            for rec in RECOMMENDATIONS.get(domain, []):
                print(f"    • {rec}")
            print()
    else:
        print(f"\n  {BOLD}✅ Strong security posture across all domains.{RESET}")
        print(f"  Continue regular reviews and maintain current controls.\n")

    print_separator("═")

    # Export option
    export = input(f"\n  {WHITE}Export report to JSON? (y/n): {RESET}").strip().lower()
    if export == "y":
        export_report(org_name, results, overall_score, risk_label, timestamp)

    print(f"\n  {CYAN}Assessment complete. Stay secure.{RESET}\n")


def export_report(org_name, results, overall_score, risk_label, timestamp):
    filename = f"risk_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    report_data = {
        "organisation": org_name,
        "timestamp": timestamp,
        "overall_score": overall_score,
        "overall_risk_level": risk_label,
        "domain_results": results,
    }
    with open(filename, "w") as f:
        json.dump(report_data, f, indent=4)
    print(f"\n  ✅ Report saved to: {CYAN}{filename}{RESET}")


# ─── Entry Point ─────────────────────────────────────────────────────────────

def main():
    try:
        org_name, results, domain_scores = run_assessment()
        generate_report(org_name, results, domain_scores)
    except KeyboardInterrupt:
        print(f"\n\n  {CYAN}Assessment cancelled. Goodbye.{RESET}\n")


if __name__ == "__main__":
    main()
