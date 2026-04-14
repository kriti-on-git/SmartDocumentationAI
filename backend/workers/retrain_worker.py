import time
from ingestion.ingest_docs import ingest
from app.config import settings


def worker():

    while True:

        print("Running ingestion cycle...")
        ingest()

        time.sleep(settings.INGEST_INTERVAL)