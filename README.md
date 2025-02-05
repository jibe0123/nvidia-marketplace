# 🚀 NVIDIA GPU Stock Checker 🟢

This is a Python script that **monitors NVIDIA Marketplace for RTX 5080 and RTX 5090 stock availability** and sends real-time alerts via **Telegram and Discord**.

---

## **⚡ Features**
- ✅ Fetches real-time stock availability from **NVIDIA’s official API**
- ✅ Sends instant **Telegram & Discord notifications** when stock is available
- ✅ Runs **24/7** in the background on macOS
- ✅ Supports **auto-start on macOS boot** using `launchd`
- ✅ **Git-ignored credentials** stored in a separate `config.json` file

---

## **📥 Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/nvidia-stock-checker.git
cd nvidia-stock-checker
```

### **2️⃣ Create a Python Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash

pip install -r requirements.txt
```

### 🔑 Setup API Credentials

1.	Create a config.json file to store API tokens securely:

```bash
nano config.json
```
2.	Add the following and replace with your details:

```bash
{
    "telegram_bot_token": "YOUR_BOT_TOKEN",
    "telegram_chat_id": "YOUR_CHAT_ID",
}
```

