import arxiv

client = arxiv.Client()

search = arxiv.Search(
    query='all:"quantum intrusion detection"', 
    max_results=5
)

for paper in client.results(search):
    print("\n" + "=" * 50)
    print("TITLE:", paper.title)
    print("AUTHORS:", ", ".join(author.name for author in paper.authors))
    print("\nABSTRACT:")
    print(paper.summary[:500]) 