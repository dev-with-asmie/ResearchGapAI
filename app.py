import time
import json

from agents.project_ranking_agent import ProjectRankingAgent
from agents.paper_search_agent import PaperSearchAgent
from agents.paper_analysis_agent import PaperAnalysisAgent
from agents.research_gap_agent import ResearchGapAgent
from agents.idea_generator_agent import IdeaGeneratorAgent
from agents.local_gap_generator import LocalGapGenerator
from parsers.idea_parser import IdeaParser

from utils.save_json import save_json
from utils.save_report import save_report


# ---------------------------------
# User Input
# ---------------------------------

topic = input("Enter Topic: ")

print("\nSearching papers...\n")


# ---------------------------------
# Initialize Agents
# ---------------------------------

search_agent = PaperSearchAgent()
analysis_agent = PaperAnalysisAgent()
gap_agent = ResearchGapAgent()
local_gap_agent = LocalGapGenerator()
idea_agent = IdeaGeneratorAgent()
ranking_agent = ProjectRankingAgent()
parser = IdeaParser()


# ---------------------------------
# Search Papers
# ---------------------------------

papers = search_agent.search(topic)

if not papers:
    print("No papers found.")
    exit()

all_analysis = ""


# ---------------------------------
# Analyze Papers
# ---------------------------------

for paper in papers[:3]:

    print("\n" + "=" * 80)
    print("Title      :", paper["title"])
    print("Source     :", paper["source"])
    print("Year       :", paper["year"])
    print("Citations  :", paper["citations"])
    
 
    if not paper["summary"]:
        print("Skipping paper (No abstract found).")
        continue

    print("\nAnalyzing paper...\n")

    analysis = analysis_agent.analyze(
        paper["summary"]
    )

    print(analysis)

    all_analysis += f"""

TITLE:
{paper['title']}

SOURCE:
{paper.get('source', 'Unknown')}

{analysis}

"""

    time.sleep(2) 
print("\n")
print("=" * 80)
print("RESEARCH GAPS")
print("=" * 80)

gaps = gap_agent.find_gaps(all_analysis)

if (
    "unavailable" in gaps.lower()
    or "resource_exhausted" in gaps.lower()
    or "gemini unavailable" in gaps.lower()
):

    print("\nGemini unavailable.")
    print("Using Local Gap Generator...\n")

    gaps = local_gap_agent.generate(all_analysis)

print(gaps)


# ---------------------------------
# Generate Project Ideas
# ---------------------------------

print("\n")
print("=" * 80)
print("PROJECT IDEAS")
print("=" * 80)

ideas = idea_agent.generate(gaps)

print(ideas)


# ---------------------------------
# Parse Projects
# ---------------------------------

parsed_projects = parser.parse(ideas)

save_json(parsed_projects)


# ---------------------------------
# Display Parsed Projects
# ---------------------------------

print("\n")
print("=" * 80)
print("PARSED PROJECTS")
print("=" * 80)

for i, project in enumerate(parsed_projects, start=1):

    print(f"\nProject {i}")

    for key, value in project.items():
        print(f"{key}: {value}")


# ---------------------------------
# Rank Projects
# ---------------------------------

print("\n")
print("=" * 80)
print("PROJECT RANKING")
print("=" * 80)

ranking = ranking_agent.rank(ideas)

print("\nPROJECT RANKING\n")

if isinstance(ranking, dict):

    if "ranking" in ranking:

        for project in ranking["ranking"]:

            print("=" * 60)
            print(f"Rank : {project['rank']}")
            print(f"Title: {project['title']}")
            print(f"Score: {project['score']}/100")

            print("Strengths:")
            for s in project["strengths"]:
                print("-", s)

            print("Weaknesses:")
            for w in project["weaknesses"]:
                print("-", w)

        print("\nBEST PROJECT")
        print(ranking["best_project"]["title"])
        print(ranking["best_project"]["reason"])

    elif "ranking_text" in ranking:

        print(ranking["ranking_text"])

else:

    print(ranking) 

# ---------------------------------
# Save Report 
# ---------------------------------

full_report = f"""
RESEARCH TOPIC:
{topic}

================================================================================

PAPER ANALYSIS

{all_analysis}

================================================================================

RESEARCH GAPS

{gaps}

================================================================================

PROJECT IDEAS

{ideas}

================================================================================

PROJECT RANKING

{ranking}
"""

save_report(full_report)


print("\n")
print("=" * 80)
print("REPORT SAVED SUCCESSFULLY")
print("=" * 80)
print("JSON file : report/report.json")
print("PDF file  : report.pdf") 