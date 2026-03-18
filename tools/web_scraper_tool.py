import httpx
from bs4 import BeautifulSoup

def scrape_forum_page(url: str) -> str:
    """Scrape a patient forum or community page for discussion signals."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; CustomerDiscoveryAgent/1.0)"}
    resp = httpx.get(url, headers=headers, timeout=15, follow_redirects=True)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    return " ".join(soup.get_text(separator=" ").split())[:6000]
