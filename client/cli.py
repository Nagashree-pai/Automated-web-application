import requests
import os
from datetime import datetime

LOG_DIR = "logs"

def save_log(content: str) -> str:
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(LOG_DIR, f"log_{timestamp}.txt")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(content)
    return log_path

def main():
    print("💬 Your Command (or 'exit'):")
    while True:
        cmd = input("» ").strip()
        if cmd.lower() == "exit":
            break
        try:
            res = requests.post("http://localhost:8000/execute", json={"prompt": cmd})
            result = res.json()
            success = result.get("success", False)
            log = result.get("log", "No output")
            log_file_path = save_log(log)

            print("✅ Success:" if success else "❌ Failed")
            print(f"📄 Log saved to {log_file_path}")
        except Exception as e:
            print("⚠️ Error:", str(e))

if __name__ == "__main__":
    main()


# ollama run mistral:7b-instruct
# uvicorn server.main:app --reload --port 8000