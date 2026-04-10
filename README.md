# 🔐 Password Security Analysis & Brute Force Attack Simulation
# CSCI 400 Cybersecurity Capstone Project
The goal is to simulate real-world password attacks in a controlled lab environment and measure how different security implementations impact resistance to brute-force and dictionary attacks. This project is significant because weak password storage remains one of the most exploited vulnerabilities in modern web applications.

# 📌 Project Overview
This project simulates real-world password attacks in a controlled lab environment and evaluates how different password storage mechanisms impact resistance to brute-force and dictionary attacks. The project demonstrates both offline password cracking and online brute-force attack simulations.
The goal is to analyze the effectiveness of different hashing techniques and demonstrate detection and prevention mechanisms for brute-force attacks.

# 🎯 Objectives
- Simulate real-world password attacks
- Compare different hashing algorithms
- Perform offline password cracking
- Simulate online brute-force login attacks
- Implement detection mechanisms
- Demonstrate prevention and mitigation strategies

# 🛠️ Technologies & Tools
# Tools
- Burp Suite
- John the Ripper
- Python
- SQLite
- Linux (VMware)
# 🌐 Web Application
- GroceryGo Web Application
- React Frontend
- Firebase Authentication
# 🔐 Methods used
- SHA-256 hashing
- Salted SHA-256
- bcrypt hashing
- BurpSuite Brute-force attacks
- Dictionary attacks
- Login monitoring

# 📂 Project Structure
Project-/Password Security Analysis & Brute Force Attack Simulation/
│
├── password_cracking_lab/
│   ├── sha256/
│   ├── salted_sha256/
│   ├── bcrypt/
│
├── scripts/
│   ├── hash_passwords.py
│   ├── salted_hash.py
│   ├── bcrypt_hash.py
│
├── wordlists/
│   ├── rockyou.txt
|   ├── Wordslist.txt
│
├── reports/
│   ├── offline_attack_results
│   ├── online_attack_results
│
└── README.md

# 🔓 Part 1 — Offline Password Cracking
- SHA-256 (Unsalted)
- Fast hashing
- Weak security
- Easily cracked using dictionary attacks

Tools Used

- John the Ripper
- rockyou.txt

# 🧂 Salted SHA-256
- Salt added to password
- Slower cracking
- Improved security
# 🔒 bcrypt Hashing
- Adaptive hashing
- Cost factor = 12
- Strongest security tested
- Slow brute-force attempts

# 🌐 Part 2 — Online Brute Force Attack
# Attack Method:
Burp Suite Intruder was used to simulate repeated login attempts against the GroceryGo authentication system.

# Steps
Capture login request
Send request to Intruder
Configure payload positions
Load wordlist
Start attack
Analyze results

# 📊 Results
| Method         | Security Level | Attack Difficulty |
| -------------- | -------------- | ----------------- |
| SHA-256        | Weak           | Easy              |
| Salted SHA-256 | Medium         | Moderate          |
| bcrypt         | Strong         | Difficult         |

# 📸 Screenshots
- SHA256 cracking results
- Salted hashing results
- bcrypt cracking results
- Burp Suite Intruder attack
- Login detection results

# 📚 Learning Outcomes
- Password hashing techniques
- Offline password cracking
- Online brute-force attacks
- Detection mechanisms
- Burp Suite Intruder usage
- Security implementation strategies
