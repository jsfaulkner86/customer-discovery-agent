from crewai import Agent

DISCOVERY_STRUCTURE = """
## 🔥 Top Unmet Needs (highest frequency patient pain points this cycle)
## 🚨 Competitor Vulnerabilities (what patients hate about existing solutions)
## 📈 Emerging Trends (new signals that weren't present last cycle)
## 🗣️ Patient Language Glossary (exact words patients use — for marketing copy)
## 💡 Product & Roadmap Implications (what these signals mean for the founder's product)
## 🎯 Narrative Opportunities (patient stories that strengthen fundraising narrative)
"""

discovery_synthesizer = Agent(
    role="Customer Discovery Briefing Synthesizer",
    goal="Synthesize all patient signals into a structured briefing that directly connects voice-of-patient intelligence to product roadmap, marketing copy, and fundraising narrative opportunities.",
    backstory="You bridge the gap between what patients say and what founders build. Every signal you surface comes with a 'so what' for the founder's product, pitch, or go-to-market.",
    tools=[], verbose=True, allow_delegation=False,
)
DISCOVERY_PROMPT = DISCOVERY_STRUCTURE
