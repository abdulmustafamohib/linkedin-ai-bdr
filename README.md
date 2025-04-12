# AI BDR Automation Platform 🧠📬

An automated business development (BDR) pipeline that scrapes job postings, performs LLM-based company and role analysis, generates synthetic candidate profiles, and sends customized outreach messages — all in one streamlined workflow.

## ✨ Features

- 🔍 Scrape job postings from LinkedIn using Proxycurl API
- 🧠 Use GPT-4 to analyze role descriptions and generate relevant candidate personas
- 📇 Enrich profiles with Apollo API and auto-match them to roles
- ✉️ Send hyper-personalized cold emails via Instantly or LinkedIn
- 📊 Track and visualize leads & messaging via Firebase dashboard

## 🧰 Tech Stack

- **LLMs**: GPT-4 via OpenAI API
- **Frontend**: TypeScript, Next.js
- **Backend**: Python, Node.js
- **Automation**: Clay, Instantly, Apollo
- **Database**: Firebase
- **APIs**: Proxycurl, Clay, Apollo

## 📦 Setup

1. Clone the repo
2. Install dependencies: `npm install` / `pip install -r requirements.txt`
3. Set your API keys in `.env`
4. Run with: `npm run dev` or `python main.py`

## 🎯 Impact

- 5x faster than manual BDR research
- Processed 500+ job roles and 200+ targeted messages in test runs
- Competing for a $7,500 prize at Neolific AI venture challenge

## 🧠 Future Plans

- Add analytics for message open/response rates
- Integrate with CRM (e.g., Hubspot, Airtable)
- Auto-sync candidate tracking sheet
