# 🧪 QA Automation Testing - Dashboard Tepak

[![Automation](https://img.shields.io/badge/QA-Automation-blue)](#)
[![Selenium](https://img.shields.io/badge/Tool-Selenium-yellow)](#)
[![Python](https://img.shields.io/badge/Language-Python%203.x-green)](#)
[![License](https://img.shields.io/badge/License-MIT-brightgreen)](#)

Automated UI testing for the website [https://dash.tepak.id](https://dash.tepak.id) using **Selenium WebDriver** and **Python**.  
This project focuses on testing the *Menu Page* and other navigational components of the Dashboard Tepak system.

---

## 📸 Preview
> Sample Test: Check all menu items appear and display names correctly

![Screenshot]

---

## 📂 Project Structure
qa-tepak-automation/
│
├── tests/ # Contains test scripts
│ └── test_menu_page.py
│
├── drivers/ # Contains ChromeDriver
│ └── chromedriver.exe
│
├── reports/ # (Optional) Test results / screenshots
│
├── requirements.txt # Python dependencies
└── README.md # This file

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/qa-tepak-automation.git
cd qa-tepak-automation

2. Install Dependencies


pip install -r requirements.txt

3. Download & Setup ChromeDriver

Download the ChromeDriver matching your browser version from:
https://chromedriver.chromium.org/downloads

Place it in the drivers/ folder.

4. Run Test

python tests/test_menu_page.py
🧪 Test Case Details
Test Case	Description
test_menu_page.py	- Open Menu Page
- Check if menu cards exist
- Print menu names

🔧 Tech Stack
🐍 Python 3.x

🌐 Selenium WebDriver

🧪 Unit test style (or can use pytest optionally)

🖥 Google Chrome

📝 Future support: HTML report, Allure, CI integration

📌 Notes
This test focuses only on UI validation of the /menu page.

You can extend it to test other pages like /customers, /events, or implement login.

Project is ready for conversion to Page Object Model structure.

📄 License
This project is open-source under the MIT License.

🙋‍♀️ Author
Created by @rheaanjani
Feel free to fork, modify, and contribute!
