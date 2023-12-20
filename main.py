import requests
import time, datetime
import json

with open("config.json") as f:
    config = json.load(f)

partnerUserId = str(config.get("partnerUserId"))
discordUserId = str(config.get("discordUserId"))

url = "https://api.discord.gx.games/v1/direct-fulfillment"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-F946U Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36 OPX/2.2",
    "Content-Type": "application/json",
}

data = {
    "partnerUserId": partnerUserId
}

def log(text):
    timestamp = datetime.datetime.utcfromtimestamp(time.time()).strftime("%H:%M:%S")
    print(f"[{timestamp}] {text}")

while True:
    try:
        with requests.session() as session:
            response = session.post(url, headers=headers, json=data)

        if response.status_code == 200:
            json_response = response.json()
            
            token = json_response.get("token", "")
            
            if token:
                with open("links.txt", "a") as file:
                    file.write(f"https://discord.com/billing/partner-promotions/{discordUserId}/"+token+"\n")
                    log("Nitro generated")
            else:
                log("Nitro token not found")
        else:
            log(f"Error > {response.status_code}\n{response.text}")
    except:
        log("Something went wrong")