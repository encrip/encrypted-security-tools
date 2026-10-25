# 🛡️ Encrypted Security Tools

**A Python-Based Cybersecurity Learning & Security Automation Toolkit**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![Security](https://img.shields.io/badge/Focus-Cybersecurity-green)

## 📖 About the Project

**Encrypted Security Tools** is an open-source cybersecurity learning and development project focused on building practical security tools using Python.

The goal is to improve skills in network security, ethical hacking, web application security, digital forensics, and security automation through hands-on development.

Each tool is developed as a separate project, with the long-term goal of creating a complete cybersecurity toolkit.

## 🎯 Project Objectives

- Learn cybersecurity through practical Python projects.
- Understand computer networks and common security vulnerabilities.
- Build tools for security testing, monitoring, and analysis.
- Develop skills in penetration testing and digital forensics.
- Improve Python programming and software engineering skills.
- Create reusable and well-documented security utilities.
- Build a professional cybersecurity development portfolio.

## 🚀 Project Roadmap

| # | Security Tool | Status |
|---|---|---|
| 01 | TCP Port Scanner | 🚧 In Progress |
| 02 | Password Strength Analyzer | 📌 Planned |
| 03 | IP Address & Subnet Calculator | 📌 Planned |
| 04 | DNS Lookup Tool | 📌 Planned |
| 05 | HTTP Security Header Checker | 📌 Planned |
| 06 | Network Device Discovery | 📌 Planned |
| 07 | Packet Analyzer | 📌 Planned |
| 08 | SSL/TLS Certificate Checker | 📌 Planned |
| 09 | Web Security Scanner | 📌 Planned |
| 10 | File Integrity Monitor | 📌 Planned |
| 11 | Firewall Log Analyzer | 📌 Planned |
| 12 | Security Event Monitor | 📌 Planned |
| 13 | Phishing URL Analyzer | 📌 Planned |
| 14 | Digital Forensics Toolkit | 📌 Planned |
| 15 | Encrypted Security Suite | 📌 Planned |

## 📂 Project Structure

```text
encrypted-security-tools/
│
├── README.md
├── .gitignore
│
└── port-scanner/
    └── scanner.py
```

Additional project directories will be introduced as development progresses.

## 🔍 Project 01: TCP Port Scanner

The first tool is a simple Python TCP port scanner designed to check whether selected TCP ports accept connections on an authorized host.

### Features

- TCP connection scanning
- Common network port inspection
- Configurable connection timeout
- Open port detection
- Basic error handling
- Python standard library implementation

### Technologies

- Python 3
- Socket Programming
- TCP/IP Networking

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/encrypted-security-tools.git
```

**2. Navigate to the project**

```bash
cd encrypted-security-tools/port-scanner
```

**3. Run the scanner**

```bash
python scanner.py
```

No third-party Python packages are required for the initial scanner.

### Example Output

The following is an illustrative output from a host with a listening service on port 8080:

```text
Scanning 127.0.0.1

[CLOSED/FILTERED] Port 21
[CLOSED/FILTERED] Port 22
[CLOSED/FILTERED] Port 80
[CLOSED/FILTERED] Port 443
[CLOSED/FILTERED] Port 3306
[OPEN] Port 8080

Scan completed.
```

**Note:** A failed TCP connection does not always distinguish a closed port from a filtered or unreachable port.

## 🧠 Learning Areas

This repository focuses on:

- Python for Cybersecurity
- Network Security
- Linux Administration
- TCP/IP and Network Protocols
- Web Application Security
- API Security Testing
- Security Automation
- Digital Forensics
- Vulnerability Assessment
- Defensive Security Monitoring

## 🗺️ Development Phases

### Phase 1 — Foundations

Python, networking fundamentals, Linux, sockets, and basic security utilities.

### Phase 2 — Network Security

Port scanning, service inspection, packet analysis, and network inventory.

### Phase 3 — Web Security

HTTP security, TLS analysis, authentication testing, and authorized web security assessments.

### Phase 4 — Security Automation

File monitoring, event analysis, detection rules, and automated reporting.

### Phase 5 — Digital Forensics

File hashing, evidence collection, system artifacts, and incident investigation.

### Phase 6 — Complete Security Platform

Combine the developed tools into an integrated security platform using Python, FastAPI, a database, and a web dashboard.

## ⚠️ Legal & Ethical Disclaimer

This repository is intended for **education, defensive security research, and authorized security testing only**.

Use these tools only on systems, networks, and applications that you own or have explicit permission to assess.

The project does not encourage unauthorized access, disruption, or malicious activity.

## 🤝 Contributions

Contributions, improvements, suggestions, and bug reports are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your implementation.
5. Submit a pull request.

## 👨‍💻 Developer

**Encrypted Team**

Cybersecurity Enthusiast | Network Engineer | Python Developer | Security Tool Developer

GitHub: https://github.com/encrip

## ⭐ Support the Project

If you find this repository useful, consider giving it a star on GitHub.

**Learn. Build. Test. Secure.**

*Encrypted Security Tools — Building Security Through Code.*
