import subprocess
from pathlib import Path

TEMP_FILE = Path("temp_script.js")

def run_script(code: str):
    TEMP_FILE.write_text(code)
    try:
        result = subprocess.run(["node", str(TEMP_FILE)],
                                capture_output=True, text=True, timeout=30)
        success = result.returncode == 0
        return success, result.stdout + "\n" + result.stderr
    except Exception as e:
        return False, str(e)
