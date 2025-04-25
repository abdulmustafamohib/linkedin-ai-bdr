import requests
import os
from dotenv import load_dotenv

load_dotenv()
HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")

# You can replace this map with a real domain-resolver API later
HARDCODED_DOMAINS = {
    "Google": "google.com",
    "Meta": "meta.com",
    "Amazon": "amazon.com",
    "OpenAI": "openai.com",
    "Salesforce": "salesforce.com"
}

def extract_domain(company_name):
    return HARDCODED_DOMAINS.get(company_name)

def get_hiring_contacts(domain):
    if not domain:
        return []

    try:
        url = "https://api.hunter.io/v2/domain-search"
        params = {"domain": domain, "api_key": HUNTER_API_KEY}
        res = requests.get(url, params=params)
        res.raise_for_status()
        emails = res.json().get("data", {}).get("emails", [])

        hiring_keywords = ["talent", "recruit", "hr", "hiring", "people"]
        filtered = [
            {
                "name": (e.get("first_name", "") + " " + e.get("last_name", "")).strip(),
                "email": e.get("value"),
                "position": e.get("position", "")
            }
            for e in emails
            if any(kw in (e.get("position") or "").lower() for kw in hiring_keywords)
        ]
        return filtered

    except Exception as e:
        print(f"[Enrichment Error] for {domain}: {e}")
        return []
