# 🛡️ CyberGuardInnovations — Python Threat Detection & User Authentication

A lightweight Python-based CLI system for **user management** and **threat detection**. This tool provides a foundational framework for basic cybersecurity applications, educational purposes, or prototyping.

---

## 🔍 Features

- 🔐 User Registration & Authentication
- ⚠️ Real-time Threat Detection Logging
- 📄 Display of Detected Threats

---

## 🧑‍💻 How It Works

The core functionality is handled via a Python class:

### 📦 `CyberGuardInnovations` Class

- `register_user(username, password)`  
  Adds a new user to the system.

- `authenticate_user(username, password)`  
  Verifies login credentials.

- `detect_threat(threat_type)`  
  Logs a new security threat.

- `display_detected_threats()`  
  Outputs a list of all detected threats.

---

## ▶️ Example Usage

```python
cyber_guard = CyberGuardInnovations()

cyber_guard.register_user("user1", "password123")

if cyber_guard.authenticate_user("user1", "password123"):
    print("User authentication successful.")
else:
    print("User authentication failed.")

cyber_guard.detect_threat("Malware")
cyber_guard.detect_threat("Phishing")

cyber_guard.display_detected_threats()
```

### 💻 Output

```
User authentication successful.
Detected Threats:
-  Malware
-  Phishing
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x installed

### ▶️ Run the script

```bash
python cyber_guard.py
```

> Replace `cyber_guard.py` with your actual filename if different.

---

## 📁 File Structure

```
cyberguard/
├── cyber_guard.py     # Main script
└── README.md          # Project documentation
```

---

## 💡 Use Cases

- 👩‍💻 Educational demonstration for user systems
- 🧪 Testing basic security logic
- 🛠️ Prototype for extended cybersecurity tools

---

## 📣 Feedback

Have ideas for improvements or features?  
Feel free to fork this project, suggest enhancements, or open an issue!

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
