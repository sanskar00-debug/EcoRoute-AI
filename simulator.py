import time
import random
import requests

TARGET_URL = "http://127.0.0.1:5000/api/telemetry"

virtual_bins = [
    {"bin_id": 1, "fill_level": 45.0},
    {"bin_id": 2, "fill_level": 20.0},
    {"bin_id": 3, "fill_level": 70.0}
]

print("🚀 EcoRoute AI: Simulator Started...")

try:
    while True:
        for bin_node in virtual_bins:
            increment = round(random.uniform(1.0, 4.0), 2)
            bin_node["fill_level"] = min(100.0, bin_node["fill_level"] + increment)
            
            payload = {"bin_id": bin_node["bin_id"], "fill_level": bin_node["fill_level"]}
            
            try:
                response = requests.post(TARGET_URL, json=payload, timeout=2)
                if response.status_code == 200:
                    print(f"📡 Data Sent -> Bin #{bin_node['bin_id']} is at {bin_node['fill_level']}%")
                else:
                    print(f"⚠️ Server returned error: {response.status_code}")
            except Exception:
                print("❌ Cannot connect to server. Check if main.py is running on port 5000!")
        
        print("-" * 40)
        time.sleep(3)
except KeyboardInterrupt:
    print("\n🛑 Stopped.")