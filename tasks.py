
import os
from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

# Research Task
research_task = Task(
    description = (
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market opportunities, and potential risks."
    ),
    expected_output = "A comprehensive 5 paragraphs long report on the latest AI trends.",
    tools = [tool],
    agent = news_researcher,
)


# Writing Task
write_task = Task(
    description = (
        "Compose and insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This aricle should be easy to understand, engaging and positive."
    ),
    expected_output = "A 5 paragraph article on {topic} advancements formatted as markdown.",
    tools = [tool],
    agent = news_writer,
    async_execution = False,
    output_file = "new-blog-post.md"  # Example pf output customization
)
