import arxiv
from google import genai
from dotenv import load_dotenv
import os
import time

# Load API key
load_dotenv()

# Gemini Client
gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# arXiv Client
arxiv_client = arxiv.Client()

# User input
topic = input("Enter research topic: ")

# Search papers
search = arxiv.Search(
    query=topic,
    max_results=3,
    sort_by=arxiv.SortCriterion.Relevance
)

print("\nSearching papers...\n")

for i, paper in enumerate(arxiv_client.results(search), start=1):

    print("\n" + "=" * 80)
    print(f"PAPER {i}")
    print("=" * 80)

    print("\nTITLE:")
    print(paper.title)

    print("\nAUTHORS:")
    print(", ".join(author.name for author in paper.authors))

    abstract = paper.summary[:1000]

    prompt = f"""
You are a research analyst.

Analyze this paper abstract.

ABSTRACT:
{abstract}

Return the following sections:

1. Main Problem
2. Methodology
3. Key Contribution
4. Limitations
5. Future Research Directions

Keep answers concise.
"""

    print("\nAnalyzing...\n")

    try:

        response = gemini.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print(response.text)

    except Exception as e:

        print("Gemini Error:")
        print(e)

    time.sleep(2)

print("\nDone!")  