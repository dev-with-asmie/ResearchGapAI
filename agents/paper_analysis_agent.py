from google import genai
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class PaperAnalysisAgent:

    def analyze(self, summary):

        prompt = f"""
You are an expert research paper reviewer.

Analyze the following research paper abstract.

Abstract:
{summary}

Return ONLY a valid JSON object in the following format:

{{
    "main_problem": "...",
    "methodology": "...",
    "key_contribution": "...",
    "limitations": [
        "...",
        "...",
        "..."
    ],
    "future_research": [
        "...",
        "...",
        "..."
    ]
}}

Rules:

1. Return ONLY valid JSON.
2. Do NOT use markdown.
3. Do NOT use ```json.
4. Every field MUST contain meaningful information.
5. Never leave any field empty.
6. If limitations or future work are not explicitly mentioned, infer them from the abstract.
7. Keep every answer concise (1–2 sentences).
"""

        models = [
            "gemini-2.5-flash",
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

                print("\n========== GEMINI RESPONSE ==========")
                print(text)
                print("=====================================\n")

                text = text.replace("```json", "")
                text = text.replace("```", "").strip()

                try:
                    return json.loads(text)

                except json.JSONDecodeError:

                    print("JSON Parsing Failed.")
                    print(text)

                    start = text.find("{")
                    end = text.rfind("}")

                    if start != -1 and end != -1:

                        try:
                            cleaned = text[start:end + 1]
                            return json.loads(cleaned)

                        except Exception:
                            pass

            except Exception as e:

                print(f"{model} Error:")
                print(e)

                if "RESOURCE_EXHAUSTED" in str(e):
                    print("Gemini quota exceeded.")
                    break

                if (
                    "503" in str(e)
                    or "UNAVAILABLE" in str(e)
                    or "INTERNAL" in str(e)
                ):
                    time.sleep(3)
                    continue

                time.sleep(2)

        print("Returning fallback response.")

        return {
            "main_problem": "Analysis unavailable.",
            "methodology": "Analysis unavailable.",
            "key_contribution": "Analysis unavailable.",
            "limitations": [
                "Unable to analyze the paper."
            ],
            "future_research": [
                "Try again later."
            ]
        }