import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

PROXYCURL_API_KEY = os.getenv("PROXYCURL_API_KEY")

def scrape_jobs(role, location):
    url = "https://nubela.co/proxycurl/api/linkedin/job"
    params = {
        "role": role,
        "location": location,
    }
    headers = {
        "Authorization": f"Bearer {PROXYCURL_API_KEY}"
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    jobs = response.json()

    os.makedirs("data", exist_ok=True)
    with open("data/jobs_raw.json", "w") as f:
        json.dump(jobs, f, indent=2)

    print(f"Fetched {len(jobs)} jobs and saved to data/jobs_raw.json")

if __name__ == "__main__":
    scrape_jobs("Software Engineer", "Toronto")
