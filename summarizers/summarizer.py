import os
import sys

# 👇 Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.llm_client import summarize_job
from enrichers.enrichment import extract_domain, get_hiring_contacts
import json


RAW_PATH = "data/jobs_raw.json"
OUT_PATH = "data/jobs_enriched.json"

def process_all_jobs():
    with open(RAW_PATH, "r") as f:
        jobs = json.load(f)

    results = []

    for i, job in enumerate(jobs):
        print(f"\n⏳ Processing job {i+1}/{len(jobs)}...")

        description = job.get("description") or str(job)
        summary = summarize_job(description)

        company = job.get("company_name")
        domain = extract_domain(company)
        contacts = get_hiring_contacts(domain) if domain else []

        results.append({
            "original": job,
            "summary": summary,
            "contacts": contacts
        })

    os.makedirs("data", exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n✅ Done: summarized and enriched {len(results)} jobs into {OUT_PATH}")

if __name__ == "__main__":
    process_all_jobs()
