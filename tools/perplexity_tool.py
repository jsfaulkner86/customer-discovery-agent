import httpx
from config.settings import settings

def research_patient_signals(query: str) -> str:
    headers = {"Authorization": f"Bearer {settings.perplexity_api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are a patient experience and market research analyst for women's health. Monitor Reddit communities, patient forums, app store reviews, and social media for: unmet needs, care gaps, frustrations with existing solutions, emerging health concerns, and shifts in patient language. Classify each signal as: UNMET NEED, CARE GAP, PRODUCT FRUSTRATION, EMERGING TREND, or SENTIMENT SHIFT. Always cite the source URL and date."},
            {"role": "user", "content": query},
        ],
    }
    resp = httpx.post("https://api.perplexity.ai/chat/completions", json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]
