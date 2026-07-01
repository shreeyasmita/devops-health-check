import os, psutil, datetime

def log_health():
    now = datetime.datetime.now()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log_path = os.path.join("/app", "health.log")
    with open(log_path, "a") as f:
        f.write(f"{now} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%\n")

if __name__ == "__main__":
    log_health()
