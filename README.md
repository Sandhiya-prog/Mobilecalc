# 📱 Calculator Automation Project (Appium + Behave + Python)

This project automates a basic Android calculator app using **Appium**, **Behave (BDD)**, and **Python** with a clean **Page Object Model (POM)** structure. It simulates user actions like performing arithmetic operations and verifies expected outcomes.

---

## 🔧 Tools & Technologies Used

- 🐍 Python
- 📱 Appium
- 🧪 Behave (BDD framework)
- 🧱 Page Object Model (POM)
- 📲 Android Emulator / Device
- 💻 PyCharm / VSCode

---

## 📁 Project Structure
calculator_automation/ │ ├── features/ │ ├── calculator.feature # BDD test scenarios written in Gherkin │ └── steps/ │ └── step_definitions.py # Step definitions matching Gherkin steps │ ├── pages/ │ └── calculator_page.py # Page Object Model class for UI elements │ ├── environment.py # Behave environment hooks (before_all, after_all, etc.) ├── requirements.txt # Python dependencies ├── config/ # (Optional) YAML or JSON files if needed │ └── README.md # Project overview and instructions

## 🚀 How to Run the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt

2. Set Android SDK Environment Variables
Make sure the following variables are set in your system:

For Windows:

ANDROID_HOME – path to Android SDK

Add to PATH:
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\emulator
%ANDROID_HOME%\tools\bin

For Mac/Linux:

bash
Copy
Edit
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
3. Start Appium Server
Use Appium Desktop or start it from terminal:

bash
Copy
Edit
appium
4. Run Tests
bash
Copy
Edit
behave
⚠️ Known Issue
Due to a temporary SDK environment setup issue, the automation test may not run successfully in the current local environment. The code structure and logic are complete and ready for execution once the system variables are fixed. The code runs in another system where SDK environment is set .


