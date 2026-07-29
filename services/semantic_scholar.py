import requests


class SemanticScholarService:

    BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

    def search(self, topic):

        params = {

            "query": topic,

            "limit": 10,

            "fields": "title,abstract,year,citationCount,authors,url"

        }

        try:

            response = requests.get(

                self.BASE_URL,

                params=params,

                timeout=20

            )

            if response.status_code == 429:

                print("\nSemantic Scholar Rate Limited.\n")

                return []

            response.raise_for_status()

            data = response.json()

            papers = []

            for paper in data.get("data", []):

                        papers.append({

                        "title": paper.get("title", ""),

                        "authors": ", ".join(
                            author.get("name", "")
                            for author in paper.get("authors", [])
                        ),

                        "summary": (paper.get("abstract") or "")[:2000],

                        "year": paper.get("year", ""),

                        "citations": paper.get("citationCount", 0),

                        "source": "Semantic Scholar",

                        "url": paper.get("url", "")

                    })

            return papers

        except Exception as e:

            print("Semantic Scholar Error:", e)

            return [] 