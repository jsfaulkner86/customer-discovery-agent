from crewai import Crew, Task
from agents.reddit_agent import reddit_agent
from agents.app_review_agent import app_review_agent
from agents.trend_agent import trend_agent
from agents.discovery_synthesizer_agent import discovery_synthesizer, DISCOVERY_PROMPT
from delivery.email_briefing import send_discovery_briefing
from delivery.notion_push import push_to_notion
from db.supabase_client import save_briefing
from profiles.founder_profiles import FOUNDER_PROFILES
from datetime import datetime

def run_pipeline():
    period = datetime.now().strftime("%B %d, %Y")
    for profile in FOUNDER_PROFILES:
        tasks = [
            Task(description=f"Monitor Reddit communities {profile['monitor_communities']} for signals about: {profile['monitor_keywords']}. Focus: {profile['sentiment_focus']}", agent=reddit_agent, expected_output="List of patient signals with classification, quote/summary, community source, and date."),
            Task(description=f"Monitor app store reviews for competitor apps: {profile.get('competitor_apps', [])} in {profile['indication']} category. Surface recurring complaints.", agent=app_review_agent, expected_output="List of competitor vulnerabilities with frequency, exact language, and app name."),
            Task(description=f"Monitor emerging trends in {profile['indication']} women's health across media, TikTok, advocacy groups, and news.", agent=trend_agent, expected_output="List of emerging trends with signal strength, first observed date, and sources."),
            Task(description=f"Synthesize all signals for {profile['founder_name']}.\n{DISCOVERY_PROMPT}", agent=discovery_synthesizer, expected_output="Structured HTML discovery briefing."),
        ]
        crew = Crew(agents=[reddit_agent, app_review_agent, trend_agent, discovery_synthesizer], tasks=tasks, verbose=True)
        result = crew.kickoff()
        result_str = result if isinstance(result, str) else str(result)
        save_briefing({"client_id": profile["client_id"], "period": period, "briefing": result_str})
        push_to_notion(profile["client_id"], profile["founder_name"], result_str, period)
        send_discovery_briefing(profile["email"], profile["founder_name"], result_str, period)
    print("[CustomerDiscoveryAgent] Bi-weekly run complete.")

if __name__ == "__main__":
    run_pipeline()
