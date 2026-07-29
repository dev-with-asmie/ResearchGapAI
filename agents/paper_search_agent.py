import arxiv

from services.semantic_scholar import SemanticScholarService


class PaperSearchAgent:

    def __init__(self):

        self.semantic = SemanticScholarService()

    def search(self, topic):

        papers = []

        # ---------------------------------
        # Search arXiv
        # ---------------------------------

        search = arxiv.Search(

            query=topic,

            max_results=10,

            sort_by=arxiv.SortCriterion.Relevance

        )

        client = arxiv.Client()

        try:

            for paper in client.results(search):

                papers.append({

                 "title": paper.title,

                 "authors": ", ".join(author.name for author in paper.authors),

                 "summary": paper.summary[:2000],

                 "year": paper.published.year,

                 "citations": 0,

                 "source": "arXiv",

                 "url": paper.entry_id

            })

        except Exception as e:

            print("arXiv Error:", e)

        # ---------------------------------
        # Search Semantic Scholar
        # ---------------------------------

        try:

            semantic_papers = self.semantic.search(topic)

            papers.extend(semantic_papers)

        except Exception as e:

            print("Semantic Scholar Error:", e)

        # ---------------------------------
        # Remove Duplicate Titles
        # ---------------------------------

        unique = {}

        for paper in papers:

            title = paper["title"].strip().lower()

            if title not in unique:

                unique[title] = paper

        papers = list(unique.values())

        # ---------------------------------
        # Keyword Filtering
        # ---------------------------------

        keywords = topic.lower().split()

        filtered = []

        for paper in papers:

            text = (

                paper["title"] +

                " " +

                paper["summary"]

            ).lower()

            score = sum(

                keyword in text

                for keyword in keywords

            )

            if score >= 2:

                filtered.append((score, paper))

        if filtered:

            filtered.sort(

                key=lambda x: (

                    x[0],

                    x[1].get("citations", 0)

                ),

                reverse=True

            )

            papers = [

                paper

                for _, paper in filtered

            ]

        else:

            papers.sort(

                key=lambda x: x.get(

                    "citations",

                    0

                ),

                reverse=True

            )

        return papers[:10] 