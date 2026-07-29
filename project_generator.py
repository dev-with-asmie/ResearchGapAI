import arxiv
from google import genai
from dotenv import load_dotenv
import os
import time

# Load API key
load_dotenv()

gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Get topic
topic = input("Enter research topic: ")

print("\nSearching papers...\n")

# arXiv search
search = arxiv.Search(
    query=f'all:"{topic}"',
    max_results=3
)

client = arxiv.Client()

papers = []

for paper in client.results(search):

    papers.append(
        f"""
TITLE:
{paper.title}

ABSTRACT:
{paper.summary[:500]}
"""
    )

paper_text = "\n\n".join(papers)

prompt = f"""
You are an expert research mentor.

Analyze these research papers:

{paper_text}

Tasks:

1. Find the top 3 research gaps.
2. Generate 1 novel project idea for each gap.

For every project provide:

- Project Title
- Problem Solved
- Novelty
- Suggested Dataset
- Tech Stack
- Difficulty (Easy/Medium/Hard)
- Resume Impact Score (1-10)
- Research Potential Score (1-10)

Keep the answer concise and structured.
"""

print("Generating project ideas...\n")

response = None

for attempt in range(3):

    try:

        response = gemini.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        break

    except Exception as e:

        print(f"Attempt {attempt + 1} failed.")

        if attempt < 2:
            print("Retrying in 10 seconds...\n")
            time.sleep(10)
        else:
            print("\nError:")
            print(e)
            exit()

print("\n")
print("=" * 80)
print("PROJECT IDEAS")
print("=" * 80)
print("\n")

print(response.text) 