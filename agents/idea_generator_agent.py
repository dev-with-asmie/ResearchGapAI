from google import genai
from dotenv import load_dotenv
import os
import time

from agents.local_idea_generator import LocalIdeaGenerator

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

local_generator = LocalIdeaGenerator()


class IdeaGeneratorAgent:

    def generate(self, gaps):

        prompt = f"""
You are an expert AI research advisor.

Based on the following research gaps:

{gaps}

Generate EXACTLY 5 innovative AI research project ideas.

For EACH project, use EXACTLY this format:

Project Title:
Problem Solved:
Novelty:
Suggested Dataset:
Tech Stack:
Difficulty:
Resume Impact Score:
Give only a number from 1-10.

Research Potential Score:
Give only a number from 1-10. 

Rules:
- Do NOT use markdown.
- Do NOT use **.
- Do NOT number the projects.
- Do NOT add introductions or conclusions.
- Keep the field names exactly as written.
- Keep each field concise but informative.
"""

        models = [
            "gemini-2.5-flash-lite",
            "gemini-2.5-flash",
            "gemini-3.1-flash-lite"
        ]

        for model in models:

            try:

                print(f"Trying {model}...")

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if response.text:
                    return response.text.strip()

            except Exception as e:

                print(f"{model} failed")
                print(e)

                # Stop immediately if quota is exhausted
                if "RESOURCE_EXHAUSTED" in str(e):
                    break

                # Retry next model for temporary server issues
                if (
                    "503" in str(e)
                    or "UNAVAILABLE" in str(e)
                    or "INTERNAL" in str(e)
                ):
                    time.sleep(3)
                    continue

                time.sleep(2)

        print("\nGemini unavailable.")
        print("Using Local Idea Generator...\n")

        return local_generator.generate(gaps) 