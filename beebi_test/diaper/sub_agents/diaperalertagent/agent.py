from beebi_test.diaper_tools import analyze_diaper_alert
from google.adk.agents import Agent

diaper_alert_agent = Agent(
    name="diaper_alert_agent",
    model="gemini-2.0-flash",
    description="An agent that detects abnormal diaper change patterns, such as consecutive big poos or excessive intervals between changes.",
    instruction="""
    You are a diaper alert agent.
    Your task is to identify abnormal excretion patterns, such as consecutive big poos or excessive time intervals without a change, to help with parent reminders.
    Use the analyze_diaper_alert tool to generate your report.
    """,
    tools=[analyze_diaper_alert],
)