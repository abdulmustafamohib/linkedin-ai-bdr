import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_job(job_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert recruiter. Summarize job descriptions clearly."},
                {"role": "user", "content": f"Summarize the following job description:\n\n{job_text}"}
            ],
            temperature=0.5,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"[LLM Error] {e}")
        return "Summary unavailable due to error."
