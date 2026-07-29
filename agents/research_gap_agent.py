from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class ResearchGapAgent:

    def find_gaps(self, analyses):

        prompt = f"""
You are an expert AI research advisor.

Analyze the following research paper analyses.

{analyses}

Generate the output in EXACTLY the following format.

Recurring Limitations:
- limitation 1
- limitation 2
- limitation 3

Unexplored Research Areas:
- area 1
- area 2
- area 3

Missing Evaluations:
- evaluation 1
- evaluation 2
- evaluation 3

Research Opportunities:
- opportunity 1
- opportunity 2
- opportunity 3
- opportunity 4
- opportunity 5

Top 5 Research Gaps:
1.
2.
3.
4.
5.

Rules:
- Do NOT use markdown.
- Do NOT use **.
- Do NOT add introductions.
- Do NOT explain your reasoning.
- Return only the requested sections.
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

                # Stop if daily quota is exhausted
                if "RESOURCE_EXHAUSTED" in str(e):
                    break

                # Try another model if server is busy
                if (
                    "503" in str(e)
                    or "UNAVAILABLE" in str(e)
                    or "INTERNAL" in str(e)
                ):
                    time.sleep(3)
                    continue

                time.sleep(2)

        return """
Research gap generation unavailable. 
Please try again later.
"""