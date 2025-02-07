from crewai import Task
from textwrap import dedent
from agents import linkedin_scraper_agent, web_researcher_agent, doppelganger_agent

scrape_linkedin_task = Task(
    description=dedent("Scrape a LinkedIn profile and retrieve a list of relevant posts."),
    expected_output="A list of LinkedIn posts from the given profile.",
    agent=linkedin_scraper_agent,
)

web_research_task = Task(
    description=dedent("Find and summarize high-quality comparisons between LLaMA 2 and LLaMA 3."),
    expected_output="A research summary comparing LLaMA 2 and LLaMA 3.",
    agent=web_researcher_agent,
)

create_linkedin_post_task = Task(
    description=dedent("Create a LinkedIn post comparing LLaMA 2 and LLaMA 3, following the scraped writing style."),
    expected_output="A LinkedIn post in the same style as the scraped posts, comparing LLaMA 2 and LLaMA 3.",
    agent=doppelganger_agent,
)
