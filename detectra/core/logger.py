import os
from datetime import datetime

LOG_FILE = os.path.expanduser("~/detectra/detectra.log")


def log_event(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"[{timestamp}] [{level}] {message}"

    # Print to terminal
    print(log_line)

    # Save to file
    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")


def info(message):
    log_event("INFO", message)


def warning(message):
    log_event("WARNING", message)


def alert(message):
    log_event("ALERT", message)


def success(message):
    log_event("SUCCESS", message)