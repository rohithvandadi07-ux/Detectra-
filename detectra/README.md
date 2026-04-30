# 🔐 Detectra

Automated Security Layer for ROS2 Systems

---

## 🚨 Problem
ROS2 systems are vulnerable to:
- Unauthorized nodes
- Fake publishers (message injection)
- No easy security setup

---

## ✅ Solution
Detectra automatically:
- Scans ROS2 workspace
- Generates certificates
- Creates permissions
- Enforces secure communication
- Blocks malicious nodes

---

## ⚙️ Features
- 🔍 Node discovery
- 🔐 Auto keystore generation
- 📜 Policy enforcement
- 🚫 Unauthorized node blocking

---

## 🚀 Usage

python -m detectra.cli secure ~/ros2_ws

---

## 🧠 Tech Stack
- ROS2 Jazzy
- SROS2
- Python

---

## 🔥 Demo

Without Detectra:
HACKED MESSAGE

With Detectra:
SECURITY ERROR (attacker blocked)
