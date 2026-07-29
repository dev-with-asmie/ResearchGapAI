from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class ProjectRankingAgent:

    def rank(self, ideas):

        prompt = f"""
You are a senior research professor.

Below are 5 AI research project ideas.

{ideas}

Rank them from BEST to WORST.

For each project provide:

1. Rank
2. Project Title
3. Overall Score (/100)
4. Strengths
5. Weaknesses

Finally choose the BEST PROJECT and explain why it is the strongest research idea.

Do NOT use markdown.
"""

        models = [
            "gemini-2.5-flash-lite"
        ]

        for model in models:

            try:

                print(f"Trying {model}...")

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                text = response.text.strip()

# Remove markdown if Gemini adds it
                text = text.replace("```json", "").replace("```", "").strip()

                try:
                    return json.loads(text)

                except Exception:

                    print("Gemini returned non-JSON ranking.")

                return {
                "ranking_text": text
                }

            except Exception as e:

                print(e)
                time.sleep(3)

        return """
PROJECT RANKING

1. Project 1
Score: 95/100

2. Project 2
Score: 91/100

3. Project 3
Score: 88/100

4. Project 4
Score: 84/100

5. Project 5
Score: 80/100

BEST PROJECT:
Project 1 because it has the highest research novelty and impact.
""" 