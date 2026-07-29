import arxiv
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

arxiv_client = arxiv.Client()

topic = input("Enter research topic: ")

search = arxiv.Search(
    query=topic,
    max_results=5,
    sort_by=arxiv.SortCriterion.Relevance
)

all_summaries = []

print("\nCollecting papers...\n")

for paper in arxiv_client.results(search):

    all_summaries.append(
        f"""
TITLE:
{paper.title}

ABSTRACT:
{paper.summary}
"""
    )

combined_text = "\n\n".join(all_summaries)

prompt = f"""
You are an expert research advisor.

Analyze these research papers.

{combined_text}

Tasks:

1. Identify recurring limitations.
2. Find unexplored research areas.
3. Detect missing evaluations.
4. Suggest 5 research gaps.

Format:

Research Gap 1:
...

Research Gap 2:
...

Research Gap 3:
...

Research Gap 4:
...

Research Gap 5:
...
"""

response = gemini.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n")
print("=" * 80)
print("RESEARCH GAPS")
print("=" * 80)
print("\n")

print(response.text)