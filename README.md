# HanseMerkur B2C Authentication Flow Automation (PoC)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Purpose](https://img.shields.io/badge/Purpose-Educational%20%2F%20PoC-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview

This repository contains a Proof of Concept (PoC) Python script designed to navigate and automate complex Microsoft B2C identity and authentication flows. It demonstrates how to programmatically handle dynamic session tokens, CSRF protection, and multi-step verification processes (including OTP) without a headless browser.

> **Note to Recruiters & Reviewers:** This project was developed to showcase advanced skills in HTTP session management, API reverse engineering, concurrency, and automated testing. It highlights a deep understanding of modern web authentication mechanisms.

## 🚀 Technical Highlights & Skills Demonstrated

- **Complex Session Management:** Programmatic extraction and handling of dynamic Microsoft B2C parameters (e.g., `x-ms-cpim-csrf`, `state`, and cookies) using the `requests` library.

- **Automated OTP Verification:** Integration with the (`mail.tm`) disposable email API—utilizing Bearer Authorization Tokens to programmatically provision temporary accounts, continuously poll inboxes, and extract One-Time Passwords (OTP) in real-time using targeted regex.

- **Concurrency & Performance:** Implementation of Python's `threading` modules to run multiple authentication workflows simultaneously, optimizing execution time.

- **Network Routing & Evasion:** Support for proxy integration (HTTP/SOCKS) via a `vpn.txt` configuration to manage rate limiting and IP-based restrictions.

## 🛠️ Prerequisites

- Python 3.8 or higher.

- Required Python packages (install via `pip`):

  ```bash
  pip install requests beautifulsoup4 names selenium phonenumbers pycountry phone-iso3166
  ```

## ⚙️ Setup and Execution

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dev-nayef/HanseMerkur-B2C-Auto-Registrator-Bot.git
   cd HanseMerkur-B2C-Auto-Registrator-Bot
   ```

2. **Configure Proxies (Recommended to bypass IP block security):**
   Add your proxies to a file named `vpn.txt` in the root directory.
   Format: `ip:port` or `username:password@ip:port` (one per line).

3. **Run the automation:**

   ```bash
   python b2c01hansemerkur.py
   ```

## 📂 Project Structure

- `b2c01hansemerkur.py`: The core automation engine handling the B2C requests.

- `vpn.txt`: Configuration file for proxy routing.

- `phone.txt`: Configuration file containing phone number data that will receive the OTP text messages or Phone Verification Calls.

- `README.md`: Project documentation.

## ⚠ Legal & Ethical Disclaimer

**Strictly for Educational and Authorized Testing Purposes.**

This script is provided as a technical demonstration of automating web requests and understanding authentication architecture. The author does not condone, encourage, or support the use of this tool for spam, malicious activities, or violating the Terms of Service of any platform. The creator assumes no liability for any misuse of this software. Use responsibly.

## 📝 License

&copy; 2026 dev-nayef. All rights reserved.
