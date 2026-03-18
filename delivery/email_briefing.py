import resend
from config.settings import settings
resend.api_key = settings.resend_api_key
def send_discovery_briefing(email, name, html, period):
    resend.Emails.send({"from": settings.discovery_from_email, "to": email, "subject": f"Customer Discovery Intelligence — {period}",
        "html": f"<html><body style='font-family:sans-serif;max-width:700px;margin:auto'><h2 style='color:#1a237e'>👁️ Customer Discovery Briefing</h2><p>{period} — {name}</p><hr/>{html}<hr/><p style='font-size:12px;color:#999'>The Faulkner Group Advisors</p></body></html>"})
