# HanseMerkur B2C Authentication Flow Analysis & Automation (PoC)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Purpose](https://img.shields.io/badge/Purpose-Educational%20%2F%20PoC-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview

This repository contains an educational Proof of Concept (PoC) focused on analyzing a Microsoft B2C authentication workflow at the HTTP, session, and protocol layers.

The project explores how multi-step identity flows maintain authentication state across requests, including session cookies, CSRF-related state, transaction state, email verification, OTP validation, and phone-factor verification.

The implementation uses Python HTTP tooling rather than relying exclusively on browser automation, making the project useful for studying request sequencing, state propagation, response handling, and protocol-level debugging.

> **Note to Recruiters & Reviewers:** This project demonstrates practical experience with Python HTTP engineering, authentication-flow analysis, session-state management, CSRF-related request handling, API integration, OTP workflows, concurrency, and protocol-level debugging. It is presented as an educational security-research exercise for authorized testing and identity-engineering study.

## 🔄 Authentication Workflow

```text
B2C Authorization
        │
        ▼
Session / CSRF State Handling
        │
        ▼
Email Provisioning
        │
        ▼
Email Verification Request
        │
        ▼
OTP Retrieval & Validation
        │
        ▼
Authentication State Transition
        │
        ▼
Phone-Factor Selection
        │
        ▼
Phone Verification Workflow
```

## 🚀 Technical Highlights

### Authentication State Management

- Tracks dynamic authentication state across a multi-step B2C workflow.
- Handles session cookies and flow-specific state values.
- Maintains request sequencing between authentication stages.
- Demonstrates HTTP-level state propagation without depending exclusively on a browser.

### CSRF & Request Protection

- Extracts and propagates CSRF-related state used by the authentication flow.
- Sends state-bound request headers and parameters across verification steps.
- Demonstrates how request context changes throughout a multi-stage identity workflow.

### OTP Workflow Integration

- Integrates with the Mail.tm API for controlled mailbox provisioning.
- Uses Bearer-token authentication for mailbox access.
- Polls the inbox for verification messages.
- Extracts verification codes programmatically using structured parsing and regular expressions.

### Phone-Factor Workflow

- Models the transition from email verification to a phone-factor step.
- Demonstrates the request structure and state handling associated with phone verification.
- Uses configurable test input data for controlled research environments.

### Concurrent HTTP Workflows

- Uses Python threading to execute independent workflow instances.
- Maintains session-scoped state for each workflow.
- Demonstrates practical concurrency considerations in HTTP automation and testing.

### Network Routing

- Supports configurable HTTP/SOCKS proxy routing.
- Allows controlled network experimentation through external configuration.
- Keeps routing configuration separate from the authentication workflow logic.

## 🧠 Engineering Focus

- Identity & Authentication
- Microsoft B2C / CIAM concepts
- HTTP session management
- Authentication state management
- CSRF & request-state analysis
- OTP / MFA workflow modeling
- API integration
- Concurrent HTTP workflows
- Protocol-level debugging
- Security testing in authorized environments

## 🛠️ Technology Stack

- **Python 3.8+**
- **Requests**
- **BeautifulSoup**
- **Mail.tm API**
- **Python threading**
- **Regular expressions**
- **HTTP/SOCKS proxy support**

## 📂 Project Structure

```text
.
├── b2c01hansemerkur.py
├── phone.txt
├── vpn.txt
├── README.md
└── .gitignore
```

### Core files

- `b2c01hansemerkur.py` — Main HTTP authentication-flow analysis and automation implementation.
- `phone.txt` — External test input used by the phone-factor workflow.
- `vpn.txt` — Optional network-routing configuration for controlled testing.
- `README.md` — Project documentation and security-research context.

## ⚙️ Setup

Install the required Python packages:

```bash
pip install requests beautifulsoup4 names phonenumbers pycountry phone-iso3166
```

Configure the required test inputs in the appropriate local files before execution.

Run:

```bash
python b2c01hansemerkur.py
```

The program requests the desired number of concurrent workflow threads at runtime.

## 🔍 What This Project Demonstrates

This PoC is primarily valuable as an example of **protocol-level identity engineering** rather than a conventional browser automation project.

It demonstrates:

- Maintaining state across complex HTTP request sequences
- Working with cookies and authentication state
- Handling CSRF-related request requirements
- Integrating external APIs into authentication workflows
- Parsing verification messages and OTP values
- Managing concurrent HTTP sessions
- Debugging multi-step authentication protocols
- Separating network-routing configuration from workflow logic

## ⚠️ Security Research Disclaimer

This project is provided strictly as an educational Proof of Concept for studying identity, authentication, HTTP session management, and security engineering concepts.

Testing must only be performed against systems for which the tester has explicit authorization. The project is not intended to bypass security controls, create unauthorized accounts, abuse authentication systems, send unauthorized verification traffic, or violate service Terms of Use.

The techniques demonstrated here should be applied only to owned systems, local labs, or explicitly authorized security-testing environments.

## 📝 License

&copy; 2026 dev-nayef. All rights reserved.
