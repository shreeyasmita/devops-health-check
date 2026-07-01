import psutil
import datetime

def log_health():
    now = datetime.datetime.now()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    with open("health.log", "a") as f:
        f.write(f"{now} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%\n")

if __name__ == "__main__":
    log_health()
