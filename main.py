import os

import requests
import time
import json

# NVIDIA API Endpoint
API_URL = "https://api.nvidia.partners/edge/product/search?locale=fr-fr&page=1&limit=12&gpu=RTX%205080,RTX%205090&manufacturer=NVIDIA&manufacturer_filter=NVIDIA~2&category=GPU"

# Headers (to mimic a browser request)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://marketplace.nvidia.com/",
    "Origin": "https://marketplace.nvidia.com"
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get script's directory
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")  # Absolute path to config.json

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

TELEGRAM_BOT_TOKEN = config["telegram_bot_token"]
TELEGRAM_CHAT_ID = config["telegram_chat_id"]

def fetch_product_data():
    """Fetch product data from NVIDIA API"""
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise error for bad HTTP response codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching product data: {e}")
        return None


def check_stock():
    """Check if RTX 5080 or RTX 5090 is in stock"""
    data = fetch_product_data()
    if not data:
        return

    products = data.get("searchedProducts", {}).get("productDetails", [])

    for product in products:
        name = product.get("productTitle", "Unknown GPU")
        price = product.get("productPrice", "Unknown Price")
        status = product.get("prdStatus", "out_of_stock")
        link = product.get("internalLink", "")

        if status == "in_stock":
            message = f"🚨 {name} is **IN STOCK**!\n💰 Price: {price}\n🔗 Buy Now: {link}"
            send_telegram_notification(message)
        else:
            print(f"❌ {name} is out of stock.")




def send_telegram_notification(message):
    """Send a notification via Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Telegram notification sent successfully.")
        else:
            print(f"❌ Telegram error: {response.text}")
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")


def main():
    print("🔍 Starting NVIDIA GPU stock checker...")
    while True:
        check_stock()
        time.sleep(60)  # Check every 60 seconds


if __name__ == "__main__":
    main()
