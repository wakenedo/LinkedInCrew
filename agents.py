from crewai import Agent
from textwrap import dedent
from tools.linkedin_scraper import scrape_linkedin_posts_tool  # Fixed path
from tools.search_tool import scrape_website_tool, search_tool  # Ensure these exist
from config import OPENAI_API_KEY  # Import API key safely
from your_llm_module import openai_llm  # Ensure LLM is correctly imported

doppelganger_agent = Agent(
    role="LinkedIn Post Creator",
    goal="Create a LinkedIn post comparing LLaMA 2 and LLaMA 3, following the writing style of scraped LinkedIn posts.",
    backstory=dedent("""
        You are a skilled content creator with experience in writing engaging posts on LinkedIn.
        You have a deep understanding of the latest trends in machine learning and natural language processing.
        Your writing style adapts seamlessly to match the tone and style of existing content.
    """),
    verbose=True,
    allow_delegation=False,
    llm=openai_llm
)

linkedin_scraper_agent = Agent(
    role="LinkedIn Post Scraper",
    goal="Scrape LinkedIn profiles and retrieve posts.",
    tools=[scrape_linkedin_posts_tool],
    backstory=dedent("""
        You are an expert in web scraping, specializing in LinkedIn data extraction.
        You use advanced techniques to gather relevant insights without triggering security measures.
    """),
    verbose=True,
    allow_delegation=False,
    llm=openai_llm
)

web_researcher_agent = Agent(
    role="Web Researcher",
    goal="Search for relevant content comparing LLaMA 2 and LLaMA 3.",
    tools=[scrape_website_tool, search_tool],
    backstory=dedent("""
        You are a skilled web researcher with expertise in finding relevant content on the internet.
        You specialize in search engines and automated web scraping to collect high-quality data.
    """),
    verbose=True,
    allow_delegation=False,
    llm=openai_llm
)
