import arxiv

topic = input("Topic: ")

search = arxiv.Search(
    query="""
    quantum computing OR
    quantum cybersecurity OR
    intrusion detection OR
    anomaly detection
    """,
    max_results=10
)

client = arxiv.Client()

for i, paper in enumerate(client.results(search), start=1):
    print("\n" + "="*80)
    print(f"PAPER {i}")
    print("="*80) 
    print("TITLE:", paper.title) 