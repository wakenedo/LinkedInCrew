from crewai import Crew
from agents import linkedin_scraper_agent, web_researcher_agent, doppelganger_agent
from tasks import scrape_linkedin_task, web_research_task, create_linkedin_post_task

# Define the Crew with agents and tasks
crew = Crew(
    agents=[
        linkedin_scraper_agent,
        web_researcher_agent,
        doppelganger_agent
    ],
    tasks=[
        scrape_linkedin_task,
        web_research_task,
        create_linkedin_post_task
    ]
)

if __name__ == "__main__":
    crew.kickoff()  # Start executing the workflow
