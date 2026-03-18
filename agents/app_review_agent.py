from crewai import Agent
from tools.perplexity_tool import research_patient_signals

app_review_agent = Agent(
    role="App Store Review Intelligence Analyst",
    goal="Monitor app store reviews (1-3 star) for competitor products in the founder's category. Surface recurring complaints, unmet feature needs, and trust/safety concerns that represent competitive differentiation opportunities.",
    backstory="Negative app store reviews are a goldmap for product strategy. A competitor's 1-star reviews about 'no real human support' tells a founder exactly what to build and how to market against them.",
    tools=[research_patient_signals], verbose=True, allow_delegation=False,
)
