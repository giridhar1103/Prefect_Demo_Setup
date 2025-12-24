from datetime import datetime, UTC
from prefect import flow, task

@task(retries=2, retry_delay_seconds=30)
def fetch_data():
    print(f"[{datetime.now(UTC)}] hello from EC2!")
    return "ok"

@flow(log_prints=True)
def prefect_flow():
    fetch_data()

if __name__ == "__main__":
    prefect_flow()


