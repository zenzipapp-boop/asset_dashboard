#!/usr/bin/env python3
"""Start the Asset Audit System server."""

import subprocess
import sys
import webbrowser
import time
import os
from pathlib import Path

print("\n" + "=" * 60)
print("  ASSET AUDIT SYSTEM - STARTUP")
print("=" * 60 + "\n")

# Git: Fetch latest updates from GitHub
print("[*] Checking for updates from GitHub...")
try:
    result = subprocess.run(
        ["git", "pull", "origin", "main"],
        capture_output=True,
        text=True,
        timeout=10
    )
    
    if result.returncode == 0:
        if "Already up to date" not in result.stdout:
            print("[OK] Updates pulled! Restarting with new version...")
            print()
            # Restart the script with updated code
            os.execv(sys.executable, [sys.executable, __file__])
        else:
            print("[OK] Already up to date\n")
    else:
        print("[!] Git pull failed (no remote configured?). Continuing anyway...\n")
except Exception as e:
    print(f"[!] Could not check for updates: {e}\n")

# Install dependencies
print("[*] Installing dependencies...")
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"])

# Check database exists
if not Path("assets.db").exists():
    print("[!] Warning: assets.db not found. Please ensure the database file is present.")
    sys.exit(1)

print("\n[OK] Starting FastAPI server on http://localhost:8000\n")
print("Web UI will open automatically in your browser...")
print("API docs available at: http://localhost:8000/docs\n")

# Wait a moment and open browser
def open_browser():
    time.sleep(2)
    try:
        webbrowser.open("http://localhost:8000")
    except Exception:
        print("Note: Could not open browser automatically.")
        print("Please visit: http://localhost:8000")

import threading
thread = threading.Thread(target=open_browser, daemon=True)
thread.start()

# Run server
try:
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
except KeyboardInterrupt:
    print("\n\n[OK] Servers  stopped\n")
